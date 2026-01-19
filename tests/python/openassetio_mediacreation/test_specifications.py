# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 The Foundry Visionmongers Ltd
"""
Tests Specifications include required traits.
"""

# pylint: disable=no-self-use
# pylint: disable=invalid-name
# pylint: disable=missing-class-docstring

import inspect

import pytest

from openassetio_mediacreation.traits.usage import EntityTrait, RelationshipTrait
from openassetio_mediacreation import specifications


class Test_specification_traits:
    def test_contain_usage_trait(self):
        """
        All specifications should contain one trait from the usage namespace
        so that their purpose can be determined at runtime.
        """
        for cls in self.__specifications():
            # Ensure exactly one is present
            assert (EntityTrait.kId in cls.kTraitSet) != (RelationshipTrait.kId in cls.kTraitSet)

    def test_traits_constructible(self):
        """
        Asserts that specifications reference valid traits, without
        relying on private knowledge that the trait set already uses
        their Id attribute.
        """
        for cls in self.__specifications():
            instance = cls.create()
            functions = inspect.getmembers(instance, inspect.ismethod)
            for _, func in functions:
                if not func.__name__.endswith("Trait"):
                    continue
                func()

    def test_relationship_names_suffixed(self):
        """
        Relationship specifications should be suffixed with "Relationship"
        """
        for cls in self.__specifications():
            if RelationshipTrait.kId in cls.kTraitSet:
                assert cls.__name__.endswith("RelationshipSpecification_v1")

    def __specifications(self):
        """
        Retrieves all defined Specification classes
        """
        specs = []
        namespaces = inspect.getmembers(specifications, inspect.ismodule)
        for _, namespace in namespaces:
            classes = inspect.getmembers(namespace, inspect.isclass)
            for _, cls in classes:
                if cls.__name__.endswith("Specification_v1"):
                    specs.append(cls)
        assert specs
        return specs
