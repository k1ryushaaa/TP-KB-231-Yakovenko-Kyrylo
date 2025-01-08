from student import student
import csv
class FileManager:
    @staticmethod
    def load_from_csv(file_name):
        students = []
        try:
            with open(file_name, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append(student(row['name'], row['phone'], row['faculty'], row['address']))
        except FileNotFoundError:
            print(f"File {file_name} not found.")
        return students

    @staticmethod
    def save_to_csv(file_name, students):
        try:
            with open(file_name, mode='w', encoding='utf-8', newline='') as file:
                fieldnames = ['name', 'phone', 'faculty', 'address']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for student in students:
                    writer.writerow({
                        'name': student.name,
                        'phone': student.phone,
                        'faculty': student.faculty,
                        'address': student.address
                    })
        except Exception as e:
            print(f"An error occurred while saving data: {e}")