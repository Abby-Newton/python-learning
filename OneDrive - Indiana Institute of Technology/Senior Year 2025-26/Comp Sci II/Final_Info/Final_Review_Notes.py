"""
1. Dictionaries
"""
# Creating Dictionaries
# Method 1: Literal syntax
student = {'name': 'Alice', 'age': 20}

# Method 2: dict() constructor
student = dict(name='Alice', age=20)
student = dict([('name', 'Alice'), ('age', 20)])

# Method 3: Dictionary comprehension
squares = {x: x**2 for x in range(5)}


# Accessing Dictionary Elements
# Direct access (raises KeyError if missing)
value = student['name']

# Safe access with get()
value = student.get('grade', 'N/A') # Returns 'N/A' if missing

# Check if key exists
if 'name' in student:
    print(student['name'])


# Modifying Dictionaries
# Add/update
student['grade'] = 'A'
student.update({'major': 'CS', 'year': 2})

# Remove
del student['age']
value = student.pop('grade') # Returns and removes
item = student.popitem() # Removes arbitrary item


# Keys() Method
# Returns view object of keys
keys_view = student.keys()
# Supports set operations
common_keys = dict1.keys() & dict2.keys()

# Values() Method
# Returns view object of values
values_view = student.values()
# Can contain duplicates
total = sum(grades.values())


# Items() Method
# Returns view of (key, value) tuples
items_view = student.items()
for key, value in student.items():
    print(f"{key}: {value}")


# Iteration Patterns
# Iterate over keys (default)
for key in student:
    print(key)

# Iterate over values
for value in student.values():
    print(value)

# Iterate over items
for key, value in student.items():
    print(f"{key}: {value}")


# Conditional Processing
# Filter dictionary
high_scores = {k: v for k, v in grades.items() if v >= 90}


# Nested Dictionary Iteration
for category, items in nested_dict.items():
    for item_name, details in items.items():
        process(category, item_name, details)


# Dictionary Transformation
# Filter by keys
filtered = {k: v for k, v in data.items() if condition(k)}

# Transform values
transformed = {k: transform(v) for k, v in data.items()}

# Invert dictionary
inverted = {v: k for k, v in data.items()}


"""
2. Sets
"""
# Python Set Types
# Mutable set
my_set = {1, 2, 3}
my_set = set([1, 2, 3])

# Immutable frozenset
frozen = frozenset([1, 2, 3])


# Set Comprehensions
squares = {x**2 for x in range(10)}
evens = {x for x in range(20) if x % 2 == 0}


# Creating and Modifying Sets
# Create
s = set()
s = {1, 2, 3}

# Add elements
s.add(4)
s.update([5, 6, 7])

# Remove elements
s.remove(3) # Raises KeyError if not found
s.discard(3) # No error if not found
s.pop() # Remove arbitrary element


# Mathematical Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union: A ∪ B
union = A | B # {1, 2, 3, 4, 5, 6}

# Intersection: A ∩ B
intersection = A & B # {3, 4}

# Difference: A - B
difference = A - B # {1, 2}

# Symmetric difference: A △ B
sym_diff = A ^ B # {1, 2, 5, 6}

# Subset/Superset
A.issubset(B) # False
A.issuperset(B) # False


# Set Methods
# Membership
if 3 in my_set:
print("Found")

# Properties
len(my_set) # Size
my_set.isdisjoint(other_set) # No common elements



"""
3. NumPy
"""
# Creating NumPy Arrays
import numpy as np

# From lists
arr = np.array([1, 2, 3])
arr2d = np.array([[1, 2], [3, 4]])

# Special arrays
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
identity = np.eye(3)
range_arr = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)


# Array Attributes
arr.shape # Dimensions
arr.size # Total elements
arr.dtype # Data type
arr.ndim # Number of dimensions


# NumPy Data Types
# Specify dtype
arr = np.array([1, 2, 3], dtype=np.float64)

# Type conversion
arr.astype(np.int32)


# Vectorization
# Element-wise operations without loops
arr = np.array([1, 2, 3, 4])
result = arr * 2 # [2, 4, 6, 8]


# Arithmetic Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b # Element-wise addition
a * b # Element-wise multiplication
a @ b # Dot product


# Universal Functions
np.sqrt(arr)
np.exp(arr)
np.sin(arr)
np.log(arr)


# Aggregate Functions
arr.sum()
arr.mean()
arr.std()
arr.min()
arr.max()
arr.argmax() # Index of maximum


# Array Indexing and Slicing
# 1D array
arr[0] # First element
arr[-1] # Last element
arr[1:4] # Slice

# 2D array
arr2d[0, 1] # Row 0, column 1
arr2d[:, 1] # All rows, column 1
arr2d[1, :] # Row 1, all columns


# Broadcasting
# Different shapes can be operated together
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr + 10 # Adds 10 to each element

# Broadcasting rules:
# 1. Dimensions are aligned right to left
# 2. Dimensions of size 1 can stretch


# Statistical Operations
np.median(arr)
np.percentile(arr, 75)
np.corrcoef(x, y) # Correlation


# Working with 2D Arrays
# Matrix operations
arr.T # Transpose
np.linalg.inv(arr) # Inverse
np.linalg.det(arr) # Determinant


# Comparing Arrays
# Element-wise comparison
arr1 == arr2
arr > 5

# Finding values
np.where(arr > 5) # Indices where condition is True
np.argwhere(arr > 5) # Indices as array




"""
4. Regular Expressions
"""
# Basic Patterns
import re

# Literal matching
re.search('hello', text)

# Case insensitive
re.search('hello', text, re.IGNORECASE)


# Character Classes
[abc] # Match a, b, or c
[^abc] # Match anything except a, b, c
[a-z] # Range: lowercase letters
[A-Za-z] # All letters
[0-9] # Digits


# Shorthand Character Classes
\d # Digit [0-9]
\D # Non-digit [^0-9]
\w # Word character [a-zA-Z0-9_]
\W # Non-word character
\s # Whitespace
\S # Non-whitespace


# Anchors
^ # Start of string
$ # End of string
\b # Word boundary


# Dot
. # Any character except newline


# Repetition Metacharacters
* # 0 or more
+ # 1 or more
? # 0 or 1
{n} # Exactly n
{n,} # n or more
{n,m} # Between n and m


# Grouping and Capturing
# Groups
(abc) # Capturing group
(?:abc) # Non-capturing group
(?P<name>pattern) # Named group

# Backreferences
\1, \2 # Reference captured groups


# Alternation
cat|dog # Match cat or dog


# re.match()
# Match at beginning of string
match = re.match(r'\d+', '123abc')

if match:
    print(match.group()) # '123'


# re.search()
# Search anywhere in string
match = re.search(r'\d+', 'abc123def')
if match:
    print(match.group()) # '123'



# re.findall()
# Find all matches
matches = re.findall(r'\d+', 'a1b22c333')
# Returns: ['1', '22', '333']


# re.finditer()
# Iterator of match objects
for match in re.finditer(r'\d+', 'a1b22c333'):
    print(match.group(), match.span())


# re.sub()
# Replace matches
result = re.sub(r'\d+', 'X', 'a1b22c333')
# Returns: 'aXbXcX'


# Compilation for Efficiency
# Compile once, use many times
pattern = re.compile(r'\d+')
matches = pattern.findall(text)



"""
5. Advanced String Operations
"""
# String Methods - Case and Cleaning
text.upper() # UPPERCASE
text.lower() # lowercase
text.title() # Title Case
text.capitalize() # First letter only
text.swapcase() # sWAP cASE

text.strip() # Remove whitespace both ends
text.lstrip() # Remove from left
text.rstrip() # Remove from right



# String Searching
'word' in text # Check if contains
text.find('word') # Index or -1
text.index('word') # Index or raises error
text.count('word') # Count occurrences
text.startswith('pre') # Check prefix
text.endswith('suf') # Check suffix


# String Checking
text.isalpha() # Only letters?
text.isdigit() # Only digits?
text.isalnum() # Letters or numbers?
text.isspace() # Only whitespace?
text.isupper() # All uppercase?
text.islower() # All lowercase?


# String replacement and Splitting
# Replace
text.replace('old', 'new')
text.replace('old', 'new', 1) # Replace first only

# Split
text.split() # Split by whitespace
text.split(',') # Split by comma
text.splitlines() # Split by newlines

# Join
', '.join(['a', 'b', 'c']) # 'a, b, c'


# String Formatting
# F-strings (recommended)
name = 'Alice'
age = 25
f"Name: {name}, Age: {age}"
f"Price: ${price:.2f}" # 2 decimal places

# Format method
"Name: {}, Age: {}".format(name, age)

# Alignment and padding
f"{text:>10}" # Right align
f"{text:<10}" # Left align
f"{text:^10}" # Center
f"{text:*^10}" # Center with fill


# String Slicing and Indexing
text[0] # First character
text[-1] # Last character
text[1:4] # Characters 1-3
text[:5] # First 5 characters
text[5:] # From character 5 to end
text[::2] # Every second character
text[::-1] # Reverse string



"""
6. File I/O
"""
# Python File Types and Objects
# File object represents open file
# Text mode vs Binary mode
# Buffered vs Unbuffered


# Text File Processing
# Opening files
file = open('file.txt', 'r') # Read mode
file = open('file.txt', 'w') # Write mode (overwrites)
file = open('file.txt', 'a') # Append mode

# Reading
content = file.read() # Read entire file
line = file.readline() # Read one line
lines = file.readlines() # Read all lines into list

# Writing
file.write('text')
file.writelines(['line1\n', 'line2\n'])

# Always close!
file.close()


# With Statements (Context Managers)
# Automatic file closing
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed after block


# JSON
import json

# Write JSON
data = {'name': 'Alice', 'age': 25}
with open('data.json', 'w') as f:
    json.dump(data, f)
    
# Read JSON
with open('data.json', 'r') as f:
    data = json.load(f)


# Pickle (Binary Serialization)
import pickle

# Save object
with open('data.pkl', 'wb') as f:
    pickle.dump(obj, f)

# Load object
with open('data.pkl', 'rb') as f:
    obj = pickle.load(f)


# File Paths
import os

# Path operations
os.path.join('dir', 'file.txt')
os.path.exists('file.txt')
os.path.isfile('file.txt')
os.path.isdir('directory')
os.path.basename('/path/to/file.txt') # 'file.txt'
os.path.dirname('/path/to/file.txt') # '/path/to'


# File System Operations
import os

os.listdir('.') # List directory contents
os.mkdir('new_dir') # Create directory
os.remove('file.txt') # Delete file
os.rename('old.txt', 'new.txt') # Rename
os.getcwd() # Current working directory
os.chdir('/path/to/dir') # Change directory



"""
7. Object-Oriented Programming
"""
# Class Definition
class Student:
    # Class variable (shared by all instances)
    school = "University"

    # Constructor
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    # Instance method
    def introduce(self):
        return f"I'm {self.name}, {self.age} years old"

    # Destructor (rarely used)
    def __del__(self):
        print(f"{self.name} object destroyed")

# Instantiation
student = Student("Alice", 20)


# Public vs Private Attributes
class BankAccount:
    def __init__(self, balance):
        self.public_var = "Anyone can access"
        self._protected = "Convention: internal use"
        self.__private = "Name mangled: harder to access"


# Property Decorators
class Person:
    def __init__(self, age):
        self._age = age

@property
def age(self): # Getter
    return self._age

@age.setter
def age(self, value): # Setter
    if value < 0:
        raise ValueError("Age cannot be negative")
    self._age = value

@age.deleter
def age(self): # Deleter
    del self._age

# Usage
person = Person(25)
print(person.age) # Calls getter
person.age = 26 # Calls setter


# Base and Derived Classes
class Animal: # Base/Parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal): # Derived/Child class
    def speak(self): # Method overriding
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Super() Function
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) # Call parent constructor
        self.student_id = student_id


# Multiple Inheritance
class A:
    pass

class B:
    pass

class C(A, B): # Inherits from both A and B
    pass


# Polymorphic Behavior
# Different classes, same interface
def make_sound(animal):
    return animal.speak()

dog = Dog("Rex")
cat = Cat("Fluffy")

make_sound(dog) # "Rex says Woof!"
make_sound(cat) # "Fluffy says Meow!"


# Abstract Base Classes
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self): # Must implement
        return 3.14159 * self.radius ** 2


# Duck Typing
# If it walks like a duck and quacks like a duck...
# Python doesn't check type, just checks if method exists


# Class Methods and Static Methods
class MyClass:
    class_var = 0

    @classmethod
    def class_method(cls):
        # Access class variables
        return cls.class_var

    @staticmethod
    def static_method():
        # No access to cls or self
        return "I'm independent"

    def instance_method(self):
        # Normal method
        return self


# Factory Methods
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = date_string.split('-')
        return cls(int(year), int(month), int(day))

# Usage
date = Date.from_string('2024-12-25')


# Special Methods 
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Arithmetic operators
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Comparison operators
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # Container protocols
    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError



"""
8. Exceptions
"""
# Python's Exception Hierarchy
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ArithmeticError
    │ ├── ZeroDivisionError
    │ └── OverflowError
    ├── LookupError
    │ ├── IndexError
    │ └── KeyError
    ├── TypeError
    ├── ValueError
    └── IOError/OSError


# Try-Except-Else_Finally Pattern
try:
    # Code that might raise exception
    result = risky_operation()
except ValueError as e:
    # Handle specific exception
    print(f"ValueError: {e}")
except (TypeError, KeyError) as e:
    # Handle multiple exceptions
    print(f"Type or Key error: {e}")
except Exception as e:
    # Catch all other exceptions
    print(f"Unexpected error: {e}")
else:
    # Runs if no exception occurred
    print("Success!")
finally:
    # Always runs, used for cleanup
    print("Cleaning up...")


# Raising Exceptions
# Raise built-in exception
if value < 0:
    raise ValueError("Value must be non-negative")

# Re-raise exception
try:
    dangerous_operation()
except Exception:
    log_error()
    raise # Re-raises the same exception


# Custom Exceptions
class CustomError(Exception):
    """Custom exception class"""
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code

# Usage
raise CustomError("Something went wrong", code=404)


# Context Managers For Cleanup
# Using with statement
with open('file.txt') as f:
    content = f.read()
# File automatically closed

# Custom context manager
from contextlib import contextmanager

@contextmanager
def managed_resource():
    resource = acquire_resource()
    try:
        yield resource
    finally:
        release_resource(resource)



"""
9. Recursion
"""
# Introduction via Factorial
def factorial(n):
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)


# Visualizing the Call Stack
factorial(4)
├── 4 * factorial(3)
│ ├── 3 * factorial(2)
│ │ ├── 2 * factorial(1)
│ │ │ └── 1 (base case)
│ │ └── 2 * 1 = 2
│ └── 3 * 2 = 6
└── 4 * 6 = 24


# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# Binary Search 
def binary_search(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)


# Divide and Conquer
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# Dynamic Programming
# Memoization
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]



"""
10. Advanced Functions
"""
# Assigned to Variables
def greet(name):
    return f"Hello, {name}"

my_func = greet # Function assigned to variable
print(my_func("Alice")) # "Hello, Alice"


# Passed as Arguments
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

result = apply_twice(add_five, 10) # 20


# Functions as Return Values 
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times_two = make_multiplier(2)
print(times_two(5)) # 10


# Stored in Data Structures
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y
}

result = operations['add'](5, 3) # 8


# map()
# Apply function to all elements
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]


# filter()
# Keep elements that satisfy condition
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6]


# reduce()
from functools import reduce

# Aggregate elements
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
# 120


# zip()
# Combine iterables
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
combined = list(zip(names, ages))
# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


# Lambda Functions
# Anonymous functions
square = lambda x: x**2
add = lambda x, y: x + y

# Often used with higher-order functions
sorted_list = sorted(items, key=lambda x: x.price)


# Comprehensions vs Functional Style
# List comprehension
squares = [x**2 for x in range(10)]

# Functional style
squares = list(map(lambda x: x**2, range(10)))

# Dict comprehension
square_dict = {x: x**2 for x in range(5)}

# Set comprehension
unique_squares = {x**2 for x in [-2, -1, 0, 1, 2]}


# Generator Functions with Yield
def count_up_to(n):
    i = 1
    while i <= n:
        yield i # Produces value and pauses
        i += 1

# Usage
for num in count_up_to(5):
    print(num) # 1, 2, 3, 4, 5


# Generator Expressions
# Like list comprehension but lazy evaluation
gen = (x**2 for x in range(1000000)) # Doesn't create list
first_five = [next(gen) for _ in range(5)]


# Yield From
def flatten(nested):
    for sublist in nested:
        yield from sublist # Delegates to another generator

# Usage
nested = [[1, 2], [3, 4], [5, 6]]
flat = list(flatten(nested)) # [1, 2, 3, 4, 5, 6]


# Sending Values to Gnerators
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

gen = accumulator()
next(gen) # Initialize
gen.send(10) # Returns 10
gen.send(5) # Returns 15


# Args and Kwargs
def flexible_function(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")

flexible_function(1, 2, 3, name='Alice', age=25)
# Positional: (1, 2, 3)
# Keyword: {'name': 'Alice', 'age': 25}

# Unpacking
def func(a, b, c):
    return a + b + c

args = [1, 2, 3]
result = func(*args) # Unpacks list

kwargs = {'a': 1, 'b': 2, 'c': 3}
result = func(**kwargs) # Unpacks dict


# Type Hints and Annotations
def greet(name: str) -> str:
    return f"Hello, {name}"

def calculate(x: float, y: float) -> float:
    return x + y

from typing import List, Dict, Optional

def process(items: List[int]) -> Dict[str, int]:
    return {'sum': sum(items), 'count': len(items)}

def find(key: str) -> Optional[str]:
    # Returns str or None
    return database.get(key)


# Context Managers as Functions
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Elapsed: {end - start:.2f} seconds")

# Usage
with timer():
    # Code to time
    time.sleep(1)


# Function Factories
def make_power_func(n):
    """Factory that creates power functions"""
    def power(x):
        return x ** n
    return power

square = make_power_func(2)
cube = make_power_func(3)

print(square(5)) # 25
print(cube(5)) # 125