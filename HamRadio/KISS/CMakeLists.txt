####
# F prime CMakeLists.txt:
#
# SOURCE_FILES: combined list of source and autocoding files
# MOD_DEPS: (optional) module dependencies
#
####
set(SOURCE_FILES
    "${CMAKE_CURRENT_LIST_DIR}/KISSComponentAi.xml"
    "${CMAKE_CURRENT_LIST_DIR}/KISSComponent.cpp"
)

# # Determine the platform specific source files to append:
# string(TOLOWER "${CMAKE_SYSTEM_NAME}" CMAKE_SYSTEM_NAME_LOWER)

# # CygWin platform additions
# if(${CMAKE_SYSTEM_NAME_LOWER} STREQUAL "cygwin")
#     list(APPEND SOURCE_FILES "${CMAKE_CURRENT_LIST_DIR}/KISSComponentCygWin.cpp")
# # Darwin platform additions
# elseif(${CMAKE_SYSTEM_NAME_LOWER} STREQUAL "darwin")
#     list(APPEND SOURCE_FILES "${CMAKE_CURRENT_LIST_DIR}/KISSComponentDarwin.cpp")
# # VxWorks platform additions
# elseif(${CMAKE_SYSTEM_NAME_LOWER} STREQUAL "vxworks")
#     list(APPEND SOURCE_FILES "${CMAKE_CURRENT_LIST_DIR}/KISSComponentVxWorks.cpp")
# # Otherwise, assume Linux-compatible build
# else()
#     list(APPEND SOURCE_FILES "${CMAKE_CURRENT_LIST_DIR}/KISSComponentLinux.cpp")
# endif()


# Uncomment and add any modules that this component depends on, else
# they might not be available when cmake tries to build this component.

# set(MOD_DEPS
#     Fw/Logger
# )

register_fprime_module()


