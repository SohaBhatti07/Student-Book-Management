class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student(self):
        self.display_person()
        print("Student ID:", self.student_id)


class Book:
    def __init__(self, title, author):
        self.__title = title     
        self.__author = author    

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def display_book(self):
        print("Book Title:", self.get_title())
        print("Author:", self.get_author())


s1 = Student("Ali", 20, 101)

b1 = Book("Python Basics", "John Smith")

print("Student Information")
s1.display_student()

print("\nBook Information")
b1.display_book()