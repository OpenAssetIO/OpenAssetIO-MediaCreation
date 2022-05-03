# SPDX-License-Identifier: Apache-2.0
# Copyright 2013-2022 The Foundry Visionmongers Ltd
"""
Traits that can be composed within a specification to define
characteristics of the calling context within an API host.
"""

from openassetio import Trait


class UsesUrlsTrait(Trait):
    """
    This trait can be used in a calling context `locale` to control
    the data resolved for the `locatableContent` trait.

    By default, the `location` property of the `locatableContent` trait
    holds a file system path appropriate for the host process. When this
    trait is set, then the property should instead hold a valid URL.

    A host that supports loading data through URLs should set this trait
    to allow alternate schemes to be used.
    """

    kId = "usesUrls"
