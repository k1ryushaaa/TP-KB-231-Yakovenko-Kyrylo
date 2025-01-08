from student import student
from student_list import StudentList
from file_manager import FileManager

def main():
    student_list = StudentList()
    student_list.students = FileManager.load_from_csv("students.csv")

    while True:
        choice = input("Choose an action [C create, U update, D delete, P print, S save, X exit]: ").lower()
        if choice == "c":
            name = input("Enter student name: ")
            phone = input("Enter student phone: ")
            faculty = input("Enter student faculty: ")
            address = input("Enter student address: ")
            student_list.add_student(student(name, phone, faculty, address))
            print("New student added.")
        elif choice == "u":
            name = input("Enter the name of the student to update: ")
            phone = input("Enter new phone (or leave blank): ")
            faculty = input("Enter new faculty (or leave blank): ")
            address = input("Enter new address (or leave blank): ")
            if student_list.update_student(name, phone, faculty, address):
                print("Student updated.")
            else:
                print("Student not found.")
        elif choice == "d":
            name = input("Enter the name of the student to delete: ")
            student_list.remove_student(name)
            print("Student deleted if they existed.")
        elif choice == "p":
            student_list.print_all_students()
        elif choice == "s":
            FileManager.save_to_csv("students.csv", student_list.get_students())
            print("Data saved successfully.")
        elif choice == "x":
            FileManager.save_to_csv("students.csv", student_list.get_students())
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()