# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/masais/ziyu/robotControlProgram

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/masais/ziyu/robotControlProgram/build

# Include any dependencies generated for this target.
include CMakeFiles/communication_test.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/communication_test.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/communication_test.dir/flags.make

CMakeFiles/communication_test.dir/src/communication_test.cpp.o: CMakeFiles/communication_test.dir/flags.make
CMakeFiles/communication_test.dir/src/communication_test.cpp.o: ../src/communication_test.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/masais/ziyu/robotControlProgram/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/communication_test.dir/src/communication_test.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/communication_test.dir/src/communication_test.cpp.o -c /home/masais/ziyu/robotControlProgram/src/communication_test.cpp

CMakeFiles/communication_test.dir/src/communication_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/communication_test.dir/src/communication_test.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/masais/ziyu/robotControlProgram/src/communication_test.cpp > CMakeFiles/communication_test.dir/src/communication_test.cpp.i

CMakeFiles/communication_test.dir/src/communication_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/communication_test.dir/src/communication_test.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/masais/ziyu/robotControlProgram/src/communication_test.cpp -o CMakeFiles/communication_test.dir/src/communication_test.cpp.s

# Object files for target communication_test
communication_test_OBJECTS = \
"CMakeFiles/communication_test.dir/src/communication_test.cpp.o"

# External object files for target communication_test
communication_test_EXTERNAL_OBJECTS =

communication_test: CMakeFiles/communication_test.dir/src/communication_test.cpp.o
communication_test: CMakeFiles/communication_test.dir/build.make
communication_test: libfranka/examples/libexamples_common.a
communication_test: libfranka/libfranka.so.0.9.0
communication_test: CMakeFiles/communication_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/masais/ziyu/robotControlProgram/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable communication_test"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/communication_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/communication_test.dir/build: communication_test

.PHONY : CMakeFiles/communication_test.dir/build

CMakeFiles/communication_test.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/communication_test.dir/cmake_clean.cmake
.PHONY : CMakeFiles/communication_test.dir/clean

CMakeFiles/communication_test.dir/depend:
	cd /home/masais/ziyu/robotControlProgram/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/masais/ziyu/robotControlProgram /home/masais/ziyu/robotControlProgram /home/masais/ziyu/robotControlProgram/build /home/masais/ziyu/robotControlProgram/build /home/masais/ziyu/robotControlProgram/build/CMakeFiles/communication_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/communication_test.dir/depend

