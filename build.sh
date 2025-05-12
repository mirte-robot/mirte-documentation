#!/bin/bash
sudo apt update
sudo apt install libenchant-2-dev -y python3-empy zip
python3 -m pip install --upgrade pip
sudo apt install python3-venv -y
python3 -m venv docs-env
. docs-env/bin/activate
mkdir -p _modules/mirte-python
git clone https://github.com/mirte-robot/mirte-python -b develop _modules/mirte-python
pip install _modules/mirte-python/
pip install -r requirements.txt
make html
