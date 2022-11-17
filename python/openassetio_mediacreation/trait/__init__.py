# SPDX-License-Identifier: Apache-2.0
# Copyright 2013-2022 The Foundry Visionmongers Ltd
"""
A collection of well-known traits for use within the Media Creation
industry.

Traits at this level may be used for multiple purposes. Those specific
to certain applications are grouped into modules by use.
"""


from typing import Union

from openassetio import TraitBase


class TimelineTrait(TraitBase):
    """
    This trait characterizes a collection of tracks that evaluate
    concurrently to form layers of references to media. Frequently used
    in non-linear editing environments such as Video and Audio post
    production tools.
    """

    kId = "timeline"


class TrackTrait(TraitBase):
    """
    This trait characterizes a lane or collection of media, arranged
    temporally such that only a single item in the collection is active
    at any given time. Frequently used in non-linear editing
    environments such as Video and Audio post production tools.
    """

    kId = "track"


class ClipTrait(TraitBase):
    """
    This trait characterizes the use of some range of external media,
    commonly on a track or timeline. Frequently used in non-linear
    editing environments such as Video and Audio production tools.

    TODO(TC): Define any additional properties, and companion traits
    such as 'frameRange' and 'handles'.
    """

    kId = "clip"

    __kName = "name"

    def setName(self, name: str):
        """
        Sets the name of the clip.
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self._data.setTraitProperty(self.kId, self.__kName, name)

    def getName(self, defaultValue=None) -> Union[str, None]:
        """
        Returns the name of the clip or the defaultValue.
        """
        value = self._data.getTraitProperty(self.kId, self.__kName)
        if value is None:
            return defaultValue
        elif not isinstance(value, str):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{value}' [{type(value).__name__}]")
            return defaultValue
        return value
