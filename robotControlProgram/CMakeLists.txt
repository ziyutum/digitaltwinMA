cmake_minimum_required(VERSION 3.4)
project(fci-workshop)

set(CMAKE_CXX_STANDARD 14)
#set(CMAKE_BUILD_TYPE "Debug")
set(CMAKE_BUILD_TYPE "RelWithDebInfo")

find_package(Eigen3 REQUIRED)
add_subdirectory(libfranka)

include_directories(src) # Added for chesslib.h

set(EXAMPLES
        communication_test
        bottleplacing
        brickplacing
        bottleplacing_reading_data
        bottleplacing_control
        test
        printjoint
        qcontrol
        chess
        chessV2
        torquecontrole
        )

foreach(example ${EXAMPLES})
    add_executable(${example} src/${example}.cpp)
    target_include_directories(${example} PUBLIC libfranka/examples)
    target_link_libraries(${example} franka examples_common)
endforeach()
