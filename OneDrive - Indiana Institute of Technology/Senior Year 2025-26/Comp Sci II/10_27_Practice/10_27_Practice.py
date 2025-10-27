# TODO: Create Person class with private _age
class Person:
    def __init__(self, name, age):
        self.name = name # Public
        self._age = age # Make age private
    def get_age(self):
        return self._age
        # Return the private age
        pass
# Test:
person = Person("Bob", 25)
print(person.get_age()) # Should print 25
#person._age = -5 # We shouldn't do this!


# TODO: Add set_age() with validation
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    def get_age(self):
        return self._age
    def set_age(self, new_age):
        # Only allow age between 0 and 150
        # Print error if invalid
        if 0 <= new_age <= 150:
            self._age = new_age
        else:
            print("Error: Age must be between 0 and 150")
# Test:
person = Person("Alice", 25)
person.set_age(30) # Should work
person.set_age(-5) # Should print error


# TODO: Store SSN privately, show only last 4 digits
class Person:
    def __init__(self, name, ssn):
        self.name = name
        self._ssn = ssn
        # Store SSN privately
    def get_masked_ssn(self):
        # Return like: ***-**-6789
        return f"***-**-{self._ssn[-4:]}"
    def verify_ssn(self, ssn_to_check):
        # Return True if matches stored SSN
        return self._ssn == ssn_to_check


# TODO: Make area a property (calculated)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
        # Calculate and return area
        return self.width * self.height
# Test:
rect = Rectangle(5, 3)
print(rect.area) # Should print 15 (no parentheses!)


# TODO: Extract domain from email
class Email:
    def __init__(self, address):
        self.address = address
    @property
    def username(self):
        # Return part before @
        return self.address.split('@')[0]
    @property
    def domain(self):
        # Return part after @
        return self.address.split('@')[1]
# Test:
# email = Email("alice@gmail.com")
# print(email.username) # alice
# print(email.domain) # gmail.com


# TODO: Calculate age from birthdate
from datetime import datetime
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    @property
    def age(self):
        # Calculate age from birth_year
        # Use datetime.now().year
        return datetime.now().year - self.birth_year
    @property
    def can_vote(self):
        # Return True if age >= 18
        return self.age >= 18
# Test:
person = Person("Bob", 2000)
print(f"Age: {person.age}")
print(f"Can vote: {person.can_vote}")


# TODO: Create Score class (0-100 range)
class Score:
    def __init__(self, value=0):
        self._value = 0
        self.value = value # Use setter
    @property
    def value(self):
            return self._value
    @value.setter
    def value(self, new_value):
            # Check if between 0 and 100
            # Set if valid, print error if not
        if 0 <= new_value <= 100:
            self._value = new_value
        else:
            print("Error: Score must be between 0 and 100")
# Test:
score = Score(85)
score.value = 95 # Should work
score.value = 105 # Should print error


# TODO: Username with format checking
import re 
class Username:
    def __init__(self, name):
        self._name = ""
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        # Check: 3-20 characters
        # Check: only letters, numbers, underscore
        # Set if valid
        if not (3 <= len(value) <= 20):
            print("Error: Username must be 3–20 characters long")
        elif not re.match(r'^\w+$', value):
            print("Error: Username can only contain letters, numbers, and underscores")
        else:
            self._name = value
# Test:
user = Username("alice_123") # Should work
user.name = "ab" # Too short
user.name = "alice@123" # Invalid character


# TODO: Password with strength requirements
class Password:
    def __init__(self):
        self._value = None
    @property
    def value(self):
        # Never show actual password!
        return "*" * len(self._value) if self._value else None
    @value.setter
    def value(self, password):
        # Check: at least 8 characters
        # Check: has uppercase
        # Check: has lowercase
        # Check: has number
        # Store if valid
        if len(password) < 8:
            print("Error: Password must be at least 8 characters")
        elif not any(c.isupper() for c in password):
            print("Error: Must contain an uppercase letter")
        elif not any(c.islower() for c in password):
            print("Error: Must contain a lowercase letter")
        elif not any(c.isdigit() for c in password):
            print("Error: Must contain a number")
        else:
            self._value = password
    def verify(self, password):
        # Check if matches stored password
        return self._value == password


# TODO: Create Inventory with protected stock
class Inventory:
    def __init__(self, product_name):
        self.product_name = product_name
        self._stock = 0
    @property
    def stock(self):
        # Return current stock
        return self._stock
    def add_stock(self, quantity):
        # Add to stock if quantity > 0
        if quantity > 0:
            self._stock += quantity
        else:
            print("Error: Quantity must be positive")
    def remove_stock(self, quantity):
        # Remove if enough stock
        if 0 < quantity <= self._stock:
            self._stock -= quantity
        else:
            print("Error: Not enough stock or invalid quantity")
# Test:
inv = Inventory("Widgets")
inv.add_stock(100)
inv.remove_stock(30)
print(f"Stock: {inv.stock}")


# TODO: Add low stock warnings
class Inventory:
    def __init__(self, product_name, reorder_point=10):
        self.product_name = product_name
        self._stock = 0
        self.reorder_point = reorder_point
    @property
    def needs_reorder(self):
        # Return True if stock below reorder_point
        return self._stock < self.reorder_point

    def add_stock(self, quantity):
        if quantity > 0:
            self._stock += quantity
        else:
            print("Error: Quantity must be positive")

    def remove_stock(self, quantity):
        if 0 < quantity <= self._stock:
            self._stock -= quantity
            if self.needs_reorder:
                print(f"⚠️ Warning: {self.product_name} stock low! Consider reordering.")
        else:
            print("Error: Invalid quantity or insufficient stock")
# Add previous methods plus warning in remove_stock


from datetime import datetime
# TODO: Track all inventory changes
from datetime import datetime
class Inventory:
    def __init__(self, product_name):
        self.product_name = product_name
        self._stock = 0
        self._history = []
    @property
    def stock(self):
        return self._stock
    @property
    def history(self):
        # Return copy of history
        return list(self._history)
    def add_stock(self, quantity, reason=""):
        # Add stock and record in history
        # Include timestamp, action, quantity, reason
        if quantity > 0:
            self._stock += quantity
            self._history.append({
                "time": datetime.now(),
                "action": "ADD",
                "quantity": quantity,
                "reason": reason
            })
        else:
            print("Error: Quantity must be positive")
    def remove_stock(self, quantity, reason=""):
        if 0 < quantity <= self._stock:
            self._stock -= quantity
            self._history.append({
                "time": datetime.now(),
                "action": "REMOVE",
                "quantity": quantity,
                "reason": reason
            })
        else:
            print("Error: Invalid quantity or insufficient stock")
    def get_history_summary(self):
        # Return formatted history
        lines = [f"{item['time']} | {item['action']} | {item['quantity']} | {item['reason']}" for item in self._history]
        return "\n".join(lines)