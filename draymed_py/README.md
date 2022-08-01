# Draymed

Sensyne Health library for medical related helper functions and SNOMED codes

## Installing

It's generally a good idea to have the latest version of pip installed:

```bash
pip3 install --upgrade pip
```

You will need `PIP_EXTRA_INDEX_URL` defined.
More information can be found here: [Dev Environment Setup](https://sensynehealth.atlassian.net/wiki/spaces/SENS/pages/3193270/Environment+setup)

```bash
make install
```

or

```bash
poetry install -v
```

## Running the tests

Draymed uses tox to run its unit tests. 

Tox can be installed as follows:
```bash
pip3 install --upgrade tox
```

run tox from inside the repo (at the same level as `tox.ini`):
```bash
make test
```

Tox will also perform a few checks on the code:

- flake8: checks code style violations
- bandit: checks for known vulnerabilities in the code
- safety: checks for known vulnerabilities in the code
- coverage: runs the unit tests (using pytest) and generates a coverage report
- mypy: type checking
- black: code formatting
- isort: import sorting

coverage can be configured in `.coveragerc`: 
all other configuration is in `tox.ini`

## Deployment

When a PR is merged into master, a Circle CI job is triggered and the new code is pushed to gemfury.
For the new code to be available for install from Gemfury, the version in `pyproject.toml` must be bumped for every change.
Javascript library version must remain aligned with Python library version.
When incrementing Python library version in `pyproject.toml`, also increment Javascript library version in `package.json`.

## Updating SNOMED/DRAYMED codes

To update SNOMED/DRAYMED codes edit the source master_codes.json in the root folder of the draymed repository. 
Then use the Makefile in the root folder to copy the file to the Python library.
Do not edit the local copy of master_codes.json in the Python library directly.

## Usage

#### Calculating BMI

BMI can be calculated using a patients height (millimeters) and weight (grams).
The resulting value is returned as a float.

If either parameter is 0, a ValueError is raised (to avoid division by 0)

```python

import draymed

patient_height = 18000  # 1.8m in millimeters
patient_weight = 75000  # 75kg in grams

draymed.bmi(patient_height, patient_weight) 
# 0.23

```

#### Validating an NHS number

NHS numbers are considered valid if they can be matched using the following regex pattern: `^[0-9]{10}$`

```python

from draymed_py import draymed

bad_nhs_number = "not-a-valid-nhs-number"
draymed.validate_nhs_number(bad_nhs_number)
# False

valid_nhs_number = "1726358394"
draymed.validate_nhs_number(valid_nhs_number)
# True
```

#### Calculating pregnancy stage

Given an estimated delivery date (as a `datetime.date` object), 
draymed will return a named tuple containing the number of days/weeks that have elapsed since conception and a pre-formatted string to display the results.

- weeks: the number of weeks into the pregnancy
- days: the number of days into the next full week (will always be 0-6)
- string: a pre-formatted string to display the result with. eg. `3 weeks 4 days`

If delivery_date is None, a ValueError is raised 

```python
import datetime
import draymed.pregnancy

pregnancy_stage = draymed.pregnancy.stage(datetime.date(year=2019, month=10, day=2))
# PregnancyStage(weeks=11, days=0, string='11 weeks 0 days')

pregnancy_stage.weeks
# 10

pregnancy_stage.days
# 4

pregnancy_stage.string
# '10 weeks 4 days'
```

### Querying snomed/draymed codes

Draymed contains all of the snomed/draymed codes used in Digital Health products.
They are arranged by category and can be queried in a number of ways:

NOTE: `DM00000x` are used solely for routing keys in rabbitMQ

##### name_from_code

This will return a human readable label associated with a given code.

ValueError is raised if:

- the code is None.

KeyError is raised if:

- category is defined but does not exist
- a category is defined and the code does not exist in that category
- the code can not be found in the map

```python
import draymed.codes

draymed.codes.description_from_code("443911005")
# HBA1C

```

If you already know which category this code belongs to, you can reduce the overhead in searching for it by passing it in as a keyword argument.

```python
import draymed.codes

draymed.codes.description_from_code("443911005", category="observable_entity")
# HBA1C

```

##### code_from_name

This does the exact opposite of `name_from_code` in that it takes a snomed/draymed code and returns the label associated with it.

ValueError is raised if:

- the name is None.

KeyError is raised if:

- category is defined but does not exist
- a category is defined and the name does not exist in that category
- the name can not be found in the map

```python
import draymed.codes

draymed.codes.code_from_name("HBA1C")
# 443911005

```

Again, if the category is known, it is generally best to pass that in too to save unnecessary overhead.

```python
import draymed.codes

draymed.codes.code_from_name("HBA1C", category="observable_entity")
# 443911005

```

##### category_from_code

This will return the category label for a given snomed/draymed code

ValueError is raised if:

- code is None

KeyError is raised if:

- the code can not be found in the map

```python
import draymed.codes

draymed.codes.category_from_code("443911005")
# observable_entity

```

##### category_from_name

This does the same as `category_from_code` but instead of a code, it takes the label associated with a code and returns the category

ValueError is raised if:

- name is None

KeyError is raised if:

- the name can not be found in the map

```python
import draymed.codes

draymed.codes.category_from_name("HBA1C")
# observable_entity

```

##### code_exists

This will return true if a given code exists in a particular scope

You can see if a code exists anywhere in the code map:

ValueError is raised if:

- code is None

KeyError is raised if:

- a category is supplied but does not exist in map

```python
import draymed.codes

draymed.codes.code_exists("398254007")
# True

draymed.codes.code_exists("not-a-real-code")
# False
```

Or you can see if the code exists in a defined category:

```python
import draymed.codes

draymed.codes.code_exists("398254007", category="pregnancy_complications")
# True

draymed.codes.code_exists("398254007", category="diabetes_type")
# False
```


##### list_category

Takes a category name and returns a python dictionary where the key is a snomed/draymed code and the value is the label associated with that code

ValueError is raised if:

- category is None

KeyError is raised if:

- the category can not be found in the map

```python
import draymed.codes

draymed.codes.list_category("diabetes_type")
# {'11687002': 'GDM', '46635009': 'type1', '44054006': 'type2', '237604008': 'mody', 'D0000001': 'other'}

```

##### find_or_none

This should not really be used...
But if you really need to:

```python

import draymed.codes

draymed.codes.list_category("not-a-category")
# this would raise a KeyError

draymed.codes.find_or_none(
    draymed.codes.list_category,
    "not-a-category"
)
# None

```
