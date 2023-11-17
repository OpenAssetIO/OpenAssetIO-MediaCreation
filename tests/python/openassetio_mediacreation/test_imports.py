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
