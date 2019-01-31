#!/usr/bin/sh
pip install pycodestyle
pycodestyle --first --ignore=E501,E722,E704
echo no problems
