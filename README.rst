==========================================
GT-1 Satellite Amateur Radio Demonstration
==========================================

This repository contains the amateur radio payload code that is being
developed for the Georgia Institute of Technology's GT-1 educational
satellite mission.

The reference software deployment is found in the GT-1 subfolder of this repository.
This is *not* the full code for the GT-1 mission's flight software, it is only the components that operation the amateur radio payload functionality, and enough supporting infrastructure to stand up a test environment.
The goal is to allow the community to test the actual, relevant code in a context that is capable of operating over RF such that useful feedback can be gathered.

This demonstration software, as well as the GT-1 flight software, are
developed using JPL's F Prime flight software framework.

Quick Installation Guide
========================

F´ can be quickly install using the following instructions.
F´ requires that the following utilities be installed: cmake, git, and Python 3.5+ with pip.
Once these have been installed, users are recommended to install F´ python dependencies.
This is usually done in a Python virtual environment as this prevents issues at the system level, but is not required.
Full installation instructions including virtual environment creation, and installation verification: [INSTALL.md](./docs/INSTALL.md).
The following are the most basic steps for convenience.

```
git clone https://github.com/nasa/fprime.git
cd fprime
pip install Fw/Python Gds/
```



