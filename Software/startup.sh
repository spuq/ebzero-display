#!/bin/bash

##
#   Run your Python program on startup
##
PROGRAM1="crowtail_demo.py"
PROGRAM2="display.py"

# Get the directory of this file
parent_path=$(dirname "$0")

# Activate the virtual environment
. $parent_path/venv/bin/activate

# Start the Python program
python $parent_path/$PROGRAM2 &
python $parent_path/$PROGRAM1

