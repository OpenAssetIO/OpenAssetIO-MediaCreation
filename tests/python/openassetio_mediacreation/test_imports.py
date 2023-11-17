# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 The Foundry Visionmongers Ltd
"""
Test MediaCreation traits and specifications can be imported
"""

# pylint: disable=no-self-use
# pylint: disable=invalid-name
# pylint: disable=unused-import,import-outside-toplevel
# pylint: disable=missing-class-docstring,missing-function-docstring

import pytest


@pytest.fixture(autouse=True)
def always_unload_openassetio_mediacreation_modules(
    unload_openassetio_mediacreation_modules,  # pylint: disable=unused-argument
):
    """
    Removes openassetio modules from the sys.modules cache that
    otherwise mask cyclic dependencies.
    """


class Test_package_imports:
    def test_importing_openassetio_mediacreation_succeeds(self):
        import openassetio_mediacreation

    def test_importing_traits_succeeds(self):
        from openassetio_mediacreation import traits

    def test_importing_specifications_succeeds(self):
        from openassetio_mediacreation import specifications


class Test_trait_imports_content:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import content

    def test_importing_LocatableContentTrait_succeeds(self):
        from openassetio_mediacreation.traits.content import LocatableContentTrait


class Test_trait_imports_managementPolicy:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import managementPolicy

    def test_importing_ManagedTrait_succeeds(self):
        from openassetio_mediacreation.traits.managementPolicy import ManagedTrait


class Test_trait_imports_identity:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import identity

    def test_importing_DisplayNameTrait_succeeds(self):
        from openassetio_mediacreation.traits.identity import DisplayNameTrait


class Test_trait_imports_auth:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import auth

    def test_importing_BearerToken_succeeds(self):
        from openassetio_mediacreation.traits.auth import BearerTokenTrait


class Test_trait_imports_usage:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import usage

    def test_importing_Entity_succeeds(self):
        from openassetio_mediacreation.traits.usage import EntityTrait

    def test_importing_Relationship_succeeds(self):
        from openassetio_mediacreation.traits.usage import RelationshipTrait


class Test_trait_imports_lifecycle:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import lifecycle

    def test_importing_Version_succeeds(self):
        from openassetio_mediacreation.traits.lifecycle import VersionTrait

    def test_importing_Stable_succeeds(self):
        from openassetio_mediacreation.traits.lifecycle import StableTrait


class Test_trait_imports_relationship:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import relationship

    def test_importing_Singular_succeeds(self):
        from openassetio_mediacreation.traits.relationship import SingularTrait

    def test_importing_Unbounded_succeeds(self):
        from openassetio_mediacreation.traits.relationship import UnboundedTrait


class Test_specification_imports_lifecycle:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.specifications import lifecycle

    def test_importing_EntityVersionsRelationship_succeeds(self):
        from openassetio_mediacreation.specifications.lifecycle import (
            EntityVersionsRelationshipSpecification,
        )

    def test_importing_StableEntityVersionsRelationship_succeeds(self):
        from openassetio_mediacreation.specifications.lifecycle import (
            StableEntityVersionsRelationshipSpecification,
        )

    def test_importing_StableReferenceRelationship_succeeds(self):
        from openassetio_mediacreation.specifications.lifecycle import (
            StableReferenceRelationshipSpecification,
        )
