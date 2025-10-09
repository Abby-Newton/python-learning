'''
DICTIONARIES
'''
# Dictionary structure: {key: value}
phone_book = {"Alice": "555-1234", "Bob": "555-5678"}

# Curly Braces
# Empty dictionary
empty_dict = {}
# Dictionary with values
grades = {"Math": 90, "English": 85, "Science": 92}

# dict() function
# Empty dictionary
empty_dict = dict()
# From pairs
grades = dict([("Math", 90), ("English", 85)])

# Using get()
grades = {"Math": 90, "English": 85}
# Safe - returns None if key doesn't exist
math_grade = grades.get("Math") # Returns 90
history_grade = grades.get("History") # Returns None (no error!)
# With default value
history_grade = grades.get("History", 0) # Returns 0 instead of None

# Using Square Brackets
grades = {"Math": 90, "English": 85}
# Direct access
math_grade = grades["Math"] # Returns 90
history_grade = grades["History"] # ERROR! KeyError!

# Adding and Updating Values 
grades = {"Math": 90}
# Add new subject
grades["Science"] = 88
# Update existing
grades["Math"] = 95
# Now grades = {"Math": 95, "Science": 88}

# Removing Items
grades = {"Math": 90, "English": 85, "Science": 88}
# Remove with del
del grades["Science"]
# Remove with pop (returns the value)
english_grade = grades.pop("English") # Returns 85
# Remove last item with popitem
last_item = grades.popitem() # Returns tuple like ("Math", 90)

# keys(), values(), items()
student = {"name": "Alice", "age": 20, "grade": "A"}
# Get all keys
all_keys = student.keys() # dict_keys(['name', 'age', 'grade'])
key_list = list(student.keys()) # Convert to list
# Get all values
all_values = student.values() # dict_values(['Alice', 20, 'A'])
# Get key-value pairs
all_items = student.items() # dict_items([('name', 'Alice'), ...])

# Looping Through Dictionaries
grades = {"Math": 90, "English": 85, "Science": 88}
# Loop through keys (default)
for subject in grades:
    print(f"{subject}: {grades[subject]}")
# Loop through values
for grade in grades.values():
    print(f"Grade: {grade}")
# Loop through key-value pairs (MOST USEFUL!)
for subject, grade in grades.items():
    print(f"{subject}: {grade}")

# Dictionary Patterns Counting
# Count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
# Result: {"apple": 3, "banana": 2, "cherry": 1}

# Dictionary Patterns Grouping
# Group students by grade
students = [
{"name": "Alice", "grade": "A"},
{"name": "Bob", "grade": "B"},
{"name": "Charlie", "grade": "A"}
]
grouped = {}
for student in students:
    grade = student["grade"]
    if grade not in grouped:
        grouped[grade] = []
    grouped[grade].append(student["name"])
# Result: {"A": ["Alice", "Charlie"], "B": ["Bob"]}

# Dictionary Patterns Default Values
# Using get() with default
inventory = {"apples": 5, "bananas": 3}
# Check stock with default
apples = inventory.get("apples", 0) # Returns 5
oranges = inventory.get("oranges", 0) # Returns 0 (not in dict)



'''
SETS
'''
# Set automatically removes duplicates
numbers = {1, 2, 2, 3, 3, 3}
print(numbers) # {1, 2, 3}

# Creating Sets
# Empty set (MUST use set(), not {})
empty_set = set() # Correct
# empty_set = {} # WRONG! This creates empty dictionary
# Set with values
fruits = {"apple", "banana", "orange"}
# From a list (removes duplicates)
numbers = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers) # {1, 2, 3}

# Adding and Removing Elements
fruits = {"apple", "banana"}
# Add single item
fruits.add("orange") # {apple, banana, orange}
fruits.add("apple") # Still {apple, banana, orange} - no duplicates!
# Add multiple items
fruits.update(["grape", "kiwi"]) # Adds both
# Remove item (error if not exists)
fruits.remove("banana") # Removes banana
# Remove item (no error if not exists)
fruits.discard("mango") # No error, does nothing
# Clear all
fruits.clear() # Now empty set

# Set Operations Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Two ways to get union
union1 = set1 | set2 # {1, 2, 3, 4, 5}
union2 = set1.union(set2) # {1, 2, 3, 4, 5}

# Set Operations Intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Two ways to get intersection
common1 = set1 & set2 # {3}
common2 = set1.intersection(set2) # {3}

# Set Operations Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Two ways to get difference
diff1 = set1 - set2 # {1, 2}
diff2 = set1.difference(set2) # {1, 2}

# Set Operations Symmetric Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Items in either set but not in both
sym_diff1 = set1 ^ set2 # {1, 2, 4, 5}
sym_diff2 = set1.symmetric_difference(set2) # {1, 2, 4, 5}

# Common Set Patterns Remove Duplicates
# Remove duplicates from list
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
# Result: ["Alice", "Bob", "Charlie"] (order might change)

# Common Set Patterns Membership Testing
# Fast checking if item exists
valid_users = {"alice", "bob", "charlie"}
username = "alice"
if username in valid_users:
    print("Valid user")

# Common Set Patterns Finding Common Elements
# Students in multiple classes
math_students = {"Alice", "Bob", "Charlie"}
science_students = {"Bob", "Charlie", "David"}
# Who takes both?
both_classes = math_students & science_students
# Result: {"Bob", "Charlie"}



'''
NUMPY ARRAYS
'''
import numpy as np # Always import like this

# Creating Arrays From Lists
import numpy as np
# 1D array
arr1d = np.array([1, 2, 3, 4])
# 2D array (matrix)
arr2d = np.array([[1, 2, 3],
[4, 5, 6]])

# Special Arrays
# Array of zeros
zeros = np.zeros(5) # [0. 0. 0. 0. 0.]
zeros_2d = np.zeros((3, 4)) # 3x4 array of zeros
# Array of ones
ones = np.ones(5) # [1. 1. 1. 1. 1.]
ones_2d = np.ones((2, 3)) # 2x3 array of ones
# Range of numbers
range_arr = np.arange(0, 10, 2) # [0 2 4 6 8]
# Random numbers
random_arr = np.random.randint(1, 100, 5) # 5 random numbers 1-99

# Array Properties
arr = np.array([[1, 2, 3],
[4, 5, 6]])
print(arr.shape) # (2, 3) - 2 rows, 3 columns
print(arr.size) # 6 - total elements
print(arr.ndim) # 2 - number of dimensions
print(arr.dtype) # int64 - data type

# Array Operations
arr = np.array([1, 2, 3, 4])
# Operations apply to all elements
print(arr + 10) # [11 12 13 14]
print(arr * 2) # [2 4 6 8]
print(arr ** 2) # [1 4 9 16]
print(arr / 2) # [0.5 1. 1.5 2.]

# Indexing and Slicing
arr = np.array([10, 20, 30, 40, 50])
print(arr[0]) # 10 - first element
print(arr[-1]) # 50 - last element
print(arr[1:4]) # [20 30 40] - slice
arr = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
# Single element
print(arr[0, 0]) # 1 - row 0, column 0
print(arr[1, 2]) # 6 - row 1, column 2
# Entire row
print(arr[0]) # [1 2 3] - first row
print(arr[1, :]) # [4 5 6] - same as arr[1]
# Entire column
print(arr[:, 0]) # [1 4 7] - first column
print(arr[:, 2]) # [3 6 9] - third column

# Statistical Functions
arr = np.array([1, 2, 3, 4, 5])
print(np.mean(arr)) # 3.0 - average
print(np.sum(arr)) # 15 - total
print(np.min(arr)) # 1 - minimum
print(np.max(arr)) # 5 - maximum
print(np.std(arr)) # Standard deviation
# For 2D arrays, specify axis
arr2d = np.array([[1, 2, 3],
[4, 5, 6]])
print(np.mean(arr2d, axis=0)) # [2.5 3.5 4.5] - column means
print(np.mean(arr2d, axis=1)) # [2. 5.] - row means

# Finding Elements
arr = np.array([1, 5, 3, 9, 2])
# Find index of maximum
max_index = np.argmax(arr) # 3 (index of 9)
# Find index of minimum
min_index = np.argmin(arr) # 0 (index of 1)
# Find where condition is true
big_numbers = arr > 3 # [False True False True False]
indices = np.where(arr > 3) # (array([1, 3]),) - indices 1 and 3

# Reshaping Arrays
arr = np.array([1, 2, 3, 4, 5, 6])
# Reshape to 2x3
reshaped = arr.reshape(2, 3)
# [[1 2 3]
# [4 5 6]]
# Reshape to 3x2
reshaped = arr.reshape(3, 2)
# [[1 2]
# [3 4]
# [5 6]]



'''
STRING OPERATIONS
'''
single = 'Hello'
double = "Hello"
multi_line = """Hello
World"""

text = "Hello"
text[0] = "J" # ERROR! Can't change string
text = "Jello" # OK - creates new string

# Case Methods
text = "Hello World"
print(text.upper()) # "HELLO WORLD"
print(text.lower()) # "hello world"
print(text.title()) # "Hello World"
print(text.capitalize()) # "Hello world"
print(text.swapcase()) # "hELLO wORLD"

#Cleaning Methods
text = " Hello World "
print(text.strip()) # "Hello World" - removes both ends
print(text.lstrip()) # "Hello World " - removes left
print(text.rstrip()) # " Hello World" - removes right
# Remove specific characters
text = "...Hello..."
print(text.strip('.')) # "Hello"

# Checking Methods
text = "Hello123"
# Check content type
print(text.isalpha()) # False - has numbers
print(text.isdigit()) # False - has letters
print(text.isalnum()) # True - letters and/or numbers
print(text.isspace()) # False - not just whitespace
# Check case
print("HELLO".isupper()) # True
print("hello".islower()) # True
# Check start/end
print(text.startswith("Hello")) # True
print(text.endswith("123")) # True

# Finding and Counting
text = "Hello World World"
# Find position
print(text.find("World")) # 6 - first occurrence
print(text.find("xyz")) # -1 - not found
print(text.index("World")) # 6 - like find but errors if not found
# Count occurrences
print(text.count("World")) # 2
print(text.count("o")) # 2

# Replacing
text = "Hello World"
# Replace all occurrences
new_text = text.replace("World", "Python")
print(new_text) # "Hello Python"
# Replace limited occurrences
text = "apple apple apple"
new_text = text.replace("apple", "orange", 2) # Replace only first 2
print(new_text) # "orange orange apple"

# Splitting
# Split by whitespace (default)
text = "Hello World Python"
words = text.split() # ['Hello', 'World', 'Python']
# Split by specific character
text = "apple,banana,orange"
fruits = text.split(',') # ['apple', 'banana', 'orange']
# Split with limit
text = "a-b-c-d"
parts = text.split('-', 2) # ['a', 'b', 'c-d'] - only 2 splits

# Joining
# Join list into string
words = ['Hello', 'World']
sentence = ' '.join(words) # "Hello World"
# Join with different separators
items = ['apple', 'banana', 'orange']
csv = ','.join(items) # "apple,banana,orange"
dashed = '-'.join(items) # "apple-banana-orange"

# F-Strings
name = "Alice"
age = 25
score = 95.5
# Basic f-string
print(f"Name: {name}, Age: {age}")
# With expressions
print(f"Next year: {age + 1}")
# Number formatting
print(f"Score: {score:.1f}") # "Score: 95.5" - 1 decimal
print(f"Score: {score:.0f}") # "Score: 96" - no decimals
print(f"Percentage: {0.856:.1%}") # "Percentage: 85.6%"
# Padding and alignment
print(f"{name:>10}") # " Alice" - right align
print(f"{name:<10}") # "Alice " - left align
print(f"{name:^10}") # " Alice " - center

# String Slicing
text = "Hello World"
# Basic slicing [start:end:step]
print(text[0:5]) # "Hello" - indices 0-4
print(text[6:]) # "World" - from 6 to end
print(text[:5]) # "Hello" - from start to 5
print(text[::2]) # "HloWrd" - every 2nd character
# Negative indices
print(text[-1]) # "d" - last character
print(text[-5:]) # "World" - last 5 characters
# Reverse string
print(text[::-1]) # "dlroW olleH"



'''
REGULAR EXPRESSIONS
'''
import re # Always import this for regex

# Literal Characters
import re
text = "Hello World"
pattern = r"World" # r means raw string (recommended for regex)
# Find pattern
if re.search(pattern, text):
    print("Found!")

# Custom Character Classes
# Square brackets for custom classes
r"[aeiou]" # Any vowel
r"[0-9]" # Any digit (same as \d)
r"[a-z]" # Any lowercase letter
r"[A-Z]" # Any uppercase letter
r"[a-zA-Z]" # Any letter
r"[^aeiou]" # NOT a vowel (^ inside [] means NOT)

# Quantifiers
r"\d{3}" # Exactly 3 digits
r"\d{2,4}" # 2 to 4 digits
r"\d{2,}" # 2 or more digits
r"\d{,4}" # Up to 4 digits

# search()
import re
text = "My phone is 555-1234"
pattern = r"\d{3}-\d{4}"
match = re.search(pattern, text)
if match:
    print(f"Found: {match.group()}") # "555-1234"
    print(f"Position: {match.span()}") # (12, 20)

# findall()
text = "I have 10 cats and 3 dogs"
pattern = r"\d+" # One or more digits
numbers = re.findall(pattern, text)
print(numbers) # ['10', '3']

# match()
# match() only checks beginning of string
text = "Hello World"
print(re.match(r"Hello", text)) # Matches
print(re.match(r"World", text)) # None (not at start)

# sub()
text = "Call 555-1234 or 555-5678"
pattern = r"\d{3}-\d{4}"
# Replace with new text
new_text = re.sub(pattern, "XXX-XXXX", text)
print(new_text) # "Call XXX-XXXX or XXX-XXXX"

# split()
text = "apple123banana456orange"
pattern = r"\d+" # Split by numbers
parts = re.split(pattern, text)
print(parts) # ['apple', 'banana', 'orange']

# Email Pattern
pattern = r"\w+@\w+\.\w+"
# Matches: user@domain.com

# Phone Number Patterns
# Format: 555-123-4567
pattern1 = r"\d{3}-\d{3}-\d{4}"
# Format: (555) 123-4567
pattern2 = r"\(\d{3}\) \d{3}-\d{4}"
# Either format
pattern3 = r"(\d{3}-|\(\d{3}\) )\d{3}-\d{4}"

# URL Pattern
pattern = r"https?://\S+"
# Matches URLs starting with http:// or https://

# Date Patterns
# Format: MM/DD/YYYY
pattern1 = r"\d{2}/\d{2}/\d{4}"
# Format: YYYY-MM-DD
pattern2 = r"\d{4}-\d{2}-\d{2}"



'''
COMMON MISTAKES TO AVOID
'''
# KeyError
# WRONG
grades = {"Math": 90}
print(grades["English"]) # KeyError!
# CORRECT
print(grades.get("English", "N/A")) # Returns "N/A"

# Using Mutable Keys
# WRONG
d = {[1, 2]: "value"} # ERROR! List can't be key
# CORRECT
d = {(1, 2): "value"} # Tuple is OK

# Modifying During Iterations
# WRONG
for key in grades:
    if grades[key] < 60:
        del grades[key] # ERROR! Dictionary changed size
# CORRECT
for key in list(grades.keys()): # Make copy of keys
    if grades[key] < 60:
        del grades[key]

# Creating Empty Set
# WRONG
s = {} # This is a dictionary!
# CORRECT
s = set() # Empty set

# Adding Lists to Sets
# WRONG
s = {[1, 2, 3]} # ERROR! List is mutable
# CORRECT
s = {(1, 2, 3)} # Use tuple instead

# Wrong Shape for Operations
# WRONG
a = np.array([1, 2, 3])
b = np.array([1, 2])
c = a + b # ERROR! Different shapes
# CORRECT
b = np.array([1, 2, 3]) # Same shape
c = a + b

# Forgetting Axis
arr = np.array([[1, 2], [3, 4]])
# WRONG
avg = np.mean(arr) # Means of entire array
# CORRECT (if you want column means)
col_avg = np.mean(arr, axis=0) # [2, 3]

# Trying to Modify String
# WRONG
text = "Hello"
text[0] = "J" # ERROR! Strings are immutable
# CORRECT
text = "J" + text[1:] # Create new string

# Forgetting strip()
# WRONG
user_input = " alice "
if user_input == "alice": # False! Has spaces
    print(False)
# CORRECT
if user_input.strip() == "alice": # True
    print(True)

# Forgetting Raw String
# WRONG
pattern = "\d+" # Might interpret \d as escape
# CORRECT
pattern = r"\d+" # Raw string

# Using match() Wrong
text = "Hello World"
# WRONG (thinking match searches everywhere)
re.match(r"World", text) # None - only checks start
# CORRECT
re.search(r"World", text) # Finds it



'''
PRACTICE PROBLEMS WITH SOLUTIONS
'''

'Dictionary Problem 1 Grade Calculator'
# Problem: Calculate average grade from dictionary
def calculate_average(grades):
    """Calculate average of grades dictionary"""
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)
# Test
grades = {"Math": 90, "English": 85, "Science": 92}
print(f"Average: {calculate_average(grades)}") # 89.0

'Dictionary Problem 2 Word Counter'
# Problem: Count word occurrences in text
def count_words(text):
    """Count occurrences of each word"""
    words = text.lower().split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count
# Test
text = "the quick brown fox jumps over the lazy dog the fox"
print(count_words(text))
# {'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, ...}

'Set Problem 1 Find Duplicates'
# Problem: Find duplicate items in a list
def find_duplicates(items):
    """Find items that appear more than once"""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)
# Test
items = [1, 2, 3, 2, 4, 3, 5]
print(find_duplicates(items)) # [2, 3]

'Set Problem 2 Common Elements'
# Problem: Find elements common to all sets
def common_to_all(list_of_sets):
    """Find elements in all sets"""
    if not list_of_sets:
        return set()
    result = list_of_sets[0]
    for s in list_of_sets[1:]:
        result = result & s
    return result
# Test
sets = [{1, 2, 3}, {2, 3, 4}, {2, 3, 5}]
print(common_to_all(sets)) # {2, 3}

'NumPy Problem 1 Normalize Data'
# Problem: Normalize array to 0-1 range
def normalize(arr):
    """Normalize array to range [0, 1]"""
    min_val = arr.min()
    max_val = arr.max()
    if min_val == max_val:
        return np.zeros_like(arr)
    return (arr - min_val) / (max_val - min_val)
# Test
data = np.array([10, 20, 30, 40, 50])
normalized = normalize(data)
print(normalized) # [0. 0.25 0.5 0.75 1.]

'NumPy Problem 2 Find Above Average'
# Problem: Find indices of values above average
def above_average_indices(arr):
    """Find indices where values > average"""
    avg = np.mean(arr)
    indices = np.where(arr > avg)[0]
    return indices
# Test
scores = np.array([70, 85, 90, 65, 95])
indices = above_average_indices(scores)
print(f"Above average at indices: {indices}") # [1 2 4]

'String Problem 1 Clean Email'
# Problem: Standardize email address
def clean_email(email):
    """Clean and standardize email"""
    # Strip whitespace and lowercase
    email = email.strip().lower()
    # Remove dots from username (Gmail style)
    if "@" in email:
        username, domain = email.split("@")
        username = username.replace(".", "")
        email = f"{username}@{domain}"
    return email
# Test
print(clean_email(" John.Doe@GMAIL.COM ")) # johndoe@gmail.com

'String Problem 2 Extract Initials'
# Problem: Get initials from full name
def get_initials(name):
    """Extract initials from name"""
    words = name.strip().split()
    initials = ""
    for word in words:
        if word:
            initials += word[0].upper()
    return initials
# Test
print(get_initials("John David Smith")) # JDS
print(get_initials("mary jane")) # MJ

'Regex Problem 1 Validate Phone'
# Problem: Check if valid phone number
def is_valid_phone(phone):
    """Check if phone matches XXX-XXX-XXXX"""
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return bool(re.match(pattern, phone))
# Test
print(is_valid_phone("555-123-4567")) # True
print(is_valid_phone("555-1234")) # False

'Regex Problem 2 Extract Numbers'
# Problem: Extract all numbers from text
def extract_numbers(text):
    """Extract all numbers (including decimals)"""
    pattern = r"\d+\.?\d*"
    return re.findall(pattern, text)
# Test
text = "I bought 3 items for $12.50 each"
print(extract_numbers(text)) # ['3', '12.50']


'''KEY FORMULAS AND PATTERNS'''
# Dictionary
# Safe access
#value = dict.get(key, default)
# Counting
#count[item] = count.get(item, 0) + 1
# Iterate key-value pairs
#for key, value in dict.items():

# Set
# Remove duplicates
#unique = list(set(items))
# Common elements
#common = set1 & set2
# Difference
#only_in_set1 = set1 - set2

# NumPy
# Statistics
#mean = np.mean(arr)
#max_index = np.argmax(arr)
# Boolean indexing
#large = arr[arr > 50]

# String
# Clean input
#clean = text.strip().lower()
# Split and join
#words = text.split()
#result = "-".join(words)

# Regex
# Common patterns
#r"\d+" # One or more digits
#r"\w+@\w+\.\w+" # Simple email
#r"^\d{3}-\d{4}$" # Phone with anchors