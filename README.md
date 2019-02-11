# Simple python service
A simple Python service that shows system info and performs arithmetic operations

# How to run tests
```
python setup.py test
```

# How to package
At fitst install pip
```
pip install wheel
```
After this step you can create wheel
```
python setup.py sdist bdist_wheel
```

# How to install dependencies
```
python setup.py install
```
# How to run pycodestyle
```
bash pycodestyle.sh
```
# How to run the service
```
FLASK_APP=service.py flask run
```
Then go to [http://localhost:5000](http://localhost:5000)

# How to package with info about commit
```
git show --summary | awk '{print $2}' | head -1 >newcommit.txt && python setup.py sdist bdist_wheel
```
