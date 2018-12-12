# Packaging a python app and adding it to Pypi

## Setup
1) Make sure you have a pypi config file `~/.pypirc` which has your pypi account details

2) Organize code into package structure by adding a setup.py,setup.cfg, moving code to __init__.py, etc

3) Navigate to repository and add git tag so github can host the package:
`git tag 0.1 -m "Adds a tag so that we can put this on PyPI."`
`git push --tags origin`
Github will then create tarballs and add them to your repo

4) Packaging Source Distribution
`python setup.py sdist` will create a source distribution, which is an unbuilt package whose build step takes place when it is installed by pip

5) Packaging Wheel Distribution
Running this will require the wheel module, `pip install wheel` if you dont have it. Wheels are a built package which can be installed without needing a build step. Only appropriate if project is pure python (No C extensions, which would need to be built)
`python setup.py bdist_wheel` Create a wheel appropriate for the version of python used to run this command. Add `--universal` if the project can run on both python 2 and python 3

Both can be run at the same time with `python setup.py sdist bdist_wheel`

6) Testing
`pip install -e .` install package locally, with the "editable" option.

4) upload package to pypi test
`twine upload --repository testpypi dist/*`

5) Upload to pypi live
`twine upload --repository pypi dist/*`

Updating package
Delete `build` `dist` and `<package>.egg-info` folders 
Change version number in setup.py
recreate distribution e.g. `python setup.py sdist bdist_wheel`
reupload e.g. `twine upload --repository pypi dist/*`

## Versioning Schemas
Preferred scheme is "Symantic versioning": <MAJOR>.<MINOR>.<MAINTENANCE>
Increment MAJOR when making incompatible API changes
Increment MINOR when adding functionality while maintaining backwards compatibility 
Increment MAINTENANCE when making backwards compatible bug fixes

