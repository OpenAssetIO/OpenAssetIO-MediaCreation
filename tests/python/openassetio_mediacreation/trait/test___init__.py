# SPDX-License-Identifier: Apache-2.0
# Copyright 2013-2022 The Foundry Visionmongers Ltd
"""
Basic tests for common entity traits.
"""

# pylint: disable=missing-function-docstring, missing-class-docstring
# pylint: disable=no-self-use, redefined-outer-name, invalid-name
# pylint: disable=too-few-public-methods,wrong-import-position

import pytest

from openassetio import Specification

##
## TimelineTrait
##

from openassetio_mediacreation.trait import TimelineTrait


class Test_TimelineTrait:
    def test_traitId(self):
        assert TimelineTrait.kId == "timeline"


##
## TrackTrait
##

from openassetio_mediacreation.trait import TrackTrait


class Test_TrackTrait:
    def test_traitId(self):
        assert TrackTrait.kId == "track"


##
## ClipTrait
##

from openassetio_mediacreation.trait import ClipTrait


class Test_ClipTrait:
    def test_traitId(self):
        assert ClipTrait.kId == "clip"


class Test_ClipTrait_name:
    def test_when_spec_does_not_have_clip_trait_then_raises_IndexError(
        self, an_empty_specification
    ):
        trait = ClipTrait(an_empty_specification)
        with pytest.raises(IndexError):
            trait.getName()

    def test_when_name_property_is_set_then_returns_name(self, a_clip_specification):
        expected = "yet another name"
        a_clip_specification.setTraitProperty(ClipTrait.kId, "name", expected)
        assert ClipTrait(a_clip_specification).getName() == expected

    def test_when_name_property_not_set_then_returns_None(self, a_clip_specification):
        assert ClipTrait(a_clip_specification).getName() is None

    def test_when_name_property_is_not_set_and_default_provided_then_returns_default(
        self, a_clip_specification
    ):
        default = "a default name"
        actual = ClipTrait(a_clip_specification).getName(defaultValue=default)
        assert actual == default

    def test_when_name_property_has_wrong_type_and_no_default_provided_then_raises_TypeError(
        self, a_clip_specification
    ):
        a_clip_specification.setTraitProperty(ClipTrait.kId, "name", 123)
        with pytest.raises(TypeError) as err:
            assert ClipTrait(a_clip_specification).getName()
        assert str(err.value) == "Invalid stored value type: '123' [int]"

    def test_when_name_property_has_wrong_value_type_and_default_provided_then_returns_default(
        self, a_clip_specification
    ):
        a_clip_specification.setTraitProperty(ClipTrait.kId, "name", 123)
        trait = ClipTrait(a_clip_specification)
        default = "a default name"
        assert trait.getName(defaultValue=default) == default


class Test_ClipTrait_setName:
    def test_when_spec_does_not_have_clip_trait_then_raises_IndexError(
        self, an_empty_specification
    ):
        trait = ClipTrait(an_empty_specification)
        with pytest.raises(IndexError):
            trait.setName("a name")

    def test_when_set_then_expected_trait_property_is_set(self, a_clip_specification):
        trait = ClipTrait(a_clip_specification)
        expected = "another name"
        trait.setName(expected)
        actual = a_clip_specification.getTraitProperty(ClipTrait.kId, "name")
        assert actual == expected

    def test_when_name_type_is_wrong_then_TypeError_is_raised(self, a_clip_specification):
        trait = ClipTrait(a_clip_specification)
        with pytest.raises(TypeError) as err:
            trait.setName(123)
        assert str(err.value) == "name must be a string"


@pytest.fixture
def an_empty_specification():
    return Specification(set())


@pytest.fixture
def a_clip_specification():
    return Specification({ClipTrait.kId})
