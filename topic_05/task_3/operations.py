def enter():
    while True:
        a = input("Для виходу із програми — напишіть 'ex' \nНапишіть ваш номер: ")
        if a != "ex":
            try:
                a = float(a)
            except ValueError:
                print("Це не цифра\n")
                continue
            return a
        else:
            exit(0)

def actions(a):
    print("\nPS — з обміном позицій значень \n'+' — сумма, '-' — різниця, '!-' — різниця (PS), '*' — добуток, '/' — ділення, '!/' — ділення (PS), '^' — піднесення в степінь, '!^' — піднесення в степінь (PS), або 'ex' для виходу із програми")
    action = input("Виберіть дію: ")
    if action == "ex":
        print("\nваш поточний результат = ", a)
        exit(0)
    elif action in ["+", "-", "!-", "*", "/", "!/", "^", "!^"]:
        return action
    else:
        print("Це не працює")