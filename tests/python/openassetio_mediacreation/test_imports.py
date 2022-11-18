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


class Test_trait_imports:
    def test_importing_openassetio_mediacreation_succeeds(self):
        import openassetio_mediacreation

    def test_importing_traits_succeeds(self):
        from openassetio_mediacreation import traits

    def test_importing_timeline_succeeds(self):
        from openassetio_mediacreation.traits import timeline

    def test_importing_content_succeeds(self):
        from openassetio_mediacreation.traits import content

    def test_importing_ClipTrait_succeeds(self):
        from openassetio_mediacreation.traits.timeline import ClipTrait

    def test_importing_TimelineTrait_succeeds(self):
        from openassetio_mediacreation.traits.timeline import TimelineTrait

    def test_importing_TrackTrait_succeeds(self):
        from openassetio_mediacreation.traits.timeline import TrackTrait

    def test_importing_LocatableContentTrait_succeeds(self):
        from openassetio_mediacreation.traits.content import LocatableContentTrait
