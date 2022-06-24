[![Python version](https://badgen.net/badge/python/3.8/yellow)](Pipfile)
[![License](https://img.shields.io/github/license/octopusinvitro/python-scafold)](https://github.com/octopusinvitro/python-scafold/blob/main/LICENSE.md)
[![Maintainability](https://api.codeclimate.com/v1/badges/94311752b2ab4ee1ffe7/maintainability)](https://codeclimate.com/github/octopusinvitro/python-scafold/maintainability)
[![Build status](https://gitlab.com/octopusinvitro/python-scafold/badges/main/pipeline.svg)](https://gitlab.com/octopusinvitro/python-scafold/commits/main)


# README

This is an opinionated Python project starter.

It uses `pipenv` for dependecy management and `unittest` as a testing framework.

Update badges with your user/repo names and the license to your preferred one.

Rename `packagename` to your project name and put your production code there. Put your tests in `tests`. The `bin` folder has scripts for daily commands.


## Install

```sh
pipenv install
```


## To run

```sh
. bin/run path/to/script.py
```


## To lint

```sh
. bin/lint
```


### To test

```sh
. bin/test                    # all tests
. bin/test tests/test_file.py # single test
```
