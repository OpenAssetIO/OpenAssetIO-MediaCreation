# OpenAssetIO-MediaCreation

A library of OpenAssetIO extensions for use in Media Creation workflows.

> Note: This repository is currently in a pre-alpha state, and so should
> not be used for any production critical applications.

Included are several well-known Traits and Specifications for use in
OpenAssetIO hosts and managers. For more information on this mechanism,
see the [OpenAssetIO docs](https://openassetio.github.io/OpenAssetIO).

MediaCreation is an automatically generated Python package,
[openassetio-traitgen](https://github.com/OpenAssetIO/OpenAssetIO-TraitGen)
is used to generate trait implementations based on [traits.yml](traits.yml)

## Examples

Code samples of how the Media Creation Traits and Specifications can be
used in production workflows are available in the [examples](./examples)
directory in form of [Jupyter](https://jupyter.org) notebooks.

When [viewed in GitHub](https://github.com/OpenAssetIO/OpenAssetIO-MediaCreation/tree/main/examples)
they will be fully rendered. They can also be explored locally:

```bash
git clone https://github.com/OpenAssetIO/OpenAssetIO-MediaCreation.git
cd OpenAssetIO-MediaCreation
python -m venv .venv
. ./.venv/bin/activate
python -m pip install .
python -m pip install -r examples/resources/requirements.txt
cd examples
jupyter notebook
```

## Project status

These initial incarnations of traits/specifications serve as
illustrative examples to facilitate discussion and experimentation.
Pending tasks:

- [x] Define YAML schema to represent traits/specifications.
- [x] Auto-generate Python classes from YAML
- [x] Auto-generate CPP classes from YAML
- [ ] Auto-generate C classes from YAML.
- [ ] Extend library to cover common post-production entities and
      locales.

## Installation

### Python

```shell
python -m pip install openassetio-mediacreation
```

### C++

> **Note**
>
> During the configure process, `openassetio-traitgen` will be used to
> generate C++ trait files. This is assumed to be available in your
> environment. You may install it via `python -m pip install
> openassetio-traitgen`

```shell
cmake -S . -B build
cmake --build build
cmake --install build
```

A cmake package will be created under a `dist` directory in your
`build` directory.

## Running the tests

### Python

To run the tests, on a local development checkout, you can install
the package with pip, then run `pytest`.

Note, editable installs are not supported as the package is entirely
auto-generated from the traits YAML.

```shell
python -m pip install .
python -m pip install pytest
pytest
```

### C++

> **Note**
>
> Building with tests introduces a build-time dependency on
> [OpenAssetIO](https://github.com/OpenAssetIO/OpenAssetIO), which must
> be discoverable via
> [cmake.](https://cmake.org/cmake/help/v3.21/command/find_package.html)

The C++ tests are enabled via setting a cmake variable in the configure:

```shell
cmake -S . -B build -DOPENASSETIO_MEDIACREATION_ENABLE_TEST=ON
cmake --build build
ctest --test-dir build/tests/cpp
```

## Contributing

This repository follows the [contribution guidelines](https://github.com/TheFoundryVisionmongers/OpenAssetIO/blob/main/contributing/PROCESS.md)
outlined in the main OpenAssetIO repository. All discussion most
welcome!

When adding new Traits and Specifications:

1. Update [traits.yml](traits.yml)
2. Add an [import test](tests/python/openassetio_mediacreation/test_imports.py)
3. Update the [RELEASE_NOTES](RELEASE_NOTES.md)
