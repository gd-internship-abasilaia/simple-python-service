#!/usr/bin/sh
pip install pycodestyle
pycodestyle --first --ignore=E501,E722,E704 tests/test_calculator.py calc/calculator.py calculator_app.py setup.py service.py
