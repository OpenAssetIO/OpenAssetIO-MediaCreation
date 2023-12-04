# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 The Foundry Visionmongers Ltd
"""
Test MediaCreation traits and specifications can be imported
"""

# pylint: disable=no-self-use
# pylint: disable=invalid-name
# pylint: disable=unused-import,import-outside-toplevel
# pylint: disable=missing-class-docstring,missing-function-docstring

import pytest


@pytest.fixture(autouse=True)
def always_unload_openassetio_mediacreation_modules(
    unload_openassetio_mediacreation_modules,  # pylint: disable=unused-argument
):
    """
    Removes openassetio modules from the sys.modules cache that
    otherwise mask cyclic dependencies.
    """


class Test_package_imports:
    def test_importing_openassetio_mediacreation_succeeds(self):
        import openassetio_mediacreation

    def test_importing_traits_succeeds(self):
        from openassetio_mediacreation import traits

    def test_importing_specifications_succeeds(self):
        from openassetio_mediacreation import specifications


class Test_trait_imports_content:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import content

    def test_importing_LocatableContentTrait_succeeds(self):
        from openassetio_mediacreation.traits.content import LocatableContentTrait


class Test_trait_imports_managementPolicy:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import managementPolicy

    def test_importing_ManagedTrait_succeeds(self):
        from openassetio_mediacreation.traits.managementPolicy import ManagedTrait


class Test_trait_imports_identity:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import identity

    def test_importing_DisplayNameTrait_succeeds(self):
        from openassetio_mediacreation.traits.identity import DisplayNameTrait


class Test_trait_imports_auth:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import auth

    def test_importing_BearerToken_succeeds(self):
        from openassetio_mediacreation.traits.auth import BearerTokenTrait


class Test_trait_imports_application:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import application

    def test_importing_Config_succeeds(self):
        from openassetio_mediacreation.traits.application import ConfigTrait

    def test_importing_Manifest_succeeds(self):
        from openassetio_mediacreation.traits.application import ManifestTrait

    def test_importing_Work_succeeds(self):
        from openassetio_mediacreation.traits.application import WorkTrait


class Test_trait_imports_usage:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import usage

    def test_importing_Entity_succeeds(self):
        from openassetio_mediacreation.traits.usage import EntityTrait

    def test_importing_Relationship_succeeds(self):
        from openassetio_mediacreation.traits.usage import RelationshipTrait


class Test_trait_imports_lifecycle:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import lifecycle

    def test_importing_Version_succeeds(self):
        from openassetio_mediacreation.traits.lifecycle import VersionTrait

    def test_importing_Stable_succeeds(self):
        from openassetio_mediacreation.traits.lifecycle import StableTrait


class Test_trait_imports_relationship:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import relationship

    def test_importing_Singular_succeeds(self):
        from openassetio_mediacreation.traits.relationship import SingularTrait

    def test_importing_Unbounded_succeeds(self):
        from openassetio_mediacreation.traits.relationship import UnboundedTrait


class Test_trait_imports_representation:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import representation

    def test_importing_Proxy_succeeds(self):
        from openassetio_mediacreation.traits.representation import ProxyTrait

    def test_importing_Original_succeeds(self):
        from openassetio_mediacreation.traits.representation import OriginalTrait


class Test_trait_imports_timeDomain:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import timeDomain

    def test_importing_FrameRanged_succeeds(self):
        from openassetio_mediacreation.traits.timeDomain import FrameRangedTrait

    def test_importing_Static_succeeds(self):
        from openassetio_mediacreation.traits.timeDomain import StaticTrait


class Test_trait_imports_twoDimensional:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import twoDimensional

    def test_importing_Image_succeeds(self):
        from openassetio_mediacreation.traits.twoDimensional import ImageTrait

    def test_importing_PixelBased_succeeds(self):
        from openassetio_mediacreation.traits.twoDimensional import PixelBasedTrait

    def test_importing_Deep_succeeds(self):
        from openassetio_mediacreation.traits.twoDimensional import DeepTrait


class Test_trait_imports_threeDimensional:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import threeDimensional

    def test_importing_Spatial_succeeds(self):
        from openassetio_mediacreation.traits.threeDimensional import SpatialTrait

    def test_importing_GeometryTrait_succeeds(self):
        from openassetio_mediacreation.traits.threeDimensional import GeometryTrait

    def test_importing_Lighting_succeeds(self):
        from openassetio_mediacreation.traits.threeDimensional import LightingTrait

    def test_importing_Shader_succeeds(self):
        from openassetio_mediacreation.traits.threeDimensional import ShaderTrait

    def test_importing_IESProfile_succeeds(self):
        from openassetio_mediacreation.traits.threeDimensional import IESProfileTrait

    def test_importing_SourcePath_succeeds(self):
        from openassetio_mediacreation.traits.threeDimensional import SourcePathTrait

    def test_importing_SourcePaths_succeeds(self):
        from openassetio_mediacreation.traits.threeDimensional import SourcePathsTrait


class Test_trait_imports_metadata:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import metadata

    def test_importing_Camera_succeeds(self):
        from openassetio_mediacreation.traits.metadata import ArbitraryMetadataTrait


class Test_trait_imports_imaging:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import imaging

    def test_importing_Camera_succeeds(self):
        from openassetio_mediacreation.traits.imaging import CameraTrait


class Test_trait_imports_color:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import color

    def test_importing_Camera_succeeds(self):
        from openassetio_mediacreation.traits.color import OCIOColorManagedTrait


class Test_trait_imports_audio:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.traits import audio

    def test_importing_Audio_succeeds(self):
        from openassetio_mediacreation.traits.audio import AudioTrait

    def test_importing_SampleBased_succeeds(self):
        from openassetio_mediacreation.traits.audio import SampleBasedTrait


class Test_specification_imports_lifecycle:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.specifications import lifecycle

    def test_importing_EntityVersionsRelationship_succeeds(self):
        from openassetio_mediacreation.specifications.lifecycle import (
            EntityVersionsRelationshipSpecification,
        )

    def test_importing_StableEntityVersionsRelationship_succeeds(self):
        from openassetio_mediacreation.specifications.lifecycle import (
            StableEntityVersionsRelationshipSpecification,
        )

    def test_importing_StableReferenceRelationship_succeeds(self):
        from openassetio_mediacreation.specifications.lifecycle import (
            StableReferenceRelationshipSpecification,
        )


class Test_specification_imports_representation:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.specifications import representation

    def test_importing_OriginalRepresentationRelationship_succeeds(self):
        from openassetio_mediacreation.specifications.representation import (
            OriginalRepresentationRelationshipSpecification,
        )

    def test_importing_ProxyRepresentationRelationship_succeeds(self):
        from openassetio_mediacreation.specifications.representation import (
            ProxyRepresentationRelationshipSpecification,
        )


class Test_specification_imports_twoDimenstional:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.specifications import twoDimensional

    def test_importing_Image_succeeds(self):
        from openassetio_mediacreation.specifications.twoDimensional import ImageSpecification

    def test_importing_BitmapImageResource_succeeds(self):
        from openassetio_mediacreation.specifications.twoDimensional import (
            BitmapImageResourceSpecification,
        )

    def test_importing_DeepBitmapImageResource_succeeds(self):
        from openassetio_mediacreation.specifications.twoDimensional import (
            DeepBitmapImageResourceSpecification,
        )


class Test_specification_imports_threeDimenstional:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.specifications import threeDimensional

    def test_importing_Spatial_succeeds(self):
        from openassetio_mediacreation.specifications.threeDimensional import SpatialSpecification

    def test_importing_SceneResource_succeeds(self):
        from openassetio_mediacreation.specifications.threeDimensional import (
            SceneResourceSpecification,
        )

    def test_importing_SceneGeometryResource_succeeds(self):
        from openassetio_mediacreation.specifications.threeDimensional import (
            SceneGeometryResourceSpecification,
        )

    def test_importing_SceneCameraResource_succeeds(self):
        from openassetio_mediacreation.specifications.threeDimensional import (
            SceneCameraResourceSpecification,
        )

    def test_importing_SceneLightingResource_succeeds(self):
        from openassetio_mediacreation.specifications.threeDimensional import (
            SceneLightingResourceSpecification,
        )

    def test_importing_ShaderResource_succeeds(self):
        from openassetio_mediacreation.specifications.threeDimensional import (
            ShaderResourceSpecification,
        )

    def test_importing_IESProfileResource_succeeds(self):
        from openassetio_mediacreation.specifications.threeDimensional import (
            IESProfileResourceSpecification,
        )


class Test_specification_imports_audio:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.specifications import audio

    def test_importing_Audio_succeeds(self):
        from openassetio_mediacreation.specifications.audio import AudioSpecification

    def test_importing_SampledAudioResource_succeeds(self):
        from openassetio_mediacreation.specifications.audio import (
            SampledAudioResourceSpecification,
        )


class Test_specification_imports_application:
    def test_importing_namespace_succeeds(self):
        from openassetio_mediacreation.specifications import application

    def test_importing_workfile_succeeds(self):
        from openassetio_mediacreation.specifications.application import WorkfileSpecification
