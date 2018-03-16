cmake_minimum_required(VERSION 2.8)
project(CPlusPlus_Python)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/..)
set(CMAKE_CXX_STANDARD 11)

find_package(pybind11 REQUIRED)

#pybind11_add_module(cmake_example main.cpp)
add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE pybind11::embed)