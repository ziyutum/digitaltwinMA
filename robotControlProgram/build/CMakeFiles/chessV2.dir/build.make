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
include CMakeFiles/chessV2.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/chessV2.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/chessV2.dir/flags.make

CMakeFiles/chessV2.dir/src/chessV2.cpp.o: CMakeFiles/chessV2.dir/flags.make
CMakeFiles/chessV2.dir/src/chessV2.cpp.o: ../src/chessV2.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/masais/ziyu/robotControlProgram/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/chessV2.dir/src/chessV2.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/chessV2.dir/src/chessV2.cpp.o -c /home/masais/ziyu/robotControlProgram/src/chessV2.cpp

CMakeFiles/chessV2.dir/src/chessV2.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/chessV2.dir/src/chessV2.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/masais/ziyu/robotControlProgram/src/chessV2.cpp > CMakeFiles/chessV2.dir/src/chessV2.cpp.i

CMakeFiles/chessV2.dir/src/chessV2.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/chessV2.dir/src/chessV2.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/masais/ziyu/robotControlProgram/src/chessV2.cpp -o CMakeFiles/chessV2.dir/src/chessV2.cpp.s

# Object files for target chessV2
chessV2_OBJECTS = \
"CMakeFiles/chessV2.dir/src/chessV2.cpp.o"

# External object files for target chessV2
chessV2_EXTERNAL_OBJECTS =

chessV2: CMakeFiles/chessV2.dir/src/chessV2.cpp.o
chessV2: CMakeFiles/chessV2.dir/build.make
chessV2: libfranka/examples/libexamples_common.a
chessV2: libfranka/libfranka.so.0.9.0
chessV2: CMakeFiles/chessV2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/masais/ziyu/robotControlProgram/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable chessV2"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/chessV2.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/chessV2.dir/build: chessV2

.PHONY : CMakeFiles/chessV2.dir/build

CMakeFiles/chessV2.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/chessV2.dir/cmake_clean.cmake
.PHONY : CMakeFiles/chessV2.dir/clean

CMakeFiles/chessV2.dir/depend:
	cd /home/masais/ziyu/robotControlProgram/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/masais/ziyu/robotControlProgram /home/masais/ziyu/robotControlProgram /home/masais/ziyu/robotControlProgram/build /home/masais/ziyu/robotControlProgram/build /home/masais/ziyu/robotControlProgram/build/CMakeFiles/chessV2.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/chessV2.dir/depend
