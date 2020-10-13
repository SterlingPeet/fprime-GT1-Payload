# GT-1 Amateur Radio Payload F Prime Deployment

Demonstration F Prime deployment showing the functionality of the GT-1 mission's payload.

The purpose of this application is to demonstrate a completely assembled application on Linux, and Mac OSX.
This allows the user to get up and running quickly, test the installation, and work with the code.

## Prerequisites

Understanding the GT1erence application has a few minimal prerequisites.

**Installing F´**

Please follow the install guide for F´ found here: [INSTALL.md](../docs/INSTALL.md).

## Building and Running the GT1 Application

In order to build the GT1 application, or any other F´ application, we first need to generate a build directory.  F´ uses CMake under the hood,
which requires a directory to work in. To generate a build directory, we will use the `fprime-util` (a wrapper for CMake to streamline standard
F´ processses). This can be done with the following commands:

```
cd fprime/GT1
fprime-util generate
```

Now that the build directory has been generated, the user need not run `fprime-util generate` again unless the build directory has been removed.

The next step is to build the GT1 application's code.
This is done for the current system that the user is running on.
This is handled by CMake and will produce a binary that can be run on the user's system.
This is accomplished by using the `build` subcommand of `fprime-util`.
Since we will run the code next, we will also run the install command to ensure we may easily find the binaries.

```
fprime-util install
```

## Running the F´ Ground System and Code

F´ ships with a browser-based test ground system. This system is designed to help developers of F´ projects quickly test and work with F´ code
without much overhead. This ground system can be run with the following commands. Please note: the GT1 application's binary will also be run
automatically.  This allows for quick testing on Linux and Mac OSX. Please ensure that the binary has been built and installed as described above.

```
cd fprime/GT1
fprime-gds -d .
```

The user may now explore the "Commanding", "Event", and "Channels" tabs to see the F´ code in action.  The "Logs" tab has logs for the running
application should an error arise.  See: Logs -> GT1.log to see standard output of the GT1 app.

To run the ground system without starting the GT1 app:
```
cd fprime/GT1
fprime-gds -d . --no-app
```

The GT1 app may then be run independently from the created 'bin' directory.

```
cd fprime/GT1/bin/<architecture>
./GT1 -a 127.0.0.1 -p 50000
```

## Quick Tips

- The F´ GDS defaults to port 50000. More information can be found with `fprime-gds --help`
- The F´ utility's build command can build individual components too.
- The 'generate' command can take a toolchain argument for quickly generating a cross-compile `fprime-util generate raspberrypi` for example.

Further work with the F´ utility can be found in the [Getting Started](../docs/Tutorials/GettingStarted/Tutorial.md) tutorial. Other tutorials
for many aspects of F´ are available [here](../docs/Tutorials/README.md).

## Change Log

Date       | Description
---------- | -----------
10/09/2020 | Initial Deployment Design

