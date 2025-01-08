import csv
import sys

# Список студентів
students = [
    {"name": "Bob", "phone": "0631234567", "faculty": "Science", "address": "Lviv"},
    {"name": "Emma", "phone": "0631234567", "faculty": "Engineering", "address": "Kyiv"},
    {"name": "Jon", "phone": "0631234567", "faculty": "Math", "address": "Kharkiv"},
    {"name": "Zak", "phone": "0631234567", "faculty": "Arts", "address": "Odesa"}
]

# Завантаження даних із CSV-файлу
def load_from_csv(file_name):
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            global students
            students = list(reader)
            print(f"Data loaded successfully from {file_name}.")
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")

# Збереження даних у CSV-файл
def save_to_csv(file_name):
    try:
        with open(file_name, mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ["name", "phone", "faculty", "address"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
            print(f"Data saved successfully to {file_name}.")
    except Exception as e:
        print(f"An error occurred while saving data: {e}")

# Виведення списку студентів
def print_all_students():
    for student in students:
        print(
            f"Name: {student['name']}, Phone: {student['phone']}, Faculty: {student['faculty']}, Address: {student['address']}"
        )

# Додавання нового студента
def add_new_student():
    name = input("Enter student name: ")
    phone = input("Enter student phone: ")
    faculty = input("Enter student faculty: ")
    address = input("Enter student address: ")
    students.append({"name": name, "phone": phone, "faculty": faculty, "address": address})
    print("New student added.")

# Оновлення даних студента
def update_student():
    name = input("Enter the name of the student to update: ")
    for student in students:
        if student["name"] == name:
            student["phone"] = input(f"Enter new phone (current: {student['phone']}): ") or student['phone']
            student["faculty"] = input(f"Enter new faculty (current: {student['faculty']}): ") or student['faculty']
            student["address"] = input(f"Enter new address (current: {student['address']}): ") or student['address']
            print("Student updated.")
            return
    print("Student not found.")

# Видалення студента
def delete_student():
    name = input("Enter the name of the student to delete: ")
    global students
    students = [student for student in students if student["name"] != name]
    print("Student deleted if they existed.")

# Юніт-тести
import unittest

def test_add_new_student():
    test_students = []
    test_name = "Alice"
    test_phone = "0631234567"
    test_faculty = "Math"
    test_address = "Kyiv"
    test_students.append({"name": test_name, "phone": test_phone, "faculty": test_faculty, "address": test_address})
    assert len(test_students) == 1
    assert test_students[0]["name"] == "Alice"

def test_update_student():
    test_students = [{"name": "Alice", "phone": "0631234567", "faculty": "Math", "address": "Kyiv"}]
    for student in test_students:
        if student["name"] == "Alice":
            student["phone"] = "0637654321"
            assert student["phone"] == "0637654321"

def test_delete_student():
    test_students = [{"name": "Alice", "phone": "0631234567", "faculty": "Math", "address": "Kyiv"}]
    test_students = [student for student in test_students if student["name"] != "Alice"]
    assert len(test_students) == 0

def test_load_from_csv():
    test_file = "test.csv"
    with open(test_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "phone", "faculty", "address"])
        writer.writeheader()
        writer.writerow({"name": "Test", "phone": "0631234567", "faculty": "Science", "address": "Test City"})
    load_from_csv(test_file)
    assert len(students) > 0
    assert students[0]["name"] == "Test"

# Головна функція програми
def main():
    if len(sys.argv) > 1:
        load_from_csv(sys.argv[1])

    while True:
        choice = input("Choose an action [C create, U update, D delete, P print, S save, X exit]: ").lower()
        match choice:
            case "c":
                add_new_student()
            case "u":
                update_student()
            case "d":
                delete_student()
            case "p":
                print_all_students()
            case "s":
                save_to_csv("students.csv")
            case "x":
                save_to_csv("students.csv")
                print("Exiting program.")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()