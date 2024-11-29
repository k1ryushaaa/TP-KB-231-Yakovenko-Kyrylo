import random

def enter():
    while True:
        try:
            p = int(input("Введіть номер, який відповідає вашому вибору \n1 — Stone, 2 — Scissors, 3 — Paper\n"))
        except:
            print("\n")
            continue
        if (0 < p < 4):
            return p - 1

def play(p):
    comp = random.randint(0, 2)
    res_list = ["00", "01", "02", "11", "12", "10", "22", "20", "21"]
    res = res_list.index(str(p) + str(comp)) % 3
    match res:
        case 0:
            draw(p)
               
        case 1:
            win(p, comp)
            
        case 2:
            loss(p, comp)

def win(p, comp):
        print(f"Ти виграв! Ви обрали {choice_list[p]}, комп'ютер вибрав {choice_list[comp]}")

def loss(p, comp):
        print(f"Ти програв. Ви обрали {choice_list[p]}, комп'ютер вибрав {choice_list[comp]}")

def draw(p):
        print(f"Нічия. Ви з комп'ютером вибрали {choice_list[p]}")


choice_list = ["stone", "scissors", "paper"]
p = enter()
play(p)