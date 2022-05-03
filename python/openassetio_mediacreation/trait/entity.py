# SPDX-License-Identifier: Apache-2.0
# Copyright 2013-2022 The Foundry Visionmongers Ltd
"""
Traits that can be composed within a specification to define
characteristics of an entity for resolve or registration.
"""

from typing import Union

from openassetio import Trait


class LocatableContentTrait(Trait):
    """
    This trait characterizes an entity whose data is persisted externally
    to the API - either in a file on disk or other storage accessible
    via a URL.

    The `location` property holds the most applicable location of the
    entity's content for the current process environment - considering
    platform, host, etc. Location is in the form of a file system path
    unless the calling context's locale has the `usesUrls` trait. In
    which case it is a URL.
    """

    kId = "locatableContent"

    __kLocation = "location"

    def setLocation(self, contentLocation: str):
        """
        Sets the location of the entities external content.

        This must be a filesystem path, unless the calling context's
        `locale` has the `usesUrls` trait, then it must be an URL.
        """
        if not isinstance(contentLocation, str):
            raise TypeError("contentLocation must be a string")
        self._specification.setTraitProperty(self.kId, self.__kLocation, contentLocation)

    def getLocation(self, defaultValue=None) -> Union[str, None]:
        """
        Returns the location of the entities external content or None
        if this property has not been set.

        By default, this is a filesystem path for broadest
        compatibility.

        If the calling context's `locale` has the `usesURLs` trait, then
        it will be will be an URL.
        """
        value = self._specification.getTraitProperty(self.kId, self.__kLocation)
        if value is None:
            return defaultValue
        elif not isinstance(value, str):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{value}' [{type(value).__name__}]")
            return defaultValue
        return value
