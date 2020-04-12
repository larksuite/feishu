#!/usr/bin/env bash

set -e
set -o pipefail

# https://pycryptodome.readthedocs.io/en/latest/src/installation.html
if [  -n "$(uname -a | grep Ubuntu)" ]; then
    if [[ `python -c "import sys; print(sys.version)"` == *"PyPy"* ]]; then
      sudo apt-get install build-essential pypy-dev
    else
      sudo apt-get install build-essential python-dev
    fi

    pip install pycryptodomex
    python -m Cryptodome.SelfTest
else
    echo "not ubuntu"
fi
