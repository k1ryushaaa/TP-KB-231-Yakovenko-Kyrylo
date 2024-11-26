def sort_pos(list, item):
    insert_pos = 0
    for elem in list:
        if item > elem:
            insert_pos += 1
        else:
            break
    return insert_pos

names_list = ["Андрій", "Олександр", "Кирило", "Микола", "Дмитро" ]

print(f"Останні імена: {names_list}")

name = input("Введіть нове ім’я, щоб отримати позицію для його вставлення: ")
pos = sort_pos(names_list, name)

if pos == 0:
    print("Це ім'я буде вставлено першим")
elif pos == len(names_list):
    print("Це ім'я буде вставлено останнім")
else:
    print(f"Ця назва буде вставлена ​​між {names_list[pos - 1]} і {names_list[pos]}.")