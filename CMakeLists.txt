# 1. Requirements
cmake_minimum_required(VERSION 3.21)

project(
OpenAssetIO-MediaCreation
VERSION 1.0.0
)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Additional include directories for CMake utils.
list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_LIST_DIR}/cmake)

#-----------------------------------------------------------------------
# Options
option(OPENASSETIO_MEDIACREATION_ENABLE_TEST "Run test on mediacreation traits" OFF)
option(OPENASSETIO_MEDIACREATION_GENERATE_PYTHON "Aditionally generate python library" OFF)
if (OPENASSETIO_MEDIACREATION_GENERATE_PYTHON)
    # By default we'll compute the correct site-packages directory
    # structure, but allow overriding.
    set(OPENASSETIO_MEDIACREATION_PYTHON_SITEDIR
        ""
        CACHE STRING
        "Override default Python module install directory, relative to CMAKE_INSTALL_PREFIX")
endif ()

message(STATUS "Test enabled = ${OPENASSETIO_MEDIACREATION_ENABLE_TEST}")
message(STATUS "Generate python library = ${OPENASSETIO_MEDIACREATION_GENERATE_PYTHON}")

# ABI wrangling only needed for test
if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU" AND
    CMAKE_CXX_COMPILER_VERSION VERSION_GREATER_EQUAL 5.0)
    option(OPENASSETIO_MEDIACREATION_GLIBCXX_USE_CXX11_ABI "For gcc, use the new C++11 library ABI"
           OFF)
    message(STATUS "New C++11 ABI for GCC = ${OPENASSETIO_MEDIACREATION_GLIBCXX_USE_CXX11_ABI}")
endif ()

#-----------------------------------------------------------------------
# Default install directory

# Default install to a `dist` directory under the build directory, ready
# for use in tests and for packaging. But don't override if user has
# explicitly set CMAKE_INSTALL_PREFIX.
if (CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT AND PROJECT_IS_TOP_LEVEL)
    set(CMAKE_INSTALL_PREFIX "${PROJECT_BINARY_DIR}/dist" CACHE PATH "Installation location" FORCE)
endif ()

#-----------------------------------------------------------------------
# OpenAssetIO-MediaCreation generates its traits at configure time, via
# calling `openassetio-traitgen`.
# Some might be surprised by this, and expect code generation to be
# performed in a build step. However, with MediaCreation being a
# header only library, there is no "build-step" as such, (unless added
# coincidently, if you are building the test executable, for example.)
#
# There are alternate ways to have the generation be done in the build
# step which we explored.
# - Add a custom target with the `ALL` depencency, which forces in a
#   build step, however, this has the downside of causing a regeneration
#   on every build
# - Define the library as a PUBLIC rather than INTERFACE library.
#   This however has the downside of needing to provide the sources up
#   front, meaning one needs to know the output of the generator.
#
# Furthermore, generating sources at configure time serves to more
# directly mimic a non-generated project, and lowers risk that changes
# to the library structure later on will encounter issues caused by the
# generative nature of the project.
message("Generating Traits with openassetio-traitgen")
# Mark the traits source as a configure dependency by copying it to the
# binary dir, and use that file to run traitgen from.
# This means if the source traits file is changed, configure will rerun.
configure_file(${CMAKE_CURRENT_LIST_DIR}/traits.yml ${PROJECT_BINARY_DIR}/traits.yml)
execute_process(COMMAND openassetio-traitgen ${PROJECT_BINARY_DIR}/traits.yml
                    -o ${PROJECT_BINARY_DIR}/cpp -g cpp
                    COMMAND_ERROR_IS_FATAL ANY
                    COMMAND_ECHO STDERR)

if (OPENASSETIO_MEDIACREATION_GENERATE_PYTHON)
    # Generate the python package by running traitgen.
    # By running traitgen during the cmake step, using the traitgen that
    # is available to the environment, just as the C++ generation does,
    # we guarentee that the versions of traitgen used between c++ and
    # python packages are identical. This isn't a guarentee when using
    # the `pip install .` method of creating a python package, due to
    # pip having a seperate dependency resolution method.
    #
    # At the time of writing, this produces the same artifact as doing
    # `pip install .` (and invoking setup.py), but that's not a
    # guarentee going forward, as additional elements of the python
    # package may be added to mediacreation.
    execute_process(COMMAND openassetio-traitgen ${PROJECT_BINARY_DIR}/traits.yml
        -o ${PROJECT_BINARY_DIR}/python -g python
        COMMAND_ERROR_IS_FATAL ANY
        COMMAND_ECHO STDERR)
endif()

add_library(openassetio-mediacreation INTERFACE)
# add alias so the project can be used with add_subdirectory
add_library(OpenAssetIO-MediaCreation::openassetio-mediacreation ALIAS openassetio-mediacreation)

include(GNUInstallDirs)

# traitgen generates to _public_header_source_root/cpp location by default.
set(_public_header_source_root "${PROJECT_BINARY_DIR}/cpp/openassetio_mediacreation/include")
set(_config_install_dir "${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}")
set(_project_config_file "${PROJECT_BINARY_DIR}/cpp/${PROJECT_NAME}Config.cmake")
set(_version_config_file "${PROJECT_BINARY_DIR}/cpp/${PROJECT_NAME}ConfigVersion.cmake")
set(_traitgen_data_dir "${CMAKE_INSTALL_DATADIR}/openassetio-traitgen")

#-----------------------------------------------------------------------
# Include directories
target_include_directories(openassetio-mediacreation
    INTERFACE
    # Use includes from source tree for building.
    "$<BUILD_INTERFACE:${_public_header_source_root}>"
    # Use includes from install tree for installed lib.
    "$<INSTALL_INTERFACE:include>")

target_compile_features(openassetio-mediacreation INTERFACE cxx_std_17)

#-----------------------------------------------------------------------
# Package config (Create the Config/Targets .cmake files)
install (TARGETS openassetio-mediacreation
         EXPORT ${PROJECT_NAME}_EXPORTED_TARGETS)

include(CMakePackageConfigHelpers)
write_basic_package_version_file(${_version_config_file}
                                VERSION ${PROJECT_VERSION}
                                COMPATIBILITY SameMajorVersion)

configure_package_config_file(
    cmake/Config.cmake.in
    ${_project_config_file}
    INSTALL_DESTINATION ${_config_install_dir}
)

install(
    EXPORT ${PROJECT_NAME}_EXPORTED_TARGETS
    DESTINATION ${_config_install_dir}
    NAMESPACE ${PROJECT_NAME}::
    FILE ${PROJECT_NAME}Targets.cmake
)

#-----------------------------------------------------------------------
# Optionally install python library
if (OPENASSETIO_MEDIACREATION_GENERATE_PYTHON)
    include(ThirdParty)

    install(
        DIRECTORY ${PROJECT_BINARY_DIR}/python/openassetio_mediacreation
        DESTINATION "${OPENASSETIO_MEDIACREATION_PYTHON_SITEDIR}"
        FILES_MATCHING PATTERN "*.py"
    )
endif()

#-----------------------------------------------------------------------
# Copy CMake Files
install(
    FILES ${_project_config_file} ${_version_config_file}
    DESTINATION ${_config_install_dir}
)

#-----------------------------------------------------------------------
# Copy traitgen headers to install dir
install(DIRECTORY ${_public_header_source_root} DESTINATION .)

install(
    FILES "${PROJECT_BINARY_DIR}/traits.yml"
    DESTINATION ${_traitgen_data_dir}
    RENAME "openassetio-mediacreation.yml"
)

#-----------------------------------------------------------------------
# C++ tests.
if (OPENASSETIO_MEDIACREATION_ENABLE_TEST)
    add_subdirectory(tests/cpp)
endif ()
