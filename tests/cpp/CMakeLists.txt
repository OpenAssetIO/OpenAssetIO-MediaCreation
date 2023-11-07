# OpenAssetIO Dependency.
find_package(OpenAssetIO REQUIRED)
enable_testing()

add_executable(test.cpp test.cpp)
add_test(cpp test.cpp)

# GCC's C++11 ABI toggle must match OpenAssetIO's settings.
if (DEFINED OPENASSETIO_MEDIACREATION_GLIBCXX_USE_CXX11_ABI)
    if (OPENASSETIO_MEDIACREATION_GLIBCXX_USE_CXX11_ABI)
        target_compile_definitions(test.cpp PRIVATE _GLIBCXX_USE_CXX11_ABI=1)
    else ()
        target_compile_definitions(test.cpp PRIVATE _GLIBCXX_USE_CXX11_ABI=0)
    endif ()
endif ()

target_link_libraries(test.cpp
PRIVATE
OpenAssetIO::openassetio-core
OpenAssetIO-MediaCreation::openassetio-mediacreation)

target_compile_features(test.cpp PRIVATE cxx_std_17)

#-----------------------------------------------------------------------
# CMake Python packaging tests. (Dist-info)

if (OPENASSETIO_MEDIACREATION_ENABLE_PYTHON_INSTALL_DIST_INFO)

    # Build the command to extend the PYTHONPATH such that the
    # site-packages directory in the install tree is included correctly.
    set(_set_pythonpath_command
        PYTHONPATH=${CMAKE_INSTALL_PREFIX}/${OPENASSETIO_MEDIACREATION_PYTHON_SITEDIR})

    # Add pytest target to run the packaging tests. These are concerned
    # with python metadata information so run in a python context.
    add_custom_target(
        openassetio-mediacreation.tests.packaging
        COMMAND cmake -E echo -- "Running pytest check for CMake dist-info packaging"
        COMMAND ${_set_pythonpath_command} &&
        pytest -v --capture=tee-sys
        "${CMAKE_CURRENT_LIST_DIR}/test_cmake.py"
        WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
        USES_TERMINAL
    )

    # Create a test fixture that performs the install step.
    add_test(
        NAME openassetio-mediacreation.internal.tests.install
        COMMAND "${CMAKE_COMMAND}" --build "${PROJECT_BINARY_DIR}" --target install
    )
    set_tests_properties(openassetio-mediacreation.internal.tests.install
                         PROPERTIES FIXTURES_SETUP test_install)

    # Add the packaging test, and set the install as a required fixture.
    add_test(
        NAME  openassetio-mediacreation.tests.packaging
        COMMAND ${CMAKE_COMMAND} --build "${PROJECT_BINARY_DIR}"
        --target openassetio-mediacreation.tests.packaging
    )
    set_tests_properties(openassetio-mediacreation.tests.packaging
                         PROPERTIES FIXTURES_REQUIRED test_install)

    # Set the project version as an environment variable accesible to
    # the packaging tests.
    set_tests_properties(
        openassetio-mediacreation.tests.packaging
        PROPERTIES
        ENVIRONMENT OPENASSETIO_MEDIACREATION_CMAKE_PACKAGE_VERSION=${PROJECT_VERSION}
    )

endif ()
