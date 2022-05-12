$ git clone --recurse-submodules https://github.com/mirte-robot/mirte-documentation
$ cd mirte-documentation
$ python3 -m venv docs-env
$ source docs-env/bin/activate
(docs-env)$ pip install wheel sphinx sphinx-prompt sphinx-tabs sphinx-rtd-theme sphinxcontrib-spelling sphinxcontrib-napoleon sphinx-multiversion
(docs-env)$ cd _modules/mirte-python
(docs-env)$ pip install .
(docs-env)$ cd ../catkin_ws/src/mirte-ros-packages
(docs-env)$ rm -rfv !("mirte_msgs")
(docs-env)$ cd ../../
(docs-env)$ catkin_make
(docs-env)$ source devel/setup.bash
(docs-env)$ cd ../../


(docs-env)$ make html
OR
(docs-env)$ sphinx-multiversion . _build/html


(docs-env)$ python3 -m http.server
$ firefox _build/html/index.html
