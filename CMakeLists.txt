cmake_minimum_required(VERSION 3.9)
project(CPlusPlus_Python)

set(CMAKE_CXX_STANDARD 11)

find_package(Boost REQUIRED)

add_executable(CPlusPlus_Python main.cpp)