$ python3 -m venv docs-env
$ source docs-env/bin/activate
(docs-env)$ pip install sphinx sphinx-prompt sphinx-tabs sphinx-rtd-theme sphinxcontrib-spelling sphinxcontrib-napoleon
(docs-env)$ mkdir -p _modules/catkin_ws/src
(docs-env)$ cd _modules
(docs-env)$ git clone https://github.com/mirte-robot/mirte-python
(docs-env)$ cd mirte-robot
(docs-env)$ pip install .
(docs-env)$ cd ../catkin_ws/src
(docs-env)$ git clone https://github.com/mirte-robot/mirte-ros-packages
(docs-env)$ cd mirte-ros-packages
(docs-env)$ rm -rfv !("mirte-msgs")
(docs-env)$ cd ../../
(docs-env)$ catkin_make
(docs-env)$ source devel/setup.bash
(docs-env)$ cd ../../
(docs-env)$ make html
(docs-env)$ python3 -m http.server


$ firefox _build/html/index.html
