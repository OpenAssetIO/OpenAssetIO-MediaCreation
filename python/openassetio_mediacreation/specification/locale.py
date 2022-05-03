# SPDX-License-Identifier: Apache-2.0
# Copyright 2013-2022 The Foundry Visionmongers Ltd
"""
Specifications that can be used to define characteristics of the
calling context within an API host. These should be set in the
`locale` property of the `Context` object supplied to each call by
the host.
"""

from openassetio import Specification

from ..trait.locale import UsesUrlsTrait


class UsesUrlsLocale(Specification):
    """
    A locale for generic access to external entity content that uses
    URLs instead of file paths. In the majority of situations some more
    specialized specification should be used that composes these traits
    with its own.
    """
    # pylint: disable=too-few-public-methods

    kTraitIDs = {UsesUrlsTrait.kId}

    def __init__(self):
        super().__init__(self.kTraitIDs)

    def usesUrlsTrait(self) -> UsesUrlsTrait:
        """
        Returns an instance of the UsesUrlsTrait bound to the data held
        by the specification.
        """
        return UsesUrlsTrait(self)
