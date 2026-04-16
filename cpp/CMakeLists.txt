cmake_minimum_required(VERSION 3.16)
project(graph_tradeoff_cpp)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# core library
add_library(graph_core
    src/graph.cpp
    src/generator.cpp
    src/traversal.cpp
    src/benchmark.cpp
    src/utils.cpp
    src/executor.cpp
)

target_include_directories(graph_core PUBLIC include)

# main app
add_executable(graph_tradeoff src/main.cpp)

target_link_libraries(graph_tradeoff PRIVATE graph_core)