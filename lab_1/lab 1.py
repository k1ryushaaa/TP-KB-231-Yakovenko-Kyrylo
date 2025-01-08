


# додав два нових поля факультет та адресу
list = [
    {"name":"Bob", "phone":"0631234567", "faculty":"Science", "address":"Lviv"},
    {"name":"Emma", "phone":"0631234567", "faculty":"Engineering", "address":"Kyiv"},
    {"name":"Jon",  "phone":"0631234567", "faculty":"Math", "address":"Kharkiv"},
    {"name":"Zak",  "phone":"0631234567", "faculty":"Arts", "address":"Odesa"}
]
# додав два поля для виведення нових полів
def printAllList(): 
    for elem in list:
        strForPrint = (
            "Student name: " + elem["name"] +
            ", Phone: " + elem["phone"] +
            ", Faculty: " + elem["faculty"] +
            ", Address: " + elem["address"]
        )
        print(strForPrint)
    return
# додав два поля для додавання нових записів 
def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    faculty = input("Please enter student faculty: ")
    address = input("Please enter student address: ")
    newItem = {"name": name, "phone": phone, "faculty": faculty, "address": address}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Deleting position " + str(deletePosition))
        del list[deletePosition]
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    found = False
    for item in list:
        if name == item["name"]:
            found = True
            # Оновлюємо поля одне за одним
            new_item = input(f"Enter new name (current: {item['name']}): ") or item['name']
            new_phone = input(f"Enter new phone (current: {item['phone']}): ") or item['phone']
            new_faculty = input(f"Enter new faculty (current: {item['faculty']}): ") or item['faculty']
            new_address = input(f"Enter new address (current: {item['address']}): ") or item['address']
            # Оновлюємо дані студента
            item['name'] = new_item
            item['phone'] = new_phone
            item['faculty'] = new_faculty
            item['address'] = new_address
            print(f"Information updated")
            return
    if not found:
        # Якщо студента не знайдено, додаємо новий запис
        print(f"Student {name} not found. Adding new student.")
        new_phone = input("Enter phone: ")
        new_faculty = input("Enter faculty: ")
        new_address = input("Enter address: ")
        new_item = {"name": name, "phone": new_phone, "faculty": new_faculty, "address": new_address}
        # Додаємо новий елемент в список
        list.append(new_item)
        print(f"New student {name} added.")

# додав функцію update
def main():
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated:")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted:")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed:")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")

main()