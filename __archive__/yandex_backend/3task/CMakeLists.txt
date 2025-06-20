cmake_minimum_required(VERSION 3.25)
project(CV_project LANGUAGES CXX)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++23")

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

add_executable(main ./main.cpp)