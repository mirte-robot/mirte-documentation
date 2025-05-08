#!/bin/bash
git submodule update --init --recursive
sudo apt update
sudo apt install libenchant-2-dev -y python3-empy zip
python3 -m pip install --upgrade pip
sudo apt install python3.10-venv -y
python3 -m venv docs-env
ls
ls docs-env
ls docs-env/bin
. docs-env/bin/activate
pip install _modules/mirte-python/
pip install -r requirements.txt
make html
