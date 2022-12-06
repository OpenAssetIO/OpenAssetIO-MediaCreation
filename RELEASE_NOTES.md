Release Notes
=============

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
