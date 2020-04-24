#!/bin/bash

if [[ $# -eq 2 ]]; then
    python 2019900004_1.py "$1" "$2"
else
    echo "Invalid number of arguments"
fi
