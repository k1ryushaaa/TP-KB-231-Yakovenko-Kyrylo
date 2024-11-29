def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def rsub(a, b):
    return b - a

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "не ділиться на 0, будь ласка, введіть наступне число, яке не дорівнює 0."
    else:
        return a / b

def rdiv(a, b):
    if a == 0:
        return "can't be divided by 0, now you result equal to 0, try another action"
    else:
        return b / a

def deg(a, b):
    return a ** b

def rdeg(a, b):
    return b ** a