"""Problem 1: Library Book System"""
"""
Create a library system with these functions:
1. add_book(library, isbn, title, copies)
- Add a book to library (isbn is the unique identifier)
- copies must be >= 0
- If book already exists, add to existing copies
- Return True if successful, False if invalid
2. check_out_book(library, isbn)
- Decrease copies by 1 if available
- Return True if checked out, False if not available
3. return_book(library, isbn)
- Increase copies by 1
- Add book with 1 copy if doesn't exist
- Always returns True
4. *bonus* get_available_books(library)
- Return list of titles that have copies > 0
- Return empty list if none available
Example:
library = {}
add_book(library, "123", "Python Basics", 3)
add_book(library, "456", "Data Science", 2)
check_out_book(library, "123") # Now has 2 copies
print(get_available_books(library))
# Should print: ["Python Basics", "Data Science"]
"""
# Write your code here:
library = {}
def add_book(library, isbn, title, copies):
    """Add book to library"""
    # Validate copies
    if copies < 0:
        return False
    # Check if book exists
    if isbn in library:
    # Add to existing copies
        library[isbn]['copies'] += copies
    else:
    # Add new book
        library[isbn] = {
            'title': title,
            'copies': copies
        }
    return True

def check_out_book(library, isbn):
    """Check out a book if available"""
    # Check if book exists and has copies
    if isbn not in library:
        return False
    if library[isbn]['copies'] > 0:
        library[isbn]['copies'] -= 1
        return True
    return False

def return_book(library, isbn):
    """Return a book"""
    # If book exists, increment copies
    if isbn in library:
        library[isbn]['copies'] += 1
    else:
    # Add book with 1 copy (assuming unknown title)
        library[isbn] = {
            'title': 'Unknown Title',
            'copies': 1
        }
    return True

# Bonus question
def get_available_books(library):
    """Get list of available book titles"""
    available = []
    for book_info in library.values():
        if book_info['copies'] > 0:
            available.append(book_info['title'])
    return available

# Test your functions
if __name__ == "__main__":
    library = {}
    # Test adding books
    print(add_book(library, "001", "Learn Python", 5)) # True
    print(add_book(library, "002", "Learn Java", -1)) # False (negative)
    print(add_book(library, "001", "Learn Python", 2)) # True (adds to existing)
    print(f"Library: {library}")
    # Test checkout
    print(check_out_book(library, "001")) # True
    print(check_out_book(library, "999")) # False (doesn't exist)
    # Test available books
    # bonus
    print(f"Available: {get_available_books(library)}")


"""Problem 2: Class Attendance with Sets"""
"""
Track which students attended which classes.
Write these functions:
1. mark_attendance(attendance_dict, date, student_list)
- Record attendance for a specific date
- attendance_dict: dictionary where keys are dates, values are sets of students
- student_list: list of students who attended
- Convert list to set and store
2. get_perfect_attendance(attendance_dict)
- Find students who attended ALL classes
- Return set of students (empty set if none)
3. get_absent_students(attendance_dict, date, all_students)
- Find who was absent on a specific date
- all_students: set of all enrolled students
- Return set of absent students
# 10 bonus points
4. get_attendance_rate(attendance_dict, student_name)
- Calculate attendance percentage for a student
- Return percentage (0-100) as float
- Return 0.0 if no classes recorded
Example:
attendance = {}
mark_attendance(attendance, "2024-01-01", ["Alice", "Bob", "Charlie"])
mark_attendance(attendance, "2024-01-02", ["Alice", "Charlie"])
all_students = {"Alice", "Bob", "Charlie", "David"}
absent = get_absent_students(attendance, "2024-01-02", all_students)
print(absent) # {"Bob", "David"}
"""
# Write your code here:
def mark_attendance(attendance_dict, date, student_list):
    """Mark attendance for a date"""
    # Convert list to set and store
    attendance_dict[date] = set(student_list)

def get_perfect_attendance(attendance_dict):
    """Find students who attended all classes"""
    if not attendance_dict:
        return set()
    # Start with first day's students
    all_dates = list(attendance_dict.keys())
    perfect = attendance_dict[all_dates[0]].copy()
    # Intersect with each other day
    for date in all_dates[1:]:
        perfect = perfect & attendance_dict[date]
    return perfect

def get_absent_students(attendance_dict, date, all_students):
    """Find absent students on a date"""
    if date not in attendance_dict:
        return all_students
    present = attendance_dict[date]
    absent = all_students - present
    return absent

#bonus question
def get_attendance_rate(attendance_dict, student_name):
    """Calculate attendance percentage"""
    if not attendance_dict:
        return 0.0
    total_classes = len(attendance_dict)
    attended = 0
    for students_present in attendance_dict.values():
        if student_name in students_present:
            attended += 1
    rate = (attended / total_classes) * 100
    return rate

# Test your functions
if __name__ == "__main__":
    attendance = {}
    # Mark attendance for different days
    mark_attendance(attendance, "Monday", ["Alice", "Bob", "Charlie"])
    mark_attendance(attendance, "Tuesday", ["Alice", "Charlie", "David"])
    mark_attendance(attendance, "Wednesday", ["Alice", "Bob", "David"])
    print(f"Attendance records: {attendance}")
    # Test perfect attendance
    print(f"Perfect attendance: {get_perfect_attendance(attendance)}")
    # Test absent students
    all_students = {"Alice", "Bob", "Charlie", "David", "Eve"}
    print(f"Absent on Tuesday: {get_absent_students(attendance, 'Tuesday',
    all_students)}")
    # bonus
    # Test attendance rate
    print(f"Alice's rate: {get_attendance_rate(attendance, 'Alice'):.1f}%")
    print(f"Eve's rate: {get_attendance_rate(attendance, 'Eve'):.1f}%")


"""Problem 3: Weather Data Analysis with NumPy"""
"""
Analyze weather data (temperatures) for a city.
Write functions to:
1. generate_weather_data(days)
- Generate random temperatures between 50-95°F
- Return 1D array of temperatures
2. find_extreme_days(temps)
- Find indices of hottest and coldest days
- Return tuple: (hottest_day_index, coldest_day_index)
3. calculate_weekly_averages(temps)
- Group temperatures into weeks (7 days each)
- Return array of weekly averages
- Ignore incomplete last week
4. count_days_in_range(temps, min_temp, max_temp)
- Count days with temperature in range [min_temp, max_temp]
- Return count as integer
Example:
temps = generate_weather_data(14) # 2 weeks of data
hot_day, cold_day = find_extreme_days(temps)
print(f"Hottest day: {hot_day}, Coldest day: {cold_day}")
weekly_avgs = calculate_weekly_averages(temps)
print(f"Weekly averages: {weekly_avgs}")
"""
import numpy as np
# Write your code here:
def generate_weather_data(days):
    """Generate random temperatures 50-95°F"""
    return np.random.uniform(50, 95, days)
    # Alternative: return np.random.randint(50, 96, days)

def find_extreme_days(temps):
    """Find hottest and coldest day indices"""
    hottest = np.argmax(temps)
    coldest = np.argmin(temps)
    return (hottest, coldest)

def calculate_weekly_averages(temps):
    """Calculate weekly averages"""
    # Number of complete weeks
    num_weeks = len(temps) // 7
    # Reshape to weeks (ignore incomplete week)
    weekly_data = temps[:num_weeks * 7].reshape(num_weeks, 7)
    # Calculate average for each week
    weekly_avgs = np.mean(weekly_data, axis=1)
    return weekly_avgs

def count_days_in_range(temps, min_temp, max_temp):
    """Count days in temperature range"""
    # Create boolean mask
    in_range = (temps >= min_temp) & (temps <= max_temp)
    # Count True values
    return np.sum(in_range)

# Test your functions
if __name__ == "__main__":
    # Generate 21 days of weather data
    temps = generate_weather_data(21)
    print(f"Temperature data (first 7 days): {temps[:7]}")
    # Find extremes
    hot, cold = find_extreme_days(temps)
    print(f"Hottest day: Day {hot} ({temps[hot]:.1f}°F)")
    print(f"Coldest day: Day {cold} ({temps[cold]:.1f}°F)")
    # Weekly averages
    weekly = calculate_weekly_averages(temps)
    print(f"Weekly averages: {weekly}")
    # Count comfortable days (65-80°F)
    comfortable = count_days_in_range(temps, 65, 80)
    print(f"Days between 65-80°F: {comfortable}")


"""Problem 4: Username Generator"""
"""
Generate and validate usernames from full names.
Write these functions:
1. create_username(full_name)
- Take first letter of first name + entire last name
- Convert to lowercase
- Remove all spaces
- Example: "John Smith" -> "jsmith"
2. validate_username(username)
- Must be 3-15 characters long
- Must contain only letters and numbers
- Must start with a letter
- Return True if valid, False otherwise
3. make_unique_username(base_username, existing_usernames)
- If base_username not in existing_usernames, return it
- Otherwise, add numbers starting from 1 until unique
- Example: "jsmith" exists, try "jsmith1", "jsmith2", etc.
4. process_name_list(names_string)
- names_string format: "Name1;Name2;Name3"
- Split by semicolon, create username for each
- Return list of usernames
Example:
name = "Alice Johnson"
username = create_username(name)
print(username) # "ajohnson"
print(validate_username("ab")) # False (too short)
print(validate_username("alice123")) # True
"""
# Write your code here:
def create_username(full_name):
    """Create username from full name"""
    # Split name into parts
    parts = full_name.strip().split()
    if len(parts) < 2:
        return full_name.lower().replace(" ", "")
    # First letter of first name + last name
    first_initial = parts[0][0].lower()
    last_name = parts[-1].lower()
    username = first_initial + last_name
    return username

def validate_username(username):
    """Validate username format"""
    # Check length
    if not 3 <= len(username) <= 15:
        return False
    # Check if starts with letter
    if not username[0].isalpha():
        return False
    # Check if only letters and numbers
    if not username.isalnum():
        return False
    return True

def make_unique_username(base_username, existing_usernames):
    """Make username unique"""
    if base_username not in existing_usernames:
        return base_username
    # Try adding numbers
    counter = 1
    while True:
        new_username = f"{base_username}{counter}"
        if new_username not in existing_usernames:
            return new_username
        counter += 1

def process_name_list(names_string):
    """Process list of names"""
    # Split by semicolon
    names = names_string.split(';')
    # Create username for each
    usernames = []
    for name in names:
        username = create_username(name.strip())
        usernames.append(username)
    return usernames

# Test your functions
if __name__ == "__main__":
    # Test username creation
    print(create_username("John Smith")) # jsmith
    print(create_username("Mary Jane Jones")) # mjones
    # Test validation
    print(validate_username("abc123")) # True
    print(validate_username("ab")) # False (too short)
    print(validate_username("123abc")) # False (starts with number)
    print(validate_username("user@name")) # False (has @)
    # Test unique username
    existing = ["jsmith", "ajones", "jsmith1"]
    print(make_unique_username("jsmith", existing)) # jsmith2
    print(make_unique_username("bwilson", existing)) # bwilson
    # Test batch processing
    names = "Alice Brown;Bob Wilson;Carol Davis"
    usernames = process_name_list(names)
    print(f"Usernames: {usernames}")


"""Problem 5: Data Extraction with Regex"""
"""
Extract structured data from text using regex.
Write these functions:
1. extract_phone_numbers(text)
- Find phone numbers in format: (XXX) XXX-XXXX or XXX-XXX-XXXX
- Return list of all phone numbers found
2. extract_course_codes(text)
- Find course codes: 2-4 uppercase letters followed by 3-4 digits
- Examples: "CS101", "MATH2010", "BIO305"
- Return list of course codes
3. validate_zip_code(zip_string)
- Valid formats: XXXXX or XXXXX-XXXX (5 digits or 5+4 digits)
- Return True if valid, False otherwise
4. extract_money_amounts(text)
- Find money amounts like: $X.XX, $XX.XX, $XXX.XX, $X,XXX.XX
- Return list of amounts as strings (keep the $ sign)
Example:
text = "Call (555) 123-4567 or 555-987-6543 for CS1350 info"
phones = extract_phone_numbers(text)
courses = extract_course_codes(text)
print(phones) # ["(555) 123-4567", "555-987-6543"]
print(courses) # ["CS1350"]
"""
import re
# Write your code here:
def extract_phone_numbers(text):
    """Extract phone numbers"""
    # Pattern for (XXX) XXX-XXXX or XXX-XXX-XXXX
    pattern = r'\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}'
    return re.findall(pattern, text)

def extract_course_codes(text):
    """Extract course codes"""
    # 2-4 uppercase letters followed by 3-4 digits
    pattern = r'[A-Z]{2,4}\d{3,4}'
    return re.findall(pattern, text)

def validate_zip_code(zip_string):
    """Validate zip code format"""
    # XXXXX or XXXXX-XXXX
    pattern = r'^\d{5}(-\d{4})?$'
    if re.match(pattern, zip_string):
        return True
    return False

def extract_money_amounts(text):
    """Extract money amounts"""
    # $X.XX, $XX.XX, $XXX.XX, $X,XXX.XX
    pattern = r'\$\d{1,3}(?:,\d{3})*\.\d{2}'
    return re.findall(pattern, text)

# Test your functions
if __name__ == "__main__":
    # Test phone extraction
    text1 = "Contact us at (555) 123-4567 or 555-987-6543 for more info"
    phones = extract_phone_numbers(text1)
    print(f"Phones: {phones}")
    # Test course code extraction
    text2 = "I'm taking CS101, MATH2010, and ENGL305 this semester"
    courses = extract_course_codes(text2)
    print(f"Courses: {courses}")
    # Test zip code validation
    print(f"12345 valid? {validate_zip_code('12345')}") # True
    print(f"12345-6789 valid? {validate_zip_code('12345-6789')}") # True
    print(f"123 valid? {validate_zip_code('123')}") # False
    # Test money extraction
    text3 = "Items cost $5.99, $125.00, and $1,299.99"
    money = extract_money_amounts(text3)
    print(f"Money amounts: {money}")