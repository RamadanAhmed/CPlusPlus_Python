cmake_minimum_required(VERSION 3.9)
project(CPlusPlus_Python)

set(CMAKE_CXX_STANDARD 11)

find_package(pybind11 REQUIRED)
find_package(Boost REQUIRED)

#pybind11_add_module(cmake_example main.cpp)
add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE pybind11::embed)