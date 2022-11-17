# SPDX-License-Identifier: Apache-2.0
# Copyright 2013-2022 The Foundry Visionmongers Ltd
"""
Traits that can be composed within a specification to define
characteristics of an entity for resolve or registration.
"""

from typing import Union

from openassetio import TraitBase


class LocatableContentTrait(TraitBase):
    """
    This trait characterizes an entity whose data is persisted externally
    to the API through data accessible via a valid URL.

    The `location` property holds the most applicable location of the
    entity's content for the current process environment - considering
    platform, host, etc. Location is in the form of a URL.
    """

    kId = "locatableContent"

    __kLocation = "location"

    def setLocation(self, contentLocation: str):
        """
        Sets the location of the entities external content.

        This must be a valid URL so special characters need to be
        encoded.
        """
        if not isinstance(contentLocation, str):
            raise TypeError("contentLocation must be a string")
        self._data.setTraitProperty(self.kId, self.__kLocation, contentLocation)

    def getLocation(self, defaultValue=None) -> Union[str, None]:
        """
        Returns the location of the entities external content or None
        if this property has not been set.

        This is a URL, and so special characters will be encoded.
        """
        value = self._data.getTraitProperty(self.kId, self.__kLocation)
        if value is None:
            return defaultValue
        elif not isinstance(value, str):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{value}' [{type(value).__name__}]")
            return defaultValue
        return value
