# draymed
This repository contains JavaScript and Python libraries for providing providing SNOMED (and custom) codes for Polaris
applications.

## Maintainers
The Polaris platform was created by Sensyne Health Ltd., and has now been made open-source. As a result, some of the
instructions, setup and configuration will no longer be relevant to third party contributors. For example, some of
the libraries used may not be publicly available, or docker images may not be accessible externally. In addition, 
CICD pipelines may no longer function.

For now, Sensyne Health Ltd. and its employees are the maintainers of this repository.

## JavaScript library
For documentation of the JavaScript `draymed` library, see [draymed_js/README.md](draymed_js/README.md)

## Python library
For documentation of the Python `draymed` library, see [draymed_py/README.md](draymed_py/README.md)

## Updating SNOMED/draymed codes
To update codes, update [master_codes.json](master_codes.json) and then run the `make copy-master-codes` command to 
copy the codes to the respective JavaScript and Python libraries.

* add new code to correct section of `master_codes.json`
* update version number - `.pre-commit-config.yaml`
* update version number - `draymed_js/package.json`
* update version number - `draymed_py/pyproject.toml`
* document the change - draymed_py/RELEASES.md
* run command `make copy-master-codes`
* check files
* commit changes / open PR
* make coffee
