####
# F prime CMakeLists.txt:
#
# SOURCE_FILES: combined list of source and autocoding files
# MOD_DEPS: (optional) module dependencies
#
# Note: using PROJECT_NAME as EXECUTABLE_NAME
####
set(SOURCE_FILES
    "${CMAKE_CURRENT_LIST_DIR}/GT1TopologyAppAi.xml"
    "${CMAKE_CURRENT_LIST_DIR}/Main.cpp"
    "${CMAKE_CURRENT_LIST_DIR}/Topology.cpp"
)
# Note: supply non-explicit dependencies here
set(MOD_DEPS
    Fw/Logger
    Svc/LinuxTime
    Os
)

register_fprime_executable()
