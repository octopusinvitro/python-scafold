[![Python version](https://badgen.net/badge/python/3.10/yellow)](Pipfile)
[![License](https://img.shields.io/github/license/octopusinvitro/python-scafold)](https://github.com/octopusinvitro/python-scafold/blob/main/LICENSE.md)
[![Maintainability](https://api.codeclimate.com/v1/badges/94311752b2ab4ee1ffe7/maintainability)](https://codeclimate.com/github/octopusinvitro/python-scafold/maintainability)
[![Build status](https://gitlab.com/octopusinvitro/python-scafold/badges/main/pipeline.svg)](https://gitlab.com/octopusinvitro/python-scafold/commits/main)


# README

This is an opinionated Python project starter. It uses `pipenv` for dependency management and `unittest` as a testing framework.


## Setup

* Update badges on top of README with your user/repo names.
* Update the license to your preferred one.
* Update the current python version (3.10) to your preferred one.
* Rename `module` to your project name and put your production code there.
* Put your tests in `tests`.
* The `bin` folder has scripts for basic commands. See examples of use in the CI config file and below.


## Install

Create an environment in your preferred way and then:

```sh
pipenv install --dev
```


## To run

```sh
. bin/run
```


## To test

```sh
. bin/test                    # all tests
. bin/test tests/test_file.py # single test
```


## To lint

```sh
. bin/lint
```
