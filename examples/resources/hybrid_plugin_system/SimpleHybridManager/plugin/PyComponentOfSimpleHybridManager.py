# SPDX-License-Identifier: BSD-3-Clause
# Copyright 2024 The Foundry Visionmongers Ltd
"""
A single-class module, providing the SimpleHybridManagerInterface class.
"""
# pylint: disable=unused-argument

from openassetio.trait import TraitsData
from openassetio.errors import BatchElementError
from openassetio.access import PolicyAccess, EntityTraitsAccess
from openassetio.managerApi import ManagerInterface
from openassetio.pluginSystem import PythonPluginSystemManagerPlugin

from openassetio_mediacreation.traits.content import LocatableContentTrait
from openassetio_mediacreation.traits.managementPolicy import ManagedTrait
from openassetio_mediacreation.traits.usage import EntityTrait

# Unique ID of the plugin. Must match that advertised by the partner C++
# plugin.
kPluginId = "org.openassetio.examples.simplehybridmanager"
# The one and only entity reference we support.
kTheEntityReference = "examplehybrid://example_entity"


class SimpleHybridManagerInterface(ManagerInterface):
    """
    Python side of the hybrid plugin.
    """

    def identifier(self):
        """
        Identifier must match the partner C++ plugin's identifier.
        """
        return kPluginId

    def displayName(self):
        """
        This display name will be used if the Python plugin system takes
        precedence in the hybrid plugin system.
        """
        return "Simple Hybrid Manager"

    def hasCapability(self, capability):
        """
        This plugin supports only the minimal required set of
        capabilities. It does not even support `resolve`. However, the
        partner C++ plugin does support `resolve`.
        """
        if capability in (
            ManagerInterface.Capability.kEntityReferenceIdentification,
            ManagerInterface.Capability.kManagementPolicyQueries,
            ManagerInterface.Capability.kEntityTraitIntrospection,
        ):
            return True

        return False

    def managementPolicy(self, traitSets, policyAccess, context, hostSession):
        """
        Only support reading file paths (or URLs).
        """
        policies = [TraitsData() for _ in traitSets]
        if policyAccess != PolicyAccess.kRead:
            # We only support read access.
            return policies

        for trait_set, policy_data in zip(traitSets, policies):
            if not {EntityTrait.kId, LocatableContentTrait.kId} <= trait_set:
                # We only support file entities.
                continue
            ManagedTrait.imbueTo(policy_data)

        return policies

    def isEntityReferenceString(self, someString, hostSession):
        """
        Both Python and C++ plugins should expect the same entity
        reference format.
        """
        return someString.startswith("examplehybrid://")

    def entityTraits(
        self,
        entityReferences,
        entityTraitsAccess,
        context,
        _hostSession,
        successCallback,
        errorCallback,
    ):
        """
        This Python plugin provides introspection of entities to get
        their trait set, whereas the values for the properties of the
        traits are `resolve`d through the partner C++ plugin.
        """

        # Only support reading.
        if entityTraitsAccess != EntityTraitsAccess.kRead:
            result = BatchElementError(
                BatchElementError.ErrorCode.kEntityAccessError, "Entities are read-only"
            )
            for idx in range(len(entityReferences)):
                errorCallback(idx, result)
            return

        for idx, ref in enumerate(entityReferences):
            if ref.toString() == kTheEntityReference:
                successCallback(idx, {EntityTrait.kId, LocatableContentTrait.kId})
            else:
                errorCallback(
                    idx,
                    BatchElementError(
                        BatchElementError.ErrorCode.kEntityResolutionError,
                        f"Entity '{ref.toString()}' not found",
                    ),
                )


class SimpleHybridManagerPlugin(PythonPluginSystemManagerPlugin):
    """
    Entry point for the plugin.
    """

    @staticmethod
    def identifier():
        """
        Identifier must match the partner C++ plugin's identifier.
        """
        return kPluginId

    @classmethod
    def interface(cls):
        """
        Create the Python side of the hybrid plugin interface.
        """
        return SimpleHybridManagerInterface()


# Public entry point that will be searched for by the plugin system.
# pylint: disable=invalid-name
openassetioPlugin = SimpleHybridManagerPlugin
