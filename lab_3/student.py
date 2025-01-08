class student:
    def __init__(self, name, phone, faculty, address):
        self.name = name
        self.phone = phone
        self.faculty = faculty
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Faculty: {self.faculty}, Address: {self.address}"