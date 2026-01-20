Release Notes
=============

v1.0.0-alpha.13
---------------

### Breaking changes

- Update the traits YAML to be compatible with the new schema defined in
  `openassetio-traitgen` v1.0.0-alpha.13+, which adds versioning to
  traits and specifications.
  [#98](https://github.com/OpenAssetIO/OpenAssetIO-MediaCreation/issues/98)

v1.0.0-alpha.12
---------------

## New features

- Added first tranche of UI-specific traits for common kinds of UI
  delegation requests.
  [OpenAssetIO#1302](https://github.com/OpenAssetIO/OpenAssetIO/issues/1302)
 
- Added better support for file and image collections by expanding
  allowed values in `LocatableContent.mimeType` and adding a new
  `ImageCollection` trait and associated specifications.
  [OpenAssetIO#1302](https://github.com/OpenAssetIO/OpenAssetIO/issues/1302)

v1.0.0-alpha.11
---------------

### Breaking changes

- Generate Trait and Specification view classes using `v1.0.0a10` of
  `openassetio-traitgen`, which reverts the use of `frozenset`s for the
  static `kTraitSet` member on Specification view classes in Python. The
  `kTraitSet` member is once again a plain `set`.
  [OpenAssetIO-TraitGen#94](https://github.com/OpenAssetIO/OpenAssetIO-TraitGen/issues/94)

v1.0.0-alpha.10
---------------

### Breaking changes

- Removed support for VFX Reference Platform CY22 or below. This means
  Python 3.7 and 3.9 builds are no longer tested or published.
  [OpenAssetIO#1351](https://github.com/OpenAssetIO/OpenAssetIO/issues/1351)

- Generate Trait and Specification view classes using `v1.0.0a10` of
  `openassetio-traitgen`, which uses `frozenset`s for the static
  `kTraitSet` member on Specification view classes in Python.
  [OpenAssetIO-TraitGen#55](https://github.com/OpenAssetIO/OpenAssetIO-TraitGen/issues/55)

v1.0.0-alpha.9
---------------

### Improvements

- Update `openassetio-traitgen` to `v1.0.0a9`, which changes exceptions
  in generated types to instead be handled via `std::optional`.
  [#74](https://github.com/OpenAssetIO/OpenAssetIO-TraitGen/issues/74)

v1.0.0-alpha.8
---------------

### New features

- Added numerous Traits and Specifications for common post-production
  workflows.
  [#22](https://github.com/OpenAssetIO/OpenAssetIO-MediaCreation/issues/22)

### Breaking changes

- Removed the `ResolvesFutureEntities` trait in favour of the [core API
  mechanism](https://github.com/OpenAssetIO/OpenAssetIO/issues/1209) for
  determining which traits can be resolved for future entities by any
  given manager.
  [#67](https://github.com/OpenAssetIO/OpenAssetIO-MediaCreation/issues/67)

### Improvements

- Pinned `openassetio-traitgen` to `v1.0.0a7` to ensure backwards
  compatibility with `openassetio` `v1.0.0a14`.
  [#60](https://github.com/OpenAssetIO/OpenAssetIO-MediaCreation/issues/60)

- Added some protection for accidental overwrites of a CMake installed
  `openassetio-mediacreation` Python package, by installing a
  `.dist-info` metadata directory alongside the package. `pip install`
  will then fail/warn against accidental overwrites/overrides. Added a
  CMake variable
  `OPENASSETIO_MEDIACREATION_ENABLE_PYTHON_INSTALL_DIST_INFO` to disable
  this feature.
  [#58](https://github.com/OpenAssetIO/OpenAssetIO-MediaCreation/issues/58)

- Added `mimeType` and `isTemplated` properties to the
  `LocatableContentTrait` to aid loading of the referenced content.
  [#22](https://github.com/OpenAssetIO/OpenAssetIO-MediaCreation/issues/22)

v1.0.0-alpha.7
--------------

### New features

- Added ability to generate python package whilst installing via cmake
  build system.
  Added cmake variables `OPENASSETIO_MEDIACREATION_GENERATE_PYTHON` and
  `OPENASSETIO_MEDIACREATION_PYTHON_SITEDIR` to support this.

- Added traits and specifications to define and query entity versioning
  information.
  [#48](https://github.com/OpenAssetIO/OpenAssetIO-MediaCreation/issues/48)

v1.0.0-alpha.6
--------------

### Breaking changes

- Removed speculative timeline traits pending real-world use cases.

### New features

- Added `openassetio_mediacreation.traits.auth.BearerTokenTrait`.

v1.0.0-alpha.5
--------------

### Improvements

- Updated `openassetio-traitgen` to `v1.0.0-alpha.6`.

### Bug fixes

- CMake will now fail at the configure stage if the
  `openassetio-traitgen` command is not available.
  [#36](https://github.com/OpenAssetIO/OpenAssetIO-MediaCreation/issues/36)

v1.0.0-alpha.4
--------------

### New features

- Add a C++ packaging process to build a cmake package from C++ traits
  generated using `openasset-traitgen`.
  [#24](https://github.com/OpenAssetIO/OpenAssetIO-MediaCreation/issues/24)

- Added the `Displayname` trait which supersedes the `entityName` and
  `entityDisplayName` methods in the core API.
  [OpenAssetIO/#837](https://github.com/OpenAssetIO/OpenAssetIO/issues/837)

v1.0.0-alpha.3
--------------

### New features

- Adds the `Managed` management policy trait, that indicates that a
  manager wishes to manage data matching the specified trait set.
  This was removed from the OpenAssetIO core API.
  [#717](https://github.com/OpenAssetIO/OpenAssetIO/issues/717)

- Adds the `ResolvesFutureEntities` management policy trait, that can be
  used to indicate that a manager is capable of resolving the specified
  trait set for entities that don't exist yet. This supersedes the old
  `WillManagePathTrait`, that was deprecated and subsequently remove
  from OpenAssetIO core API following the switch from the old 'primary
  string and attributes' approach to composed traits.
  [#717](https://github.com/OpenAssetIO/OpenAssetIO/issues/717)

### Improvements

- Added usage information to all traits.

v1.0.0-alpha.2
--------------

### Breaking changes

- Traits id's changed to `openassetio-mediacreation` namespace structure.

  - `locatableContent` -> `openassetio-mediacreation:content.LocatableContent`.
  - `timeline` -> `openassetio-mediacreation:timeline.Timeline`.
  - `track` -> `openassetio-mediacreation:timeline.Track`.
  - `clip` -> `openassetio-mediacreation:timeline.Clip`.

- Traits class paths changed to `openassetio-mediacreation` namespace
  structure.

  - `openassetio_mediacreation.trait.ClipTrait` ->
    `openassetio_mediacreation.traits.timeline.ClipTrait`.
  - `openassetio_mediacreation.trait.TimelineTrait` ->
    `openassetio_mediacreation.traits.timeline.TimelineTrait`.
  - `openassetio_mediacreation.trait.TrackTrait` ->
    `openassetio_mediacreation.traits.timeline.TrackTrait`.
  - `openassetio_mediacreation.trait.entity.LocatableContentTrait` ->
    `openassetio_mediacreation.traits.content.LocatableContentTrait`.

### Improvements

- Switched to using [openassetio-traitgen](https://github.com/OpenAssetIO/OpenAssetIO-TraitGen/)
  to generate traits. Remove hand rolled traits.
  [#10](https://github.com/OpenAssetIO/OpenAssetIO-MediaCreation/issues/10)

v1.0.0-alpha.1
--------------

### New features

- Initial release.
