def enter():
    while True:
        a = input("Вийти з програми - пишіть 'ex' \nНапишіть ваш номер: ")
        if a != "ex":
            try:
                a = float(a)
            except ValueError:
                print("Це не номер\n")
                continue
            return a
        else:
            exit(0)

def operations(a):
    while True:
        b = str(input("Напишіть наступний номер або для того щоб вийти з програми - пишіть 'ex': "))

        if b != "ex":

            try:
                b = float(b)
            except ValueError:
                print("Це не номер")
                continue
            
            print("\nPS — PS — зі значеннями зміни позиції \n'+' — сумма, '-' — різниця, '!-' — різниця (PS), '*' — добуток, '/' — ділення, '!/' — ділення (PS), '^' — піднесення в степінь, '!^' — піднесення в степінь (PS), або 'ex' щоб вийти із програми")
            action = input("Виберіть дію: ")

            match action:
                case "+":
                    a += b
                case "-":
                    a -= b
                case "!-":
                    a = b - a
                case "*":
                    a *= b
                case "/":
                    if b == 0:
                        print("не ділиться на 0, будь ласка, введіть наступне число, яке не дорівнює 0.")
                    else:
                        a /= b
                case "!/":
                    if a == 0:
                        print("не можна поділити на 0, результат дорівнює 0, спробуйте іншу дію")
                    else:
                        a = b / a
                case "^":
                    a **= b
                case "!^":
                    a = b ** a
                case "ex":
                    print("\nваш поточний результат = ", a)
                    exit(0)
                case _:
                    print("Це не працює")

            print("\nваш поточний результат = ", a)


        else:
            print("ваш поточний результат = ", a)
            exit(0)


a = enter()
operations(a)