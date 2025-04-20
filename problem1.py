class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b


calculator = Calculator()

a = 10.0
b = 2.0
operation = "divide"

if operation == "add":
    print("Result:", calculator.add(a, b))
elif operation == "subtract":
    print("Result:", calculator.subtract(a, b))
elif operation == "multiply":
    print("Result:", calculator.multiply(a, b))
elif operation == "divide":
    print("Result:", calculator.divide(a, b))
else:
    print("Invalid operation")
