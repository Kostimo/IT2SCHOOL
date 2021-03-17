class Calculator():

    @staticmethod
    def add(a, b):
        return a+b

    @staticmethod
    def subtract(a, b):
        return a-b

    @staticmethod
    def multiply(a, b):
        return a*b
        
    @staticmethod
    def divide(a, b):
        return a/b

a = int(input(": "))
b = int(input(": "))
c = input("type: ")

if c == "+":
    print(Calculator.add(a, b))
elif c == "-":
    print(Calculator.subtract(a, b))
elif c == "*":
    print(Calculator.multiply(a, b))
else:
    print(Calculator.divide(a, b))