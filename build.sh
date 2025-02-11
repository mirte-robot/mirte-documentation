#!/bin/bash
git submodule update --init --recursive
sudo apt update
sudo apt install libenchant-2-dev -y python3-empy zip
python3 -m pip install --upgrade pip
apt install python3.8-venv -y
python3 -m venv docs-env
ls
ls docs-env
ls docs-env/bin
. docs-env/bin/activate
pip install -r requirements.txt
cd _modules/mirte-python
pip install .
pip install empy==3.3.4
cd ../catkin_ws/src/mirte-ros-packages
ls | grep -xv "mirte_msgs" | xargs rm -rf
cd ../../
catkin_make # or catkin build
. devel/setup.sh
cd ../../