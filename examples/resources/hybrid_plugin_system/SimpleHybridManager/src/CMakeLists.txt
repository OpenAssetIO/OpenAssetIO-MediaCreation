# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 The Foundry Visionmongers Ltd
cmake_minimum_required(VERSION 3.27)

project(CppComponentOfSimpleHybridManager LANGUAGES CXX)

set(_target_name ${PROJECT_NAME})

add_library(${_target_name} MODULE)

install(
    TARGETS ${_target_name}
    EXPORT ${PROJECT_NAME}_EXPORTED_TARGETS
    DESTINATION .
)

#-----------------------------------------------------------------------
# Target properties.

set_target_properties(
    ${_target_name}
    PROPERTIES

    # Ensure consistent C++17 standard.
    CXX_STANDARD 17
    CXX_STANDARD_REQUIRED YES
    CXX_EXTENSIONS NO

    # Ensure non-exported symbols are hidden from the host application.
    C_VISIBILITY_PRESET hidden
    CXX_VISIBILITY_PRESET hidden
    VISIBILITY_INLINES_HIDDEN YES

    # Use a predictable name for the plugin binary.
    OUTPUT_NAME ${PROJECT_NAME}
    PREFIX ""
    SOVERSION ""
    VERSION ""
)

#-----------------------------------------------------------------------
# Compiler warnings.

if (CMAKE_CXX_COMPILER_ID MATCHES "Clang" OR CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    set(_project_warnings -Wall -Wextra -Wpedantic)
endif ()

target_compile_options(${_target_name} PRIVATE ${_project_warnings})

#-----------------------------------------------------------------------
# API export header.

include(GenerateExportHeader)
generate_export_header(
    ${_target_name}
    EXPORT_FILE_NAME ${CMAKE_CURRENT_BINARY_DIR}/include/export.h
    EXPORT_MACRO_NAME OPENASSETIO_EXAMPLE_SIMPLEHYBRIDMANAGER_EXPORT
)

#-----------------------------------------------------------------------
# Target dependencies.

target_sources(${_target_name} PRIVATE ${PROJECT_NAME}.cpp)

# For generated API export header.
target_include_directories(${_target_name} PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/include)

find_package(OpenAssetIO REQUIRED)
target_link_libraries(${_target_name} PRIVATE OpenAssetIO::openassetio-core)
find_package(OpenAssetIO-MediaCreation REQUIRED)
target_link_libraries(${_target_name} PRIVATE OpenAssetIO-MediaCreation::openassetio-mediacreation)
