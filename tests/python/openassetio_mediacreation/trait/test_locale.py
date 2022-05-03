# SPDX-License-Identifier: Apache-2.0
# Copyright 2013-2022 The Foundry Visionmongers Ltd
"""
Basic tests for locale traits.
"""

# pylint: disable=missing-function-docstring, missing-class-docstring
# pylint: disable=no-self-use, redefined-outer-name, invalid-name
# pylint: disable=too-few-public-methods

##
## URLReaderTrait
##

from openassetio_mediacreation.trait.locale import UsesUrlsTrait


class Test_UsesUrlsTrait:
    def test_id(self):
        assert UsesUrlsTrait.kId == "usesUrls"
