#!/bin/sh
virtualenv virtenv
source virtenv/bin/activate
pip install -r requirements.txt
deactivate