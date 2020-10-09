"""
(test) fprime.build:

Tests the current F prime build module. Ensures that the selected singleton defines the minimum set of functions and
that they function as expected.

@author mstarch
"""
import os
import pytest
import shutil
import tempfile

import fprime.fbuild


def get_data_dir():
    """
    Gets directory containing test-data specific to the builder being tested. This will enable new implementors, should
    there be any, to implement their own build-directory structure.
    :return:
    """
    if type(fprime.fbuild.builder()) == fprime.fbuild.CMakeHandler:
        return os.path.join(os.path.dirname(__file__), "cmake-data")
    raise Exception("Test data directory not setup for {} builder class".format(type(fprime.fbuild.builder())))


def test_hash_finder():
    """
    Tests that the hash finder works given a known builds.
    """
    build_dir = os.path.join(os.path.dirname(__file__), "cmake-data", "testbuild")
    assert fprime.fbuild.builder().find_hashed_file(build_dir, 0xdeadbeef) == ["Abc: 0xdeadbeef\n"]
    assert fprime.fbuild.builder().find_hashed_file(build_dir, 0xc0dec0de) == ["HJK: 0xc0dec0de\n"]


def test_needed_functions():
    """
    Test the needed functions for the given builder. This will ensure that the public interface to the builder is
    implemented as expected.
    """
    needed_funcs = ["get_include_info", "find_nearest_standard_build", "execute_known_target", "get_include_locations",
                    "get_fprime_configuration"]
    for func in needed_funcs:
        assert hasattr(fprime.fbuild.builder(), func)


def test_get_fprime_configuration():
    """
    Tests the given fprime configuration fetcher. Required for other portion of the system.
    """
    configs = fprime.fbuild.cmake.CMakeHandler.CMAKE_LOCATION_FIELDS
    test_data = {
        "grand-unified": ("/home/user11/fprime/Ref/..", None, "/home/user11/fprime/Ref/.."),
        "subdir": ("/home/user11/Proj", "/home/user11/Proj/lib1;/home/user11/Proj/lib2", "/home/user11/Proj/fprime"),
        "external": ("/home/user11/Proj", "/opt/lib1;/opt/lib2", "/opt/fprime")
    }
    for key in test_data.keys():
        build_dir = os.path.join(get_data_dir(), key)
        # Test all path, truth pairs
        values = fprime.fbuild.builder().get_fprime_configuration(configs, build_dir)
        assert values == test_data[key]


def test_get_include_locations():
    """
    Test all the include locations. This will ensure that values are properly read from a cache listing. This will
    support various other portions of the system, so debug here firest.
    """
    test_data = {
        "grand-unified": ["/home/user11/fprime"],
        "subdir": ["/home/user11/Proj", "/home/user11/Proj/lib1", "/home/user11/Proj/lib2", "/home/user11/Proj/fprime"],
        "external": ["/home/user11/Proj", "/opt/lib1", "/opt/lib2", "/opt/fprime"]
    }
    for key in test_data.keys():
        build_dir = os.path.join(get_data_dir(), key)
        paths = list(fprime.fbuild.builder().get_include_locations(build_dir))
        assert paths == test_data[key]


def test_get_include_info():
    """
    Tests that the include root function gets the expected value based on the path and build-directory setups.
    """
    # Test data setup, format build_dir to tuples of path, expected result. Note: None means expect Orphan exception
    test_data = {
        "grand-unified": [
            ("/home/user11/fprime/Svc/SomeComp1", ("Svc/SomeComp1", "/home/user11/fprime")),
            ("/home/user11/fprime/Ref/SomeComp2", ("Ref/SomeComp2", "/home/user11/fprime")),
            ("/home/user11/fprime/Ref/SomeComp2/../SomeComp1", ("Ref/SomeComp1", "/home/user11/fprime")),
            ("/home/user11/external-sw/NachoDeploy/SomeComp3", None)
        ],
        "subdir": [
            ("/home/user11/Proj/fprime/Svc/SomeComp1", ("Svc/SomeComp1", "/home/user11/Proj/fprime")),
            ("/home/user11/Proj/Ref/SomeComp2", ("Ref/SomeComp2", "/home/user11/Proj")),
            ("/home/user11/Proj/Ref/SomeComp2/../../fprime/Svc/SomeComp1",
             ("Svc/SomeComp1", "/home/user11/Proj/fprime")),
            ("/home/user11/external-sw/NachoDeploy/SomeComp3", None)
        ],
        "external": [
            ("/opt/fprime/Svc/SomeComp1", ("Svc/SomeComp1", "/opt/fprime")),
            ("/home/user11/Proj/Ref/SomeComp2", ("Ref/SomeComp2", "/home/user11/Proj")),
            ("/opt/something/else/external-sw/NachoDeploy/SomeComp3", None)
        ]
    }
    # Run through all the above data look for matching ansers
    for key in test_data.keys():
        build_dir = os.path.join(get_data_dir(), key)
        # Test all path, truth pairs
        for path, truth in test_data.get(key):
            if truth is None:
                with pytest.raises(fprime.fbuild.cmake.CMakeOrphanException):
                    value = fprime.fbuild.builder().get_include_info(path, build_dir)
            else:
                value = fprime.fbuild.builder().get_include_info(path, build_dir)
                assert value == truth


def test_find_nearest_std_build():
    """
    Tests the nearest build detector to ensure that it functions as expected. This assumes that no standard build exist
    in the tree outside the erroneous paths. This should not be a problem unless standard builds exist on the root of
    the file system, as the rest of the path will be non-sensical.
    """
    NAME_CONST = fprime.fbuild.cmake.CMakeHandler.CMAKE_DEFAULT_BUILD_NAME.replace("{}", "")
    test_dir = get_data_dir()
    test_data = [
        ("abcdefg", "testbuild/subdir1/subdir2/subdir3", "testbuild/subdir1/" + NAME_CONST + "abcdefg"),
        ("default", "testbuild/subdir1/subdir2/subdir3",
         "testbuild/subdir1/subdir2/subdir3/" + NAME_CONST + "default"),
        ("abcdefg", "testbuild/subdir1/subdir2", "testbuild/subdir1/" + NAME_CONST + "abcdefg"),
        ("default", "testbuild/subdir1/subdir2", "testbuild/" + NAME_CONST + "default"),
        ("abcdefg", "/nonexistent/dirone/someotherpath", None)
    ]
    for platform, path, truth in test_data:
        if truth is not None:
            path = os.path.join(test_dir, path)
            truth = os.path.join(test_dir, truth)
            value = fprime.fbuild.builder().find_nearest_standard_build(platform, path)
            assert value == truth
        else:
            with pytest.raises(fprime.fbuild.cmake.CMakeException):
                fprime.fbuild.builder().find_nearest_standard_build(platform, path)


def test_generate():
    """
    Generate a directory and ensure that it works via CMake. This tests the common setup flags for normal and testing
    builds. Will also test the right errors are raised.
    """
    rms = []
    try:
        test_flags = [{}, {"CMAKE_BUILD_TYPE": "Testing"}]
        # Build Ref with flags
        path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "..", "Ref")
        for flags in test_flags:
            # Create a temp directory and register its deletion at the end of the program run
            tempdir = tempfile.mkdtemp()
            rms.append(tempdir)
            fprime.fbuild.builder().generate_build(path, tempdir, flags, ignore_output=True)
        # Expect errors for this step
        path = "/nopath/somesuch/nothing"
        with pytest.raises(fprime.fbuild.cmake.CMakeProjectException):
            tempdir = tempfile.mkdtemp()
            rms.append(tempdir)
            fprime.fbuild.builder().generate_build(path, tempdir, ignore_output=True)
    # Clean-Up all the directories made
    finally:
        for rmd in rms:
            shutil.rmtree(rmd, ignore_errors=True)


def test_targets():
    """
    Test standard targets for the build.
    """
    # Build Ref with flags
    tempdir = None
    try:
        fprime_root = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "..")
        # Create a temp directory and register its deletion at the end of the program run
        tempdir = tempfile.mkdtemp()
        fprime.fbuild.builder().generate_build(os.path.join(fprime_root, "Ref"), tempdir, {"CMAKE_BUILD_TYPE": "Testing"})
        test_data = [(os.path.join(fprime_root, "Ref"), ""),
                     (os.path.join(fprime_root, "Svc", "CmdDispatcher"), ""),
                     (os.path.join(fprime_root, "Svc", "CmdDispatcher"), "ut_exe"),
                     (os.path.join(fprime_root, "Svc", "CmdDispatcher"), "check")]
        # Loop over all directories and target pairs ensuing things work
        for path, target in test_data:
            fprime.fbuild.builder().execute_known_target(target, tempdir, path)
        test_data = [(os.path.join(fprime_root, "Svc", "CmdDispatcher"), "nontarget1"),
                     (os.path.join(fprime_root, "Svc", "CmdDispatcher3Not"), "")]
        # Loop over all paths and target pairs looking for expected Exceptions
        for path, target in test_data:
            with pytest.raises(fprime.fbuild.cmake.CMakeException):
                fprime.fbuild.builder().execute_known_target(target, tempdir, path)
    # Clean up when all done
    finally:
        if tempdir is not None:
            shutil.rmtree(tempdir, ignore_errors=True)
