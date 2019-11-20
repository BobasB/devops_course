#!/bin/bash
set -ev
nohup pipenv run server > ./ci-build.log &
pipenv run python monitoring.py || true
exit 0
