# OpenAssetIO-MediaCreation

OpenAssetIO extensions for use in Media Creation

> Note: This repository is currently in a pre-alpha state, and so should
> not be used for any production critical applications.

Included are several well-known Traits and Specifications for use in
OpenAssetIO hosts and managers. For more information on this mechanism,
see the [OpenAssetIO docs](https://thefoundryvisionmongers.github.io/OpenAssetIO/).

MediaCreation is a fully generated component,
[openassetio-traitgen](https://github.com/OpenAssetIO/OpenAssetIO-TraitGen)
is used to generate trait implementations based on [traits.yml](traits.yml)

## Project status

These initial incarnations of traits/specifications serve as
illustrative examples to facilitate discussion and experimentation.
Pending tasks:

- [x] Define YAML schema to represent traits/specifications.
- [x] Auto-generate Python classes from YAML
- [ ] Auto-generate CPP and C classes from YAML.
- [ ] Extend library to cover common post-production entities and
      locales.

## Installation

```shell
pip install openassetio-mediacreation
```

During installation, [openassetio-traitgen](https://github.com/OpenAssetIO/OpenAssetIO-TraitGen)
will be used to generate trait implementations based on [traits.yml](traits.yml)

## Running the tests

To run the tests, after installing, simply run

```shell
pytest
```

## Contributing

This repository follows the [contribution guidelines](https://github.com/TheFoundryVisionmongers/OpenAssetIO/blob/main/contributing/PROCESS.md)
outlined in the main OpenAssetIO repository. All discussion most
welcome!
