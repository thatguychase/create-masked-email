#!/bin/bash

set -e

virtualenv virtualenv
source virtualenv/bin/activate
pip3 install -r requirements.txt
deactivate