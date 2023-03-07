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
