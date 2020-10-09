#!/bin/bash
####
# bootstrap.bash:
#
# ** Assumes that the user is in the F prime root directory for F prime CI **
#
# Sets up the python environment for the CI system. This will read the latest Python and ensure
# that we are ready to run all tools.
####
export USABLE_VENV="${FPRIME_DIR}/ci-venv"
echo -e "${BLUE}Preparing VENV at: ${USABLE_VENV}${NOCOLOR}"
rm -r "${USABLE_VENV}"
python3 -m venv "${USABLE_VENV}" || fail_and_stop "Failed to create VENV"
. "${USABLE_VENV}/bin/activate" || fail_and_stop "Failed to source VENV"
echo -e "Installing PIP Packages"
pip install -U pip wheel || fail_and_stop "Failed to bootstrap pip"
pip install ./Fw/Python || fail_and_stop "Failed to install fprime PIP module from ./Fw/Python"
pip install ./Gds[test-api-xls] || fail_and_stop "Failed to install fprime PIP module from ./Gds[test-api-xls]"

