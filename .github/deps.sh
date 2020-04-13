#!/usr/bin/env bash

set -e
set -o pipefail

# https://pycryptodome.readthedocs.io/en/latest/src/installation.html
if [  -n "$(uname -a | grep Ubuntu)" ]; then
    if [[ `python -c "import sys; print(sys.version)"` == *"PyPy"* ]]; then
      sudo apt-get install libssl-dev build-essential pypy-dev gcc
    else
      sudo apt-get install build-essential python-dev gcc
    fi
fi

if [  -n "$(uname -a | grep Darwin)" ]; then
    brew install openssl gcc
fi
