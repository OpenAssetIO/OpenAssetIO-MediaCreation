# DR002 Versioning Traits and Specification - generated view classes

- **Status:** Decided
- **Impact:** High
- **Driver:** @feltech
- **Approver:** @elliotcmorris @themissingcow
- **Outcome:** Traits and specifications will be versioned independent
  of the schema, there will be no concept of a schema version, and
  Trait/Specification view classes will be generated with version
  suffixes on the class name.

## Background

The medium of data exchange between a host and a manager is a logically
opaque data blob, i.e. a `TraitsData` object. In order to add/extract
information to/from this object, Trait and/or Specification view classes
must be used[^1]. These classes wrap a `TraitsData` instance, and
provide a suite of accessor and mutator methods that are relevant to the
target trait. The classes are generated from a YAML schema (e.g. see
[traits.yml](../traits.yml)).

Hosts and managers may use different versions of the schema, and hence
different versions of the view classes, and yet still wish to work
together.

This decision record follows on from a previous decision (OpenAssetIO
[DR023](https://github.com/OpenAssetIO/OpenAssetIO/blob/main/doc/decisions/DR023-Versioning-traits-and-specifications-method.md))
that communicating a trait's version should be done by bundling the
version number with the data blob that is communicated across the API,
i.e. within `TraitsData`, most likely by appending the version number to
the unique trait ID.

With this previous decision in mind, we then need to decide on how the
trait versions are represented in the high level interface, i.e. in
the definition and usage of Trait/Specification view classes.

A motivating example should make this problem clear.

[^1]: In reality, a `TraitsData` is a simple dictionary-like structure,
and the `TraitsData` type has a low-level interface for interacting with
it, but usage of this is discouraged.

### Motivating example

An example usage of the current form of these generated classes might
be:

```python
url = LocatableContentTrait(trait_data).getLocation()
```

Imagine that we want to rename the LocatableContent trait's `"location"`
property to a more descriptive `"url"` property, hence changing the
generated view class's method from `getLocation` to `getUrl`.

Given that hosts and managers are developed independently, we may end up
with a situation where one side is setting `"location"` (using
`setLocation`) in the data, handing it over to the other side, who then
attempts to read `"url"` (using `getUrl`). I.e. we have a version
mismatch.

There is therefore an incompatibility at the data layer (i.e. field
names differ for the same semantic information). With C++, the data
layer is where the incompatibility ends. The Trait/Specification view
classes are private utility classes whose symbols should not be
exported, so there will be no source or binary incompatibility.

However, with Python there is no such concept of a private, build-time
only, class. The manager plugin and host application must use the same
`openassetio-mediacreation` distribution package in the Python
environment (not considering, for the moment, custom vendoring). So one
side or the other will hit an `AttributeError` exception when trying to
use a method from the version they developed against, rather than the
version installed into the environment.

In order to interoperate, previous versions of Trait/Specification view
classes must be made available, so that fallback behaviour can be coded.
In this example, the side that attempts to use the newer `getUrl` to
read the data must be able to detect that it won't work and fall back to
the previous version's `getLocation`.

### Assumptions

* A Trait/Specification view class is needed for each version, such
  that a user can imbue a particular version of a trait in some data;
  and can detect that a particular version of a trait is imbued in some
  data.
* Trait unique IDs will be suffixed with a version number. This means
  two Trait view classes for the same trait, but for different versions,
  will be treated as if they are entirely separate traits.
  Version-agnostic utility functions may be added in the future, but it
  is out of scope for now.
* If a Specification view class is used to construct/imbue a trait
  set/data, that data will _not_ have the Specification version encoded
  in the data directly (only implicitly through the versioned IDs of the
  composite traits).

## Relevant data

[OpenTimelineIO schema
versioning](https://opentimelineio.readthedocs.io/en/latest/tutorials/otio-file-format-specification.html#example)
is perhaps the closest analog. The version of the schema is appended to
the schema ID whenever it appears within a OTIO JSON document.

The options presented were arrived at by sketching a proposal in [a Pull
Request](https://github.com/OpenAssetIO/OpenAssetIO-MediaCreation/pull/90),
soliciting feedback, and iterating. The final form of that PR reflects
the chosen option.

## Options considered

### Option 1 - Per schema versioning

When traits or specifications in the YAML document are updated, a
top-level schema version is incremented. During codegen, top-level
namespaces are created by providing multiple YAML documents, one for
each schema version.

For example

```python
from openassetio_mediacreation.v1.traits.content import LocatableContent as LocatableContent_v1
from openassetio_mediacreation.v2.traits.content import LocatableContent as LocatableContent_v2
from openassetio_mediacreation.v2.specifications.twoDimensional import ImageSpecification
```

#### Pros

- Tantalising possibility to use [Python namespace
  packages](https://packaging.python.org/en/latest/guides/packaging-namespace-packages)
  to allow different schema versions to be installed independently
  side-by-side.
- The schema version a specification comes from instantly tells you the
  schema version of the constituent traits.
- The YAML is kept small and focussed just on the latest versions.
- Minimal changes to the `traitgen` tool and existing YAML documents.
- Maintaining only the latest versions in the live YAML document
  prevents accidental changes to old versions that could break backward
  compatibility.
- The consuming build system is in charge of deciding which schema
  versions are available for code to use at build/run time.
  I.e. a host/manager only need generate the subpackages they support.
- Once it is clear that a host/manager understands a particular schema
  version (via `managementPolicy` or otherwise), the communicating
  manager/host can be confident in using that schema version for other
  traits/specifications.

#### Cons

- A source-incompatible breaking change, unless significant
  special-casing is added.
- Verbose when using two versions in the same source file, either
  requiring use of qualified names (e.g. `v1.traits.LocatableContent`)
  or additional aliasing (e.g. 
 `from ... import LocatableContent as LocatableContent_v1`).
- Not clear at-a-glance which traits have changed between schema
  versions, e.g. it's not clear if
  `v2.traits.content.LocatableContentTrait` is the same as
  `v1.traits.content.LocatableContentTrait`.
- Must compare multiple YAML documents side-by-side in order to discover
  the history of changes to a particular trait/specification.
- Traits/specifications that are unchanged between versions implies
  duplicated code across namespaces (though likely simply aliased).
- Independently generated/installed subpackages for each schema version
  would mean that deprecation warnings could not be added to old
  versions. This is mitigated if multiple versions are generated
  together, where the older version can be detected and deprecation
  warnings added by codegen.

### Option 2 - Per Trait/Specification versioning

A single YAML document is maintained, where each trait/specification
definition branches off into a list of versions. Old
trait/specification versions can be marked as deprecated and removed
eventually, to prevent infinite growth.

For example

```python
from openassetio_mediacreation.traits.content import LocatableContent_v1
from openassetio_mediacreation.traits.content import LocatableContent_v2
from openassetio_mediacreation.specifications.twoDimensional import ImageSpecification_v2
```

#### Pros

- Fairly trivial to say that the first version "`_v1`" is equivalent to
  "" (blank), and to ensure that v1's trait ID doesn't contain a version
  tag, then e.g. the `LocatableContent` class continues to work as
  before versioning was introduced, making this option fully source
  compatible with legacy code. I.e. not a breaking change.
- Placing versions alongside one-another in the YAML definition allows
  easy discovery of the history of changes.
- IDE code completion will list all versions of a Trait/Specification
  view class next to one-another.
- More natural for hosts and managers to do targeted compatibility
  around specific traits.

#### Cons

- No indication of the version of the constituent traits from the
  version of a Specification view class.
- Large change to `traitgen` tool and non-trivial breaking change to
  YAML documents.
- Keeping old versions in a living document (as opposed to e.g. git
  history) is a potential source of accidental breakages to backward
  compatibility.
- Generating all possible versions bloats an application's distribution,
  when it may only use a small subset of them. Configuring which
  versions to generate would mean maintaining a long list of options,
  one per trait.
- Higher level branching on a schema version is never possible.
- A specification's version must be bumped when a constituent trait has
  a version bump, even if nothing else in the specification has changed.
  Conceptually, specifications are trait version agnostic, but must
  become version-aware for the purposes of codegen, which is
  inconsistent.

## Outcome

We will implement Option 2 - Per Trait/Specification versioning. 

A huge benefit is how much easier it is to make this solution a
non-breaking change to current users.

In addition, it has better discoverability through IDE code completion,
and it is easier to view history through a single YAML document rather
than across several documents.

There will be a rather large change to the `traitgen` tool and the YAML
JSON schema, causing a headache for any early adopters who are
generating their own traits. However, this is less critical than changes
to the generated output in use within pipelines.