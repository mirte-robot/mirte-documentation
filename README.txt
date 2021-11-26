$ python3 -m venv docs-env
$ source docs-env/bin/activate
(docs-env)$ pip install sphinx sphinx-prompt sphinx-tabs
(docs-env)$ mkdir _modules
(docs-env)$ cd _modules
(docs-env)$ git clone https://github.com/mirte-robot/mirte-python
(docs-env)$ mkdir -p catkin_ws/src
(docs-env)$ cd catkin_ws/src
(docs-env)$ git clone https://github.com/mirte-robot/mirte-ros-packages
(docs-env)$ rm -rfv !("mirte-msgs")
(docs-env)$ cd ../..
(docs-env)$ catkin make
(docs-env)$ cd ..
(docs-env)$ make html


$ firefox _build/html/index.html
