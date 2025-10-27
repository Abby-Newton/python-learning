# TODO: Create a Book class with title and author
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
# Test it:
my_book = Book("Python Basics", "Jane Doe")
print(my_book.title) # Should print: Python Basics


# TODO: Add display_info() method to Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")


# TODO: Create multiple books and store in a list
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")
# Create a library (list of books)
library = [
    Book("Python Basics", "Jane Doe"),
    Book("Learning AI", "John Smith"),
    Book("Data Science 101", "Alice Johnson")
]
# Add at least 3 books to library
# Print all book titles in library
for book in library:
    print(book.title)


# TODO: Create Car with make, model, year
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
# Test:
my_car = Car("Toyota", "Camry", 2020)
print(f"{my_car.year} {my_car.make} {my_car.model}")


# TODO: Add mileage and drive() method
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
    def drive(self, miles):
        self.mileage += miles
        print(f"Driven {miles} miles. Total mileage: {self.mileage} miles.")


# TODO: Add fuel tank and consumption
class Car:
    def __init__(self, make, model, year, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
        self.mpg = mpg
        self.fuel = 0
    def add_fuel(self, gallons):
        self.fuel += gallons
        print(f"Added {gallons} gallons. Fuel in tank: {self.fuel: .2f} gallons.")
    def drive(self, miles):
        # Calculate fuel needed
        # Check if enough fuel
        # Update mileage and fuel
        fuel_needed = miles / self.mpg
        if fuel_needed > self.fuel:
            print("Not enough fiel! Please refuel.")
        else:
            self.mileage += miles
            self.fuel -= fuel_needed
            print(f"Drove {miles} miles. Total mileage: {self.mileage} miles.")
            print(f"Remaining fuel: {self.fuel: .2f} gallons.")
            
my_car = Car("Honda", "Civic", 2022, 30)
my_car.add_fuel(10)
my_car.drive(100)
my_car.drive(250)


# TODO: Create Teacher class that holds students
class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []
    # Add method to add a student
    def add_student(self, student_name):
        self.students.append(student_name)
# Test:
teacher = Teacher("Mr. Johnson")
teacher.add_student("Alice")
print(teacher.students)


# TODO: Add remove_student method
class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []
    def add_student(self, student_name):
        self.students.append(student_name)
    def remove_student(self, student_name):
        # Check if student exists first
        # Remove if found
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"{student_name} removed from the class.")
        else:
            print(f"{student_name} not found in the class.")
teacher = Teacher("Mr. Johnson")
teacher.add_student("Alice")
teacher.add_student("Bob")
print(teacher.students)   # ['Alice', 'Bob']
teacher.remove_student("Alice")
print(teacher.students)   # ['Bob']
teacher.remove_student("Charlie")  # Not found


# TODO: Track grades for each student
class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = {} # Dictionary: name -> grade
    def add_student(self, name, initial_grade=0):
        if name not in self.students:
            self.students[name] = initial_grade
            print(f"{name} added with initial grade {initial_grade}")
        else:
            print(f"{name} is already in the class.")
    def grade_student(self, name, grade):
        # Update grade if student exists.
        if name in self.students:
            self.students[name] = grade
            print(f"{name}'s grade updated to {grade}.")
        else:
            print(f"{name} not found in the class.")
    def class_average(self):
        # Calculate and return average grade
        if not self.students:
            return 0
        total = sum(self.students.values())
        avg = total / len(self.students)
        return round(avg, 2)
teacher = Teacher("Ms. Carter")
teacher.add_student("Alice", 85)
teacher.add_student("Bob", 90)
teacher.add_student("Charlie", 70)
teacher.grade_student("Charlie", 80)
print(teacher.students)
# Expected: {'Alice': 85, 'Bob': 90, 'Charlie': 80}
print("Class average:", teacher.class_average())
# Expected: Class average: 85.0