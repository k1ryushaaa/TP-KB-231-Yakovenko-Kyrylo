def enter():
    print(" (X це x^2): aX+bx+c")
    a = float(input('Напишіть a: '))
    b = float(input('Напишіть b: '))
    c = float(input('Напишіть c: '))
    return a, b, c

def discriminant(a, b, c):
    return b**2 - 4 * a * c

def find_roots(a, b, c):
    D = discriminant(a, b, c)
    
    if D > 0:
        x1 = (-b + D**0.5) / (2 * a)
        x2 = (-b - D**0.5) / (2 * a)
        return f"Два дійсні корені: x1 = {x1}, x2 = {x2}"
    elif D == 0:
        x = -b / (2 * a)
        return f"Один дійсний корінь: x = {x}"
    else:
        return "Дійсних коренів немає"
    
a, b, c = enter()
d = discriminant(a, b, c)
print(find_roots(a, b, d))
input("Натисніть Enter, щоб завершити")