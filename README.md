# Simple python service
A simple Python service that shows system info and performs arithmetic operations

# How to run tests
```
python setup.py
```

# How to package
```
python setup.py sdist
```

# How to install dependencies
```
python setup.py install
```
# How to run pycodestyle
```
pip install pycodestyle
pycodestyle --first calculator_app.py calc/calculator.py tests/test_calculator.py setup.py
```
# How to run the service
```
FLASK_APP=service.py flask run
```
Then go to [http://localhost:5000](http://localhost:5000)
