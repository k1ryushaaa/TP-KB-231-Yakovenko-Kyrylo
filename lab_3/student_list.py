from student import student

class StudentList:
    def __init__(self):
        self.students = []  # Список для зберігання студентів.

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        self.students = [s for s in self.students if s.name != name]

    def update_student(self, name, phone=None, faculty=None, address=None):
        for student in self.students:
            if student.name == name:
                if phone:
                    student.phone = phone
                if faculty:
                    student.faculty = faculty
                if address:
                    student.address = address
                return True
        return False

    def print_all_students(self):
        for student in self.students:
            print(student)

    def get_students(self):
        return self.students