""" Problem 1"""
def count_lines_with_word(filename, word):
    """
    Count how many lines in a file contain a specific word.
    The search should be case-insensitive.

    Parameters:
        filename (str): Name of the file to read
        word (str): Word to search for

    Returns:
        int: Number of lines containing the word
        Returns 0 if file doesn't exist

    Example:
        If file contains:
        "Hello world"
        "Python is fun"
        "Hello again"

        count_lines_with_word("file.txt", "hello") returns 2
    """
    count = 0
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for n < (len(lines)+1):
                if len(lines(n(0))) == word:
                    count += 1
                    n += 1
                else:
                    n += 1
    except FileNotFoundError:
        return 0
    
    return count

"""Problem 2"""
class BankAccount:
    """
    A simple bank account class.
    """

    def __init__(self, owner_name, initial_balance):
        """
        Initialize a bank account.

        Parameters:
            owner_name (str): Name of account owner
            initial_balance (float): Starting balance (default 0)
        """
        # YOUR CODE HERE
        # Store owner_name and balance as instance variables
        inital_balance = 0
        self.owner_name = owner_name
        self.initial_balance = initial_balance

    def deposit(self, amount):
        """
        Add money to the account.

        Parameters:
            amount (float): Amount to deposit
        
        Returns:
            float: New balance after deposit
        """
        # YOUR CODE HERE
        # Add amount to balance if amount is positive
        # Return the new balance
        new_balance = self.initial_balance
        amount = float(amount)
        if amount > 0:
            new_balance += amount
        else:
            return "invalid amount"

    def withdraw(self, amount):
        """
        Remove money from the account if sufficient funds exist.

        Parameters:
            amount (float): Amount to withdraw

        Returns:
            float: New balance after withdrawal
            Returns current balance unchanged if insufficient funds
        """
        # YOUR CODE HERE
        # Check if balance >= amount
        # If yes, subtract amount from balance
        # If no, print "Insufficient funds"
        # Return the balance
        new_balance = self.initial_balance
        amount = float(amount)
        if new_balance > amount:
            new_balance -= amount
        else:
            return "insufficient amount"

    def get_balance(self):
        """
        Get current balance.

        Returns:
            float: Current balance
        """
        # YOUR CODE HERE
        new_balance = self.initial_balance
        self = float(self)
        return f"current balance is {new_balance}"

# Test code (don't modify):
# account = BankAccount("John", 100)
# print(account.deposit(50)) # Should print: 150
# print(account.withdraw(30)) # Should print: 120
# print(account.withdraw(200)) # Should print: "Insufficient funds" then 120


"""Problem 3"""
def safe_calculate(num1, num2, operation):
    """
    Perform arithmetic operation with exception handling.

    Parameters:
        num1: First number (can be string or number)
        num2: Second number (can be string or number)
        operation (str): One of '+', '-', '*', '/'

    Returns:
        float: Result of the operation
        str: Error message if operation fails
    
    Examples:
        safe_calculate(10, 5, '+') returns 15.0
        safe_calculate("10", "5", '-') returns 5.0
        safe_calculate(10, 0, '/') returns "Error: Division by zero"
        safe_calculate("abc", 5, '+') returns "Error: Invalid number"
        safe_calculate(10, 5, '%') returns "Error: Invalid operation"
    """
    # YOUR CODE HERE
    # Step 1: Try to convert num1 and num2 to float
    # Step 2: Check if operation is valid (+, -, *, /)
    # Step 3: Perform the operation
    # Step 4: Handle division by zero
    # Step 5: Handle invalid number conversion
    try:
        # Convert inputs to numbers
        num_1 = float(num1)
        num_2 = float(num2)
        # Check operation and calculate
        if operation == +:
            add = num_1 + num_2
        elif operation == -:
            sub = num_1 - num_2
        elif operation == *:
            mult = num_1 * num_2
        elif operation == /:
            div = num_1 / num_2
        else:
            e = operation
            return "Invalid operation"
        if num_1 == str:
            e = num_1
            return "Cannot use non numbers"
        if num_2 == str:
            e = num_2
            return "Cannot use non numbers"
        if num_2 == 0:
            e = num_2
            return "Cannot divide by zero"
        return f"The num1 float is {num_1} and num2 float is {num_2}. The addition is {add}. The subtraction is {sub}. The multiplication is {mult}. The division is {div}."
    except ValueError:
        # Handle conversion error
        print(f"ValueError: {e}")
    except ZeroDivisionError:
        # Handle division by zero
        print(f"ZeroDivisionError: {e}")
    else:
        print(f"InvalidID: {e}")
        
# Test your function:
# print(safe_calculate(10, 5, '+')) # 15.0
# print(safe_calculate("10", "5", '-')) # 5.0
# print(safe_calculate(10, 0, '/')) # Error: Division by zero
# print(safe_calculate("abc", 5, '+')) # Error: Invalid number

"""Problem 4"""
def is_palindrome_recursive(s):
    """
    Check if a string is a palindrome using recursion.
    Ignore spaces and case.

    Parameters:
        s (str): String to check

    Returns:
        bool: True if palindrome, False otherwise

    Examples:
        is_palindrome_recursive("racecar") returns True
        is_palindrome_recursive("A man a plan a canal Panama") returns True
        is_palindrome_recursive("hello") returns False
        is_palindrome_recursive("") returns True
        is_palindrome_recursive("a") returns True
    """
    # YOUR CODE HERE
    if s != str:
        return "invalid input"
    
    if s(0) == s(-1):
        return "True"
    else:
        return "False"

# Test your function:
# print(is_palindrome_recursive("racecar")) # True
# print(is_palindrome_recursive("hello")) # False
# print(is_palindrome_recursive("A man a plan a canal Panama")) # True
# print(is_palindrome_recursive("")) # True

"""Problem 5"""
def analyze_grades(students):
    """
    Analyze student grades using map, filter, and lambda functions.

    Parameters:
        students: List of tuples (name, [grades])

    Returns:
        Dictionary with:
        - 'passing': List of names of students with average >= 70
        - 'failing': List of names of students with average < 70
        - 'highest': Name of student with highest average
        - 'class_average': Average of all student averages

    Example:
        students = [
            ('Alice', [85, 90, 88]),
            ('Bob', [60, 65, 62]),
            ('Charlie', [75, 80, 77])
        ]

        Returns:
        {
            'passing': ['Alice', 'Charlie'],
            'failing': ['Bob'],
            'highest': 'Alice',
            'class_average': 73.7
        }
    """
    
    # Step 1: Calculate average for each student
    # Create list of tuples: (name, average)
    # Hint: Use map with lambda to calculate averages
    name = [students(0)]
    average = [list(map(
        lambda s: {**s, 'average': sum(s['grades'])/len(s['grades'])},
        students
    ))]

    # Step 2: Filter passing students (average >= 70)
    # YOUR CODE HERE
    # Use filter with lambda on student_averages
    passing = [list(filter(lambda s: s['average'] >= 70, average))] # Replace with your filter code

    # Step 3: Filter failing students (average < 70)
    # YOUR CODE HERE
    failing = [list(filter(lambda s: s['average'] < 60, students.remove()))] # Replace with your filter code

    # Step 4: Find student with highest average
    # YOUR CODE HERE
    # Use max() with key parameter
    highest = max(students(1)) # Replace with your code

    # Step 5: Calculate class average
    # YOUR CODE HERE
    # Sum all averages and divide by number of students
    class_avg = average/len(name) # Replace with your calculation

    return {
        'passing': [s[0] for s in passing],
        'failing': [s[0] for s in failing],
        'highest': highest,
        'class_average': round(class_avg, 1)
    }
# Test your function:
test_data = [
    ('Alice', [85, 90, 88]),
    ('Bob', [60, 65, 62]),
    ('Charlie', [75, 80, 77]),
    ('Diana', [95, 92, 94])
]

# result = analyze_grades(test_data)
# print(result)
