# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 The Foundry Visionmongers Ltd

"""
A WIP sketch of how OpenAssetIO can be used to discover alternate
representations of an Entity, for example - proxy versions of image
sequences.
"""

import sys

from typing import Dict, List, NamedTuple, Set

from openassetio import BatchElementError, Context, EntityReference, TraitsData
from openassetio.exceptions import EntityResolutionError
from openassetio.hostApi import HostInterface, Manager, ManagerFactory
from openassetio.log import ConsoleLogger, SeverityFilter
from openassetio.pluginSystem import PythonPluginSystemManagerImplementationFactory

from openassetio_mediacreation.traits.representation import OriginalTrait, ProxyTrait
from openassetio_mediacreation.specifications.locale import ExampleCodeCLISpecification
from openassetio_mediacreation.specifications.image import RasterImageSequenceSpecification


class ProxyWorkflowsHost(HostInterface):
    """
    The class that identifies this script to OpenAssetIO.
    """

    def identifier(self):
        return "org.openassetio.mediacreation.examples.proxyWorkflows.host"

    def displayName(self):
        return "Proxy Workflows Demo"


class EntityRepresentations(NamedTuple):
    """
    Information about alternate representations of some entity.
    """

    source: EntityReference
    original: EntityReference
    proxies: List[EntityReference]
    # EntityReferences aren't currently hashable, see:
    #   https://github.com/OpenAssetIO/OpenAssetIO/issues/802
    data: Dict[str, TraitsData]


def get_all_representations(
    entity_reference: EntityReference, entity_trait_set: Set, manager: Manager, context: Context
) -> EntityRepresentations:
    """
    Gets all available representations (original/proxy) for some Entity.
    """

    # Make sure we're using the correct context
    context.access = context.Access.kRead

    # We use the getRelatedReferences mechanism to ask the Manager for
    # any other representations it may know about. We use the form where
    # we ask for multiple alternate relation types for a single source
    # reference.

    relationships = [
        # Ensure we know which entity is the "original"
        TraitsData({OriginalTrait.kId}),
        # See if there are any proxies
        TraitsData({ProxyTrait.kId})
    ]

    # NB. getRelatedReferences hasn't been moved over to the new
    # batch/callback syntax yet.

    relations = manager.getRelatedReferences(
        [entity_reference],
        relationships,
        context,
        # Constrain the results to the same "type" of entity as
        # the original, eg: image sequences
        resultTraitSet=entity_trait_set,
    )

    # The result is a list corresponding to the input relations list

    # OriginalTrait relations - expect there to only be one
    original_ref = relations[0][0] if relations[0] else None
    # ProxyTrait relations
    proxy_refs = relations[1]

    # Early out if we don't have any relations at all
    if not (original_ref or proxy_refs):
        return EntityRepresentations(entity_reference, None, [], {})

    # If we do, resolve the references to find out about their entities

    # Resolve all the requested entity traits, and additionally the
    # proxy trait to see if we have more information about those.
    # Inapplicable traits are simply ignored by the manager rather than
    # causing an error.
    traits_to_resolve = entity_trait_set | {ProxyTrait.kId}

    all_refs = [original_ref] + proxy_refs if original_ref else proxy_refs

    # The batch API uses a callback mechanism. There are plans to add
    # conveniences for exception based workflows, but these haven't
    # been written yet...

    # We'll build a map of entity data, keyed by its reference
    all_data = {}

    def resolve_cb(index: int, entity_data: TraitsData):
        # https://github.com/OpenAssetIO/OpenAssetIO/issues/802
        all_data[all_refs[index].toString()] = entity_data

    # We shouldn't really error as we're resolving references the
    # manager has only just provided us...
    def error_cb(index: int, error: BatchElementError):
        raise EntityResolutionError(error.message, all_refs[index])

    manager.resolve(all_refs, traits_to_resolve, context, resolve_cb, error_cb)

    return EntityRepresentations(entity_reference, original_ref, proxy_refs, all_data)


def __print_traits_data(data: TraitsData):
    """
    Prints out the contents of the supplied TraitsData in a
    terminal-friendly way.
    """
    # We don't have any convenience conversions to dicts etc. yet.
    # See https://github.com/OpenAssetIO/OpenAssetIO/issues/795
    as_dict = {
        trait_id: {
            property_key: data.getTraitProperty(trait_id, property_key)
            for property_key in data.traitPropertyKeys(trait_id)
        }
        for trait_id in data.traitSet()
    }

    for trait_id, trait_data in as_dict.items():
        if trait_data:
            print(f"  - {trait_id}:")
            for key, value in trait_data.items():
                print(f"      {key}: {value}")
        else:
            print(f"  - {trait_id}")


def main():
    """
    Queries the default manager for alternate image sequence
    representations of the entity reference supplied as the first CLI
    argument, and prints them to stdout.
    """

    # Bootstrap the API using the default manager

    logger = SeverityFilter(ConsoleLogger())

    manager = ManagerFactory.defaultManagerForInterface(
        ProxyWorkflowsHost(), PythonPluginSystemManagerImplementationFactory(logger), logger
    )

    if not manager:
        raise RuntimeError(
            "No default manager configured, "
            f"check ${ManagerFactory.kDefaultManagerConfigEnvVarName}"
        )

    # We can now talk to the manager

    # Will throw if input is not an entity reference understood by the manager
    entity_reference = manager.createEntityReference(sys.argv[1])

    # The context is used to describe who is using the API and tie together
    # related calls into the API
    context = manager.createContext()
    context.locale = ExampleCodeCLISpecification.create().traitsData()
    context.retention = context.Retention.kTransient

    # See what what image representations we can find for this entity
    representations = get_all_representations(
        entity_reference, RasterImageSequenceSpecification.kTraitSet, manager, context
    )

    # Make a mess of the terminal with the data we got back...
    # This could easily be used to build OTIO multi-ref timelines, etc...
    print(f"Representations for: {representations.source.toString()}")
    if representations.original:
        print(f"\nOriginal:\n\n{representations.original.toString()}")
        __print_traits_data(representations.data[representations.original.toString()])
    if representations.proxies:
        print("\nProxies:\n")
        for proxy in representations.proxies:
            print(f" {proxy.toString()}")
            __print_traits_data(representations.data[proxy.toString()])
            print("")


if __name__ == "__main__":
    main()
