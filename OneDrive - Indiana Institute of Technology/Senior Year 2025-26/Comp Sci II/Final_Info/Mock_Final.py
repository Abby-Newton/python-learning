""" 
Problem 1: File Reading Basics
"""

def count_lines(filename):
    """
    Read a file and return the number of lines.
    If the file doesn't exist, return -1.
    
    Args:
        filename: name of the file to read
    
    Returns:
        Number of lines in the file, or -1 if file doesn't exist
    
    Example:
        count_lines("test.txt") → 5 (if file has 5 lines)
        count_lines("missing.txt") → -1 (if file doesn't exist)
    """
    # YOUR CODE HERE
    try:
        with open(filename, "r") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return -1
    
#CORRECT ANSWER
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return -1


"""
Problem 2: Simple Class Design
"""

"""
Create a Rectangle class with width and height attributes, and methods to calculate area and perimeter.
"""
# YOUR CODE HERE
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

#CORRECT ANSWER
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height
    

"""
Problem 3: Exception Handling
"""

def safe_divide(a, b):
    """
    Safely divide two numbers with error handling.
    
    Args:
        a: numerator (string or number)
        b: denominator (string or number)
    
    Returns:
        Result of a/b if successful
        "Error: Cannot divide by zero" if b is 0
        "Error: Invalid input" if inputs can't be converted to numbers
    
    Examples:
        safe_divide(10, 2) → 5.0
        safe_divide("10", "2") → 5.0
        safe_divide(10, 0) → "Error: Cannot divide by zero"
        safe_divide("abc", 2) → "Error: Invalid input"
    """
    # YOUR CODE HERE
    # Hint: You'll need try-except blocks
    # Hint: Convert inputs to float first
    # Hint: Check for division by zero
    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        return "Error: Invalid input"
    
    if b == 0:
        return "Error: Cannot divide by zero"
    
    return a / b

# Test your code:
print(safe_divide(10, 2))     # 5.0
print(safe_divide("10", "2")) # 5.0
print(safe_divide(10, 0))     # Error: Cannot divide by zero
print(safe_divide("abc", 2))  # Error: Invalid input

#CORRECT ANSWER
def safe_divide(a, b):
    try:
        num_a = float(a)
        num_b = float(b)
        
        if num_b == 0:
            return "Error: Cannot divide by zero"
        
        return num_a / num_b
    
    except (ValueError, TypeError):
        return "Error: Invalid input"


"""
Problem 4: Recursion - Sum of Digits
"""

def sum_of_digits(n):
    """
    Calculate the sum of all digits in a number using recursion.
    
    Args:
        n: a positive integer
        
    Returns:
        Sum of all digits in n
        
    Examples:
        sum_of_digits(123) → 6 (because 1 + 2 + 3 = 6)
        sum_of_digits(4567) → 22 (because 4 + 5 + 6 + 7 = 22)
        sum_of_digits(5) → 5
        sum_of_digits(0) → 0
    """
    # YOUR CODE HERE
    # Hint: What's the base case? (When should recursion stop?)
    # Hint: How do you get the last digit? (n % 10)
    # Hint: How do you remove the last digit? (n // 10)
    # Hint: The sum is (last digit) + sum_of_digits(remaining digits)
    # Base case
    if n == 0:
        return 0
    
    # Recursive case
    last_digit = n % 10
    remaining = n // 10
    return last_digit + sum_of_digits(remaining)

    # Base case: if n is 0, return 0

    # Recursive case:
    # Get the last digit using n % 10
    # Get the remaining digits using n // 10
    # Return last digit + sum_of_digits(remaining)

# Test your code:
print(sum_of_digits(123)) # Should print: 6
print(sum_of_digits(4567)) # Should print: 22
print(sum_of_digits(5)) # Should print: 5
print(sum_of_digits(0)) # Should print: 0

#CORRECT ANSWER
def sum_of_digits(n):
    # Base case
    if n == 0:
        return 0

    # Recursive case
    last_digit = n % 10
    remaining = n // 10
    return last_digit + sum_of_digits(remaining)


"""
Problem 5: Advanced Functions - Student Grade Processor
"""

def process_grades(students):
    """
    Process a list of student dictionaries:
    1. Filter out students with average < 60
    2. Add a letter grade to each remaining student
    3. Sort by average (highest first)
    
    Args:
        students: list of dictionaries with 'name' and 'grades' keys
    
    Returns:
        List of processed students with added 'average' and 'letter' keys
    
    Example Input:
        [
            {'name': 'Alice', 'grades': [90, 85, 95]},
            {'name': 'Bob', 'grades': [50, 45, 55]},
            {'name': 'Charlie', 'grades': [70, 75, 72]}
        ]
        
    Example Output:
        [
            {'name': 'Alice', 'grades': [90, 85, 95], 'average': 90.0, 'letter':
                'A'},
            {'name': 'Charlie', 'grades': [70, 75, 72], 'average': 72.3, 'letter':
                'C'}
        ]
        (Bob filtered out because average < 60)
    """
    
    # Step 1: Calculate average for each student
    # Hint: Use map with a lambda that adds 'average' key
    students_with_avg = list(map(
        lambda s: {**s, 'average': sum(s['grades']) / len(s['grades'])},
        students
    ))
    
    # Step 2: Filter out students with average < 60
    # Hint: Use filter with a lambda
    passing_students = list(filter(
        lambda s: s['average'] >= 60,
        students_with_avg
    ))
    
    # Step 3: Add letter grades
    # A: >= 90, B: >= 80, C: >= 70, D: >= 60
    def add_letter_grade(student):
        avg = student['average']
        if avg >= 90:
            student['letter'] = 'A'
        elif avg >= 80:
            student['letter'] = 'B'
        elif avg >= 70:
            student['letter'] = 'C'
        else:
            student['letter'] = 'D'
        return student

    graded_students = list(map(add_letter_grade, passing_students))
    
    # Apply the letter grade function using map
    
    # Step 4: Sort by average (highest first)
    # Hint: Use sorted() with key parameter
    result = sorted(graded_students, key=lambda s: s['average'], reverse=True)
    
    return result
# Test your code:
test_students = [
    {'name': 'Alice', 'grades': [90, 85, 95]},
    {'name': 'Bob', 'grades': [50, 45, 55]},
    {'name': 'Charlie', 'grades': [70, 75, 72]},
    {'name': 'Diana', 'grades': [88, 92, 85]}
]

result = process_grades(test_students)
for student in result:
    print(f"{student['name']}: {student['average']:.1f} ({student['letter']})")

#CORRECT ANSWER
def process_grades(students):
    # Step 1: Add averages
    with_avg = list(map(
        lambda s: {**s, 'average': sum(s['grades'])/len(s['grades'])},
        students
    ))
    
    # Step 2: Filter >= 60
    passing = list(filter(lambda s: s['average'] >= 60, with_avg))

    # Step 3: Add letter grades
    def add_letter_grade(student):
        avg = student['average']
        if avg >= 90:
            student['letter'] = 'A'
        elif avg >= 80:
            student['letter'] = 'B'
        elif avg >= 70:
            student['letter'] = 'C'
        else:
            student['letter'] = 'D'
        return student
    
    with_letters = list(map(add_letter_grade, passing))

    # Step 4: Sort by average
    result = sorted(with_letters, key=lambda s: s['average'], reverse=True)

    return result