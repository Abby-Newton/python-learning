# TODO: Create Vehicle base class and Car derived class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def start(self):
        print(f"{self.brand} {self.model} is starting")

# TODO: Create Car class that inherits from Vehicle
class Car(Vehicle):
    def honk(self):
        print("Beep beep!")

# Test:
# my_car = Car("Toyota", "Camry")
# my_car.start() # From Vehicle
# my_car.honk() # From Car

# TODO: Create multiple vehicle types
class Vehicle:
    def __init__(self, brand, model, wheels):
        self.brand = brand
        self.model = model
        self.wheels = wheels

    def start(self):
        print(f"{self.brand} {self.model} is starting")

class Car(Vehicle):
    def __init__(self, brand, model):
        # Cars have 4 wheels
        super().__init__(brand, model, 4)

class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        # Motorcycles have 2 wheels
        super().__init__(brand, model, 2)
        
    def wheelie(self):
        # Only motorcycles can do this
        print(f"{self.brand} {self.model} pops a wheelie!")
# Test different vehicles

# TODO: Create vehicle registration system
class Vehicle:
    vehicle_count = 0 # Class variable
def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self.registration_id = None
    Vehicle.vehicle_count += 1

def register(self, state):
    # Generate registration like "CA-00001"
    number = str(Vehicle.vehicle_count).zfill(5)
    self.registration_id = f"{state}-{number}"
    return self.registration_id

class Car(Vehicle):
    # Add car-specific features
    pass

class Truck(Vehicle):
    def __init__(self, brand, model, cargo_capacity):
        # Initialize parent AND truck-specific attributes
        super().__init__(brand, model)
        self.cargo_capacity = cargo_capacity

# TODO: Override area calculation
class Shape:
    def __init__(self, name):
        self.name = name
        
    def area(self):
        return 0 # Base shape has no area

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    def area(self):
        # Override to return width * height
        return self.width * self.height

# Test:
# rect = Rectangle(5, 3)
# print(f"Area: {rect.area()}")

# TODO: Different grading for different students
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def calculate_grade(self):
        # Regular grading
        if self.score >= 90: return "A"
        elif self.score >= 80: return "B"
        elif self.score >= 70: return "C"
        else: return "F"

class HonorsStudent(Student):
    def calculate_grade(self):
        # Harder grading for honors
        # A: 95+, B: 85+, C: 75+
        if self.score >= 95: return "A"
        elif self.score >= 85: return "B"
        elif self.score >= 75: return "C"
        else: return "F"
# Test both student types

# TODO: Combat system with different character types
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health

    def attack(self):
        return 10 # Base damage
    
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage!")

class Warrior(Character):
    def attack(self):
        # Warriors do 2x damage
        return 20  # 2x damage

    def take_damage(self, amount):
        # Warriors have armor, reduce damage by 3
        reduced = max(amount - 3, 0)
        self.health -= reduced
        print(f"{self.name} takes {reduced} damage (after armor)!")

class Mage(Character):
    def __init__(self, name, health, mana):
        # Initialize parent AND mana
        super().__init__(name, health)
        self.mana = mana

    def attack(self):
        # If has mana, do 3x damage, else normal
        if self.mana > 0:
            self.mana -= 10
            return 30  # 3x damage
        return super().attack()

# TODO: Extend Car class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"Speed: {self.speed} mph")

class SportsCar(Car):
    def __init__(self, brand, model, year, turbo):
        # Call parent init
        # Add turbo attribute
        super().__init__(brand, model, year)
        self.turbo = turbo

    def accelerate(self):
        # If turbo, speed += 20, else normal
        if self.turbo:
            self.speed += 20
        else:
            self.speed += 10
        print(f"Speed: {self.speed} mph")
# Test:
# ferrari = SportsCar("Ferrari", "488", 2023, True)
# ferrari.accelerate()

# TODO: Student hierarchy
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
        self.gpa = 0.0
    
    def enroll(self, course):
        self.courses.append(course)
        print(f"Enrolled in {course}")

class GraduateStudent(Student):
    def __init__(self, name, student_id, thesis_topic):
        # Initialize parent
        # Add thesis_topic
        # Add advisor attribute (starts None)
        super().__init__(name, student_id)
        self.thesis_topic = thesis_topic
        self.advisor = None

    def set_advisor(self, advisor_name):
        # Set the advisor
        self.advisor = advisor_name

    def enroll(self, course):
        # Grad students can only take 500+ level courses
        # Check if course number >= 500
        if int(course) >= 500:
            super().enroll(course)
        else:
            print("Graduate students may only enroll in 500+ level courses.")

# TODO: Three-level inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle: {brand}")

    def start(self):
        print("Starting engine...")

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors
        print(f"Car with {doors} doors")

    def start(self):
        super().start()
        print("Car ready to drive")

class ElectricCar(Car):
    def __init__(self, brand, doors, battery_size):
        # Initialize everything properly
        super().__init__(brand, doors)
        self.battery_size = battery_size
        print(f"ElectricCar with {battery_size} kWh battery")
    
    def start(self):
        # No engine noise for electric!
        # Should print different message
        print("Powering on silently...")

    def charge(self):
        # New method only for electric
        print("Charging battery...")
# Test the chain

# TODO: Person who is both student and employee
class Student:
    def __init__(self):
        self.student_id = "S12345"
        self.gpa = 3.5
    
    def study(self):
        print("Studying hard!")

class Employee:
    def __init__(self):
        self.employee_id = "E67890"
        self.salary = 20000

    def work(self):
        print("Working hard!")

class StudentEmployee(Student, Employee):
    def __init__(self, name):
        # Initialize both parents
        # Add name attribute
        Student.__init__(self)
        Employee.__init__(self)
        self.name = name
# Test:
# person = StudentEmployee("Alex")
# person.study()
# person.work()

# TODO: Vehicle for land and water
class LandVehicle:
    def __init__(self):
        self.speed_on_land = 60
    
    def drive(self):
        print(f"Driving at {self.speed_on_land} mph")

class WaterVehicle:
    def __init__(self):
        self.speed_on_water = 30

    def sail(self):
        print(f"Sailing at {self.speed_on_water} knots")

class AmphibiousVehicle(LandVehicle, WaterVehicle):
    def __init__(self, name):
        # Initialize both
        # Track current mode
        LandVehicle.__init__(self)
        WaterVehicle.__init__(self)
        self.name = name
        self.mode = "land"

    def switch_mode(self):
        # Toggle between land and water
        self.mode = "water" if self.mode == "land" else "land"
        print(f"Switched to {self.mode} mode!")

# TODO: Handle method conflicts
class Camera:
    def __init__(self):
        self.megapixels = 12

    def capture(self):
        return "Photo taken!"

class Phone:
    def __init__(self):
        self.phone_number = "555-1234"
    
    def capture(self): # Same method name!
        return "Screenshot taken!"

class SmartPhone(Phone, Camera):
    def __init__(self, model):
        # Initialize both
        Phone.__init__(self)
        Camera.__init__(self)
        self.model = model

    def capture(self, mode="phone"):
        # Let user choose which capture to use
        if mode == "camera":
            return Camera.capture(self)
        else:
            return Phone.capture(self)
# How to handle conflicting methods?