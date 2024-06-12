#!/bin/bash

# set -o errexit
# set -o nounset

uvicorn app.main:app --port=8081 --host 0.0.0.0
