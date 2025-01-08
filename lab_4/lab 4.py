from collections import deque

# Пріоритети операторів
OPERATORS = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
LEFT_ASSOC = {'+': True, '-': True, '*': True, '/': True, '^': False}

def infix_to_rpn(expression):
    """Перетворення інфіксного запису у ЗПЗ."""
    output = []
    stack = []
    for token in tokenize(expression):
        if token.isnumeric():  # Якщо число
            output.append(token)
        elif token in OPERATORS:  # Якщо оператор
            while (stack and stack[-1] in OPERATORS and
                   ((LEFT_ASSOC[token] and OPERATORS[token] <= OPERATORS[stack[-1]]) or
                    (not LEFT_ASSOC[token] and OPERATORS[token] < OPERATORS[stack[-1]]))):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':  # Відкрита дужка
            stack.append(token)
        elif token == ')':  # Закрита дужка
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Видаляємо '(' зі стека
    while stack:  # Додаємо решту операторів зі стека
        output.append(stack.pop())
    return output

def evaluate_rpn(rpn_expression):
    """Обчислення результату виразу у ЗПЗ."""
    stack = deque()
    for token in rpn_expression:
        if token.isnumeric():
            stack.append(float(token))
        elif token in OPERATORS:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)
    return stack.pop()

def tokenize(expression):
    """Розбиття виразу на токени."""
    tokens = []
    num = ''
    for char in expression:
        if char.isdigit() or char == '.':
            num += char
        else:
            if num:
                tokens.append(num)
                num = ''
            if char in OPERATORS or char in '()':
                tokens.append(char)
    if num:
        tokens.append(num)
    return tokens

if __name__ == '__main__':
    expression = input("Введіть математичний вираз: ")
    rpn = infix_to_rpn(expression)
    print("ЗПЗ:", ' '.join(rpn))
    result = evaluate_rpn(rpn)
    print("Результат:", result)