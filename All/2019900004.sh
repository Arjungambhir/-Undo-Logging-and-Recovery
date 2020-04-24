#!/bin/bash

if [[ $# -eq 2 ]]; then
    python 2019900004_1.py "$1" "$2"
	
elif [[ $# -eq 1 ]]; then
    python 2019900004_2.py "$1"
else
    echo "Invalid number of arguments"
	echo "to run logging use ==>>>>   python 201990004_1.py <input_file> <actions_count> "
	echo "to run logging use ==>>>>   python 201990004_1.py <input_file> <actions_count> "
	
fi
