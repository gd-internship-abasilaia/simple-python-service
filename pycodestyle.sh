#!/usr/bin/sh
pip install pycodestyle
pip install --upgrade pycodestyle
pycodestyle --first --ignore=E501,E722,E704
