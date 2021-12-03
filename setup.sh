#!/bin/zsh
ENV_NAME = "advent_code"

if [[ -d ./${ENV_NAME} ]]
then
    echo "Virtual environment exists, activating..."
    source ${ENV_NAME}/bin/activate
else
    echo "Virtual environment doesn't exist, setting up"
    sudo apt install virtualenv
    virtualenv --python=python3 ${ENV_NAME}
    source ${ENV_NAME}/bin/activate
    pip install upgrade pip
    pip install -r requirements.txt
