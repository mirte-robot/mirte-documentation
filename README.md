# Documentation MIRTE Robot

To build the documentation (requirement: Python3.10+):

```sh
git clone https://github.com/mirte-robot/mirte-documentation
cd mirte-documentation
git submodule update --init --recursive
python3 -m venv docs-env
source docs-env/bin/activate
pip install -r requirements.txt
cd _modules/mirte-python
pip install .
cd ../../

make html
# OR
sphinx-multiversion . _build/html
```




## Host locally
```
sphinx-reload . --watch doc/ _static/ _modules/  # browser will open automatically, don't forget the dot.
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



## Multi version setup
As the docs build uses other parts (ROS, Python, ...), just using sphinx-multiversion doesn't work 100%.
New setup:
- At release of a new version, a site.zip is created with the docs of that version without any other versions or version selector
- At creation of a new pages:
  - create dummy tags to generate the correct versions html
  - sphinx-multiversions build
  - for each release:
    - download the site.zip from the release page
    - take the versions html code from the 'dummy' and replace it in the downloaded version
  - push to github pages
