class Vehicle:
    def start(self):
        return "Vehicle starting"
class Car(Vehicle):
    def start(self):
        return "Car starting"
class Boat(Vehicle):
    def start(self):
        return "Boat starting"
class AmphibiousCar(Car, Boat):
    pass # Which start() method?
# Python uses C3 linearization algorithm
amph = AmphibiousCar()
print(amph.start()) # "Car starting" - left-to-right priority
print(AmphibiousCar.__mro__) # Shows method resolution order

class Professor:
    def work(self):
        return "Teaching"
class Researcher:
    def work(self):
        return "Researching"
class ProfessorResearcher(Professor, Researcher):
    def schedule(self):
        # Explicitly choose which parent's method
        teaching = Professor.work(self)
        research = Researcher.work(self)
        return f"Morning: {teaching}, Afternoon: {research}"

# Bad: Multiple responsibilities
class Student:
    def calculate_gpa(self): pass
    def save_to_database(self): pass
    def send_email(self): pass
# Good: Separated concerns
class Student:
    def calculate_gpa(self): pass
class StudentRepository:
    def save(self, student): pass
class EmailService:
    def send_to_student(self, student): pass

# Extend behavior without changing existing code
class DiscountCalculator(ABC):
    @abstractmethod
    def calculate(self, amount): pass
class StudentDiscount(DiscountCalculator):
    def calculate(self, amount):
        return amount * 0.8 # 20% off
class SeniorDiscount(DiscountCalculator):
    def calculate(self, amount):
        return amount * 0.85 # 15% off

# Violation - Square changes Rectangle's behavior
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, width):
        self.width = width
class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width # Breaks Rectangle's contract!
# Better design - separate hierarchies
class Shape(ABC):
    @abstractmethod
    def area(self): pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

# Instead of one large interface
class Worker:
    def work(self): pass
    def eat(self): pass
    def sleep(self): pass
# Split into focused interfaces
class Workable:
    def work(self): pass
class Feedable:
    def eat(self): pass
class Human(Workable, Feedable):
    def work(self): return "Working"
    def eat(self): return "Eating"
class Robot(Workable): # Robots don't eat!
    def work(self): return "Computing"

# Depend on interface, not specific implementation
class NotificationService(ABC):
    @abstractmethod
    def send(self, message): pass
class EmailNotifier(NotificationService):
    def send(self, message):
        print(f"Email: {message}")
class SMSNotifier(NotificationService):
    def send(self, message):
        print(f"SMS: {message}")
class AlertSystem:
    def __init__(self, notifier: NotificationService):
        self.notifier = notifier # Depends on abstraction
    def alert(self, message):
        self.notifier.send(message)