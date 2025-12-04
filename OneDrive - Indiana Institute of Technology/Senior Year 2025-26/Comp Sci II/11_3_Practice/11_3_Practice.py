# TODO: Different shapes, same draw() method
class Shape:
def __init__(self, color):
self.color = color
def draw(self):
pass
class Circle(Shape):
def draw(self):
# Return "Drawing a [color] circle"
pass
class Square(Shape):
def draw(self):
# Return "Drawing a [color] square"
pass
# Test:
# shapes = [Circle("red"), Square("blue"), Circle("green")]
# for shape in shapes:
# print(shape.draw())

# TODO: Different payment methods
class Payment:
def __init__(self, amount):
self.amount = amount
def process(self):
pass
class CreditCard(Payment):
def __init__(self, amount, card_number):
super().__init__(amount)
self.card_number = card_number
def process(self):
# Return "Processing $X via credit card ending in [last 4 digits]"
pass
class PayPal(Payment):
def __init__(self, amount, email):
super().__init__(amount)
self.email = email
def process(self):
# Return "Processing $X via PayPal account [email]"
pass
# Process different payments the same way

# TODO: Save/load for different file types
class FileHandler:
def __init__(self, filename):
self.filename = filename
self.data = None
def save(self, content):
pass
def load(self):
pass
class TextFile(FileHandler):
def save(self, content):
# Print "Saving text to [filename].txt"
self.data = content
def load(self):
# Return the saved data
pass
class JsonFile(FileHandler):
def save(self, content):
# Print "Converting to JSON and saving to [filename].json"
pass
class CsvFile(FileHandler):
# Implement CSV saving/loading
pass
# Use any file type the same way!

from abc import ABC, abstractmethod
# TODO: Create abstract Vehicle class
class Vehicle(ABC):
def __init__(self, brand):
self.brand = brand
@abstractmethod
def start(self):
# Force all vehicles to have start()
pass
class Car(Vehicle):
def start(self):
# Return "Car engine starting..."
pass
# Test:
# car = Car("Toyota")
# print(car.start())
# vehicle = Vehicle("Generic") # Should error!

# TODO: Abstract database interface
from abc import ABC, abstractmethod
class DatabaseConnection(ABC):
def __init__(self, host):
self.host = host
self.connected = False
@abstractmethod
def connect(self):
pass
@abstractmethod
def disconnect(self):
pass
@abstractmethod
def execute_query(self, query):
pass
class MySQLConnection(DatabaseConnection):
# Implement all abstract methods
pass
class PostgresConnection(DatabaseConnection):
# Implement all abstract methods
pass

# TODO: Create plugin architecture
from abc import ABC, abstractmethod
class Plugin(ABC):
def __init__(self, name, version):
self.name = name
self.version = version
self.enabled = False
@abstractmethod
def activate(self):
"""Called when plugin is enabled"""
pass
@abstractmethod
def deactivate(self):
"""Called when plugin is disabled"""
pass
@abstractmethod
def process(self, data):
"""Main plugin functionality"""
pass
# Create different plugin types
class SpellChecker(Plugin):
# Implement spell checking
pass
class AutoSave(Plugin):
# Implement auto-saving
pass

# TODO: Create objects with compatible methods
class Calculator:
def compute(self, x, y):
return x + y
class ScientificCalculator: # No inheritance!
def compute(self, x, y):
# Return x * y instead
pass
def process_numbers(processor, a, b):
# Works with anything that has compute()
result = processor.compute(a, b)
print(f"Result: {result}")
# Test both calculators

# TODO: Make custom iterable class
class Countdown:
def __init__(self, start):
self.start = start
def __iter__(self):
# Return self
pass
def __next__(self):
# Count down to 0
# Raise StopIteration when done
pass
# Test:
# for num in Countdown(5):
# print(num) # Should print 5, 4, 3, 2, 1, 0

# TODO: Create context manager without inheritance
class Timer:
def __enter__(self):
# Start timing
import time
self.start = time.time()
print("Timer started...")
return self
def __exit__(self, *args):
# Stop timing and print duration
pass
def checkpoint(self):
# Print time since start
pass
# Use with 'with' statement:
# with Timer() as t:
# time.sleep(1)
# t.checkpoint()
# time.sleep(1)

# TODO: Different notification methods
class NotificationStrategy:
def notify(self, message):
pass
class EmailNotification(NotificationStrategy):
def notify(self, message):
# Print "Email sent: [message]"
pass
class SMSNotification(NotificationStrategy):
# Implement SMS notification
pass
class App:
def __init__(self, notifier):
self.notifier = notifier
def alert_user(self, message):
# Use the notifier
pass
# Test switching strategies

# TODO: Export data in different formats
class DataExporter:
def export(self, data):
pass
class CSVExporter(DataExporter):
def export(self, data):
# Return comma-separated string
pass
class JSONExporter(DataExporter):
def export(self, data):
# Return JSON-like string
pass
class HTMLExporter(DataExporter):
# Create HTML table
pass
# Create report generator that can switch formats

# TODO: Different AI behaviors
class AIStrategy:
def make_move(self, game_state):
pass
class AggressiveAI(AIStrategy):
def make_move(self, game_state):
# Always attack
pass
class DefensiveAI(AIStrategy):
def make_move(self, game_state):
# Always defend
pass
class RandomAI(AIStrategy):
def make_move(self, game_state):
# Random choice
pass
class GameCharacter:
def __init__(self, name, strategy):
self.name = name
self.strategy = strategy
self.health = 100
def play_turn(self, game_state):
# Use strategy to decide action
pass
def change_strategy(self, new_strategy):
# Switch AI behavior mid-game!
pass