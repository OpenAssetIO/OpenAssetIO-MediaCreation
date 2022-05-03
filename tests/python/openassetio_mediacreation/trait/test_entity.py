# SPDX-License-Identifier: Apache-2.0
# Copyright 2013-2022 The Foundry Visionmongers Ltd
"""
Basic tests for entity traits.
"""

# pylint: disable=missing-function-docstring, missing-class-docstring
# pylint: disable=no-self-use, redefined-outer-name, invalid-name
# pylint: disable=too-few-public-methods

import pytest

from openassetio import Specification

##
## LocatableContentTrait
##

from openassetio_mediacreation.trait.entity import LocatableContentTrait


class Test_LocatableContentTrait:
    def test_traitId(self):
        assert LocatableContentTrait.kId == "locatableContent"


class Test_LocatableContentTrait_location:
    def test_when_spec_does_not_have_locatableContent_trait_then_raises_IndexError(
        self, an_empty_specification
    ):
        trait = LocatableContentTrait(an_empty_specification)
        with pytest.raises(IndexError):
            trait.getLocation()

    def test_when_location_property_is_set_then_returns_location(
        self, a_locatableContent_specification
    ):
        expected = "yet another location"
        a_locatableContent_specification.setTraitProperty(
            LocatableContentTrait.kId, "location", expected
        )
        assert LocatableContentTrait(a_locatableContent_specification).getLocation() == expected

    def test_when_location_property_not_set_then_returns_None(
        self, a_locatableContent_specification
    ):
        assert LocatableContentTrait(a_locatableContent_specification).getLocation() is None

    def test_when_location_property_is_not_set_and_default_provided_then_returns_default(
        self, a_locatableContent_specification
    ):
        default = "a default location"
        actual = LocatableContentTrait(a_locatableContent_specification).getLocation(
            defaultValue=default
        )
        assert actual == default

    def test_when_location_property_has_wrong_type_and_no_default_provided_then_raises_TypeError(
        self, a_locatableContent_specification
    ):
        a_locatableContent_specification.setTraitProperty(
            LocatableContentTrait.kId, "location", 123
        )
        with pytest.raises(TypeError) as err:
            assert LocatableContentTrait(a_locatableContent_specification).getLocation()
        assert str(err.value) == "Invalid stored value type: '123' [int]"

    def test_when_location_property_has_wrong_value_type_and_default_provided_then_returns_default(
        self, a_locatableContent_specification
    ):
        a_locatableContent_specification.setTraitProperty(
            LocatableContentTrait.kId, "location", 123
        )
        trait = LocatableContentTrait(a_locatableContent_specification)
        default = "a default location"
        assert trait.getLocation(defaultValue=default) == default


class Test_LocatableContentTrait_setLocation:
    def test_when_spec_does_not_have_locatableContent_trait_then_raises_IndexError(
        self, an_empty_specification
    ):
        trait = LocatableContentTrait(an_empty_specification)
        with pytest.raises(IndexError):
            trait.setLocation("a location")

    def test_when_set_then_expected_trait_property_is_set(self, a_locatableContent_specification):
        trait = LocatableContentTrait(a_locatableContent_specification)
        expected = "another location"
        trait.setLocation(expected)
        actual = a_locatableContent_specification.getTraitProperty(
            LocatableContentTrait.kId, "location"
        )
        assert actual == expected

    def test_when_location_type_is_wrong_then_TypeError_is_raised(
        self, a_locatableContent_specification
    ):
        trait = LocatableContentTrait(a_locatableContent_specification)
        with pytest.raises(TypeError) as err:
            trait.setLocation(123)
        assert str(err.value) == "contentLocation must be a string"


@pytest.fixture
def an_empty_specification():
    return Specification(set())


@pytest.fixture
def a_locatableContent_specification():
    return Specification({LocatableContentTrait.kId})
