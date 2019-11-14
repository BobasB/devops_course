#!/bin/bash
set -ev
pipenv run server > ./ci-build.log 2>&1 &>/dev/null && pipenv run python monitoring.py
exit 0
