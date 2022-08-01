# draymed-js
Javascript library for providing SNOMED (and custom) codes

## Updating SNOMED/DRAYMED codes

To update SNOMED/DRAYMED codes edit the source master_codes.json in the root folder of the draymed repository. 
Then use the Makefile in the root folder to copy the file to the Javascript library.
Do not edit the local copy of master_codes.json in the Javascript library directly.

## Deployment

When a PR is merged into master, a Circle CI job is triggered and the new code is pushed to gemfury.
For the new code to be available for install from Gemfury, the version in `pyproject.toml` must be bumped for every change.
Javascript library version must remain aligned with Python library version.
When incrementing Javascript library version in `package.json`, also increment Python library version in `pyproject.toml`.
