#!/usr/bin/env bash

set -e
set -o pipefail

if [[ $1 == "cov" ]]
then
    echo "cov mode"
else
   echo "test mode"
fi

cur=$(pwd)

echo "cur dir is $cur"

# https://pycryptodome.readthedocs.io/en/latest/src/installation.html
if [  -n "$(uname -a | grep Ubuntu)" ]; then
    sudo apt-get install build-essential python-dev
    pip install pycryptodomex
    python -m Cryptodome.SelfTest
else
    echo "not ubuntu"
fi

if [[ $1 == "cov" ]]
then
    tox | tee test_output.txt

    output_filename="$cur/test_output.txt"

    coverage_percent=$(cat $output_filename | grep 'TOTAL' | egrep -o '([0-9]+)%')

    echo "覆盖率: $coverage_percent"
else
   tox
fi
