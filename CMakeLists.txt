cmake_minimum_required(VERSION 3.16 FATAL_ERROR)
enable_language( C CXX )

project(example LANGUAGES C CXX)
#Set the install path

#Turn off lto junk
set(CMAKE_INTERPROCEDURAL_OPTIMIZATION OFF )

#Add all da files
file( GLOB example_src ./*.cpp)

include_directories(./)


#Make the bindings for python import
add_subdirectory(pybind11)
pybind11_add_module(example ${example_src} ${PROJECT_SOURCE_DIR}/bindings.cpp)

#Link to Kokkos
Find_Package(Kokkos REQUIRED)
target_link_libraries(example PUBLIC Kokkos::kokkos)
