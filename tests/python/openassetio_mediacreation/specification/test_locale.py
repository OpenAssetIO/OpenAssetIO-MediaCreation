# SPDX-License-Identifier: Apache-2.0
# Copyright 2013-2022 The Foundry Visionmongers Ltd
"""
Basic tests for locale specifications.
"""

# pylint: disable=missing-function-docstring, missing-class-docstring
# pylint: disable=no-self-use, redefined-outer-name, invalid-name

import pytest

##
## UsesUrlsLocale
##

from openassetio_mediacreation.specification.locale import UsesUrlsLocale
from openassetio_mediacreation.trait.locale import UsesUrlsTrait


class Test_UsesUrlsLocale:
    def test_traitIds(self):
        assert UsesUrlsLocale.kTraitIDs == {UsesUrlsTrait.kId}

    def test_when_constructed_then_imbues_traits(self, a_usesUrls_locale):
        assert a_usesUrls_locale.hasTrait(UsesUrlsTrait.kId)


class Test_UsesUrlsLocale_usesUrlsTrait:
    def test_returns_correct_trait(self, a_usesUrls_locale):
        trait = a_usesUrls_locale.usesUrlsTrait()
        assert isinstance(trait, UsesUrlsTrait)

    def test_returns_trait_wrapping_the_locale(self, a_usesUrls_locale):
        trait = a_usesUrls_locale.usesUrlsTrait()
        assert trait.isValid() is True


@pytest.fixture
def a_usesUrls_locale():
    return UsesUrlsLocale()
