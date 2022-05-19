# OpenAssetIO-MediaCreation

OpenAssetIO extensions for use in Media Creation

> Note: This repository is currently in a pre-alpha state, and so should
> not be used for any production critical applications.

Included are several well-known Traits and Specifications for use in
OpenAssetIO hosts and managers. For more information on this mechanism,
see the [OpenAssetIO docs](https://thefoundryvisionmongers.github.io/OpenAssetIO/).

## Project status

These initial incarnations of traits/specifications serve as
illustrative examples to facilitate discussion and experimentation.
Pending tasks:

- [ ] Define JSON schema to represent traits/specifications.
- [ ] Auto-generate Python, CPP and C classes from JSON.
- [ ] Extend library to cover common post-production entities and
      locales.

## Installation

Presently, this is somewhat manual, and requires your own build of
`openassetio` `v1.0.0-alpha.1` to be available in your python
environment.

```shell
git clone https://github.com/OpenAssetIO/OpenAssetIO-MediaCreation
cd OpenAssetIO-MediaCreation
pip install .
```

## Running the tests

Assuming `openassetio` and `openassetio_mediacreation` packages are available in
your python environment:

```shell
pytest
```

## Contributing

This repository follows the [contribution guidelines](https://github.com/TheFoundryVisionmongers/OpenAssetIO/blob/main/contributing/PROCESS.md)
outlined in the main OpenAssetIO repository. All discussion most
welcome!
