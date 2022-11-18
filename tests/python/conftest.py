# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 The Foundry Visionmongers Ltd
"""
Shared fixtures/code for pytest cases.
"""


import sys

import pytest

# pylint: disable=invalid-name


@pytest.fixture
def unload_openassetio_mediacreation_modules():
    """
    Temporarily removes openassetio_mediacreation modules from the
    sys.modules cache that otherwise mask cyclic dependencies or bleed
    state from a previous test case. We restore them afterwards to avoid
    issues where module-level imports in preceding tests end up with
    references to the deleted module. This causes `isinstance` and
    others to fail as the compared classes are at different addresses.
    """
    to_delete = {
        name: module
        for name, module in sys.modules.items()
        if name.startswith("openassetio_mediacreation")
    }
    # Remove the target modules from the cache
    for name in to_delete.keys():
        del sys.modules[name]
    # Yield to allow the target test to run
    yield
    # Restore the previously imported modules
    for name, module in to_delete.items():
        sys.modules[name] = module
