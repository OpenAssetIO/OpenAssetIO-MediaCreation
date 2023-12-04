# Guidelines

This document covers general best-practices when authoring Traits and/or
Specifications for inclusion in the library.

## Traits

Traits define unique qualities or characteristics of an Entity or
Relationship.

- Traits must be atomic. No single trait should ever change the
  meaning of another trait _or its properties_. This ensures that future
  traits not known at the time code is written can't change the meaning
  of previously defined values.

- Traits should contain the minimum number of properties required to
  define a particular characteristic. They must document in their
  description if properties are optional. Non-optional properties are
  required to be populated by a host during publishing, and during
  resolve by a supporting manager.

- In order to facilitate identification, traits must define a single
  characteristic. Consider splitting 'optional' properties into a
  separate trait. For example the bounding box of a 3D object would be
  best expressed through the `BoundingBox` trait, rather than an
  optional `boundingBox` property of the `Spatial` trait.

- Traits should _not_ use properties to differentiate between different
  exhibited characteristics. Individual traits should be created for
  each one. Properties are then used to describe specific details of
  that quality. For example, instead of an `Animated` trait with a
  boolean `isAnimated` property, we have `Static` and `FrameRanged`
  traits. This ensures the _set of trait ids_ is sufficient to identify
  the qualities of an entity, and that the properties of these traits
  are then appropriate to each. Illustrated by the `startFrame` and
  `endFrame` of the `FrameRanged` trait - a future `TimeRanged` trait
  would naturally require different parameterisation.

- Effort should me made to ensure a minimal overlap between trait names.
  The namespace and package name can be leveraged in order to reduce
  ambiguity if necessary, avoiding the need to be truly unique within
  the ecosystem in all cases.

- Trait property names should describe the nature of the value as
  precisely as possible. They shouldn't require the user to consult the
  documentation. For example:
  - Good: `framesPerSecond`, `metersPerLinearUnit`
  - Bad: `frameRate`, `units`

- "Family" traits can be defined where applicable to allow high-level
  partitioning of entity space. For example the `Image` and `Spatial`
  traits exist solely to allow users to broadly filter 2D and 3D
  entities without needing multiple top-level trait sets. Care should be
  taken when defining properties for these traits, to ensure they are
  genuinely applicable to all entities with the quality in question. Eg.
  `Spatial` does not include a bounding box as there are many unbounded
  or zero-volume concepts in the 3D world, this should be expressed
  through a peer trait in the `threeDimensional` namespace that can be
  composed as needed.

- The absence of a trait _does not_ imply its inverse, and so companion
  traits may be needed to define antonyms or other mutually exclusive
  qualities

## Specifications

Specifications define well-known collections of traits that map to
first-class concepts within our workflows. They are used to create a
common definition of the nature of entities ("assets") and relationships
between them. The collection of traits is known formally within the
OpenAssetIO ecosystem as a "trait set".

- Specifications must contain the minimum number of traits required to
  define a particular concrete workflow entity. Trait sets are
  [additive](https://openassetio.github.io/OpenAssetIO/entities_traits_and_specifications.html#Specifications),
  and so each trait stipulates that the entity _must_ possess that
  quality, _in addition to_ the qualities of all the other traits in the
  set. There is no way to define a specification that states "one trait
  or the other".

- Effort should me made to ensure a minimal overlap between
  specification names. The namespace and package name can be leveraged
  in order to reduce ambiguity if necessary, avoiding the need to be
  truly unique within the ecosystem in all cases.

- Specifications that define a relationship should append `Relationship`
  to their names to help with cognition.

- "Family" specifications can be defined to allow high-level
  partitioning of entity space. For example the `Image` and `Spatial`
  specifications exist solely to allow users to broadly filter 2D and 3D
  entities without needing multiple top-level specifications. Care should be
  taken to ensure that their trait sets are not overly constrained to
  preclude future evolution. These specifications do not include the
  `LocatableContent` trait to ensure we can support inline Image or
  Spatial data (eg. a procedural checkerboard pattern), even though at
  the time of going to press, known workflows only used independent
  resource data.

- Specifications should form well-known base trait sets. They do not
  necessarily need to be exhaustively defined for all specialisations.
  Taking images as an example, we define bases for core variations of
  how they are encoded in our problem space (`PlanarBitmapImage`,
  `DeepBitmapImage`, etc). We do not define an exhaustive set of
  additional specifications for the matrix of images that are some
  combination of  `Static`, `FrameRanged`, `OCIOColorManaged`. Users are
  encouraged to compose or resolve other meaningful traits with the
  well-known specifications as appropriate. Formally defining these
  "well-known combinations" in a non-limiting way is something to be
  investigated.

- All specifications must contain a single trait from the `usage`
  namespace to define their meaning when encountered at runtime.

- Care should be taken when composing traits to ensure
  that there is a specific trait present that defines each required
  quality, rather than relying on the omission of a contrary quality.
  The absence of a trait within a specification's trait set only means the
  set does not specify whether it exhibits that quality or not. This
  allows trait sets to be used as filter predicates:
  - `{ Entity, Image }`: All images (static, animated or any other).
  - `{ Entity, Image, Static }`: Only static images without animation.
  - `{ Entity, Image, FrameRanged }`: Only animated images that cover a
	discrete series of frames.

- Hosts and managers are encouraged to _extend_ well-known
  specifications with their own proprietary traits to sufficiently to
  differentiate from other entities. A common pattern for
  application-specific "documents" is to define a trait named after the
  application (eg.`Blender`) and compose this with existing Media
  Creation `Workfile` specification. This facilitates more generic
  handling via the well-known trait set, but achieve suitable filtering
  if needed when only the app-specific variant is required.

- **Hosts and managers are _strongly discouraged_ from only using
  proprietary traits in their specifications as it defeats
  interoperability.** Using custom traits require explicit support in
  every host _and_ manager, which limits compatibility between systems.
