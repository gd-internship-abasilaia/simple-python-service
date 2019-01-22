import sys


class Calculator:
    @staticmethod
    def add(x, y): return x + y

    @staticmethod
    def sub(x, y): return x - y

    @staticmethod
    def mul(x, y): return x * y

    @staticmethod
    def div(x, y): return x / y


x= float(sys.argv[1])
d = sys.argv[2]
y = float(sys.argv[3])

if d == '+':
    e = float(x + y)
elif d == '-':
    e = float(x - y)
elif d == '*':
    e = str(x * y)
elif d == '/':
    e = float(y / x)

print(e)
