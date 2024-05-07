#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Franka::Franka" for configuration "RelWithDebInfo"
set_property(TARGET Franka::Franka APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Franka::Franka PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELWITHDEBINFO "Poco::Foundation;Poco::Net"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/libfranka.so.0.9.0"
  IMPORTED_SONAME_RELWITHDEBINFO "libfranka.so.0.9"
  )

list(APPEND _IMPORT_CHECK_TARGETS Franka::Franka )
list(APPEND _IMPORT_CHECK_FILES_FOR_Franka::Franka "${_IMPORT_PREFIX}/lib/libfranka.so.0.9.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
