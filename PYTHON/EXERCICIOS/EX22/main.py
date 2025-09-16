def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b  

def divide(a, b):
    if b == 0:

        return "Error: Division by zero"
    return a / b

def add(a, b):
    return a + b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

while True:
    num1 = float(input("Enter first number: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Choose an operation from the line above: ")
    num2 = float(input("Enter second number: "))
    
    print(f"{num1} {operation_symbol} {num2} = {operations[operation_symbol](num1, num2)}\n")
