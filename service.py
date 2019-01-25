from flask import Flask, request
from calc.calculator import Calculator

app = Flask(__name__)

@app.route("/")
def root():
    return "Try <a href='add'>/add</a> <a href='sub'>/sub</a> <a href='mult'>/mult</a> and <a href='div'>/div</a> URLs"

@app.route("/add")
def add():
    try:
        a = request.args.get('a')
        b = request.args.get('b')
        return str(Calculator.add(float(a),float(b)))
    except:
        return "Usage <a href='add?a=3&b=5'>example</a>".format(request.host_url)

