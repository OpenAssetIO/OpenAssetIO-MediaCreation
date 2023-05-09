Release Notes
=============

v1.0.0-alpha.x
--------------

### Improvements

- Updated `openassetio-traitgen` to `v1.0.0-alpha.6`.

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

### New Features

- Initial release.
