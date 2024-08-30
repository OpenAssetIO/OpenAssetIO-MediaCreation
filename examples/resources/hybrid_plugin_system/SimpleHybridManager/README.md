# Simple Hybrid Manager

This directory contains a very simple OpenAssetIO hybrid C++/Python
manager plugin. It is used in the _Hybrid Plugin System_ Jupyter 
notebook.

## C++ component 

The C++ component of the plugin is provided as sources under the `src`
directory, and so must be built before it can be used.

It has OpenAssetIO and OpenAssetIO-MediaCreation as CMake dependencies,
so these projects need to be built and installed somewhere discoverable
by CMake.

For the Jupyter Notebook to run, the resulting `.so`/`.dll` must be
placed in the `plugin` directory. This can be done using `cmake
--install` and setting `--install-prefix`/`--prefix` to the `plugin`
directory; or by simply copying the file from the build directory.