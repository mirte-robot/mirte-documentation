# Documentation Mirte Robot

To build the documentation:

```sh
git clone --recurse-submodules https://github.com/mirte-robot/mirte-documentation
cd mirte-documentation
python3 -m venv docs-env
source docs-env/bin/activate
pip install -r requirements.txt
cd _modules/mirte-python
pip install .
cd ../catkin_ws/src/mirte-ros-packages
rm -rfv !("mirte_msgs")
cd ../../
catkin_make # or catkin build
source devel/setup.bash
cd ../../


make html
# OR
sphinx-multiversion . _build/html
```




## Host locally
```
python3 -m http.server
firefox _build/html/index.html
```
## Test

The documentation must pass the following two checks. Warnings are allowed, errors not.
```sh
make html && make linkcheck
```

## Spelling
Check for spelling with the following command
```sh
make spelling
```
Add correct words to the ```spelling_wordlist.txt``` file.