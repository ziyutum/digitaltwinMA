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
include CMakeFiles/printjoint.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/printjoint.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/printjoint.dir/flags.make

CMakeFiles/printjoint.dir/src/printjoint.cpp.o: CMakeFiles/printjoint.dir/flags.make
CMakeFiles/printjoint.dir/src/printjoint.cpp.o: ../src/printjoint.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/masais/ziyu/robotControlProgram/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/printjoint.dir/src/printjoint.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/printjoint.dir/src/printjoint.cpp.o -c /home/masais/ziyu/robotControlProgram/src/printjoint.cpp

CMakeFiles/printjoint.dir/src/printjoint.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/printjoint.dir/src/printjoint.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/masais/ziyu/robotControlProgram/src/printjoint.cpp > CMakeFiles/printjoint.dir/src/printjoint.cpp.i

CMakeFiles/printjoint.dir/src/printjoint.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/printjoint.dir/src/printjoint.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/masais/ziyu/robotControlProgram/src/printjoint.cpp -o CMakeFiles/printjoint.dir/src/printjoint.cpp.s

# Object files for target printjoint
printjoint_OBJECTS = \
"CMakeFiles/printjoint.dir/src/printjoint.cpp.o"

# External object files for target printjoint
printjoint_EXTERNAL_OBJECTS =

printjoint: CMakeFiles/printjoint.dir/src/printjoint.cpp.o
printjoint: CMakeFiles/printjoint.dir/build.make
printjoint: libfranka/examples/libexamples_common.a
printjoint: libfranka/libfranka.so.0.9.0
printjoint: CMakeFiles/printjoint.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/masais/ziyu/robotControlProgram/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable printjoint"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/printjoint.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/printjoint.dir/build: printjoint

.PHONY : CMakeFiles/printjoint.dir/build

CMakeFiles/printjoint.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/printjoint.dir/cmake_clean.cmake
.PHONY : CMakeFiles/printjoint.dir/clean

CMakeFiles/printjoint.dir/depend:
	cd /home/masais/ziyu/robotControlProgram/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/masais/ziyu/robotControlProgram /home/masais/ziyu/robotControlProgram /home/masais/ziyu/robotControlProgram/build /home/masais/ziyu/robotControlProgram/build /home/masais/ziyu/robotControlProgram/build/CMakeFiles/printjoint.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/printjoint.dir/depend
