#!/bin/bash

set -x

docker build -t telematics -f Dockerfile src/
