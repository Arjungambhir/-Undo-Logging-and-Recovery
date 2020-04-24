#!/bin/bash

if [[ $# -eq 1 ]]; then
    python 2019900004_2.py "$1"
else
    echo "Invalid number of arguments"
fi
