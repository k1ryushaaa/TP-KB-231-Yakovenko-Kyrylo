def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Помилка: ділення на нуль"

def calculator():
    operation = input("Оберіть операцію (+, -, *, /): ")
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    
    if operation == '+':
        print("Результат:", add(num1, num2))
    elif operation == '-':
        print("Результат:", subtract(num1, num2))
    elif operation == '*':
        print("Результат:", multiply(num1, num2))
    elif operation == '/':
        print("Результат:", divide(num1, num2))
    else:
        print("Помилка: некоректний вибір операції.")

calculator()
input("Натисніть Enter, щоб завершити")