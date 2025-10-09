""" Problem 1: Grade Book Dictionary"""
"""
Create a grade book system with these functions:
1. add_student(gradebook, name, grade)
- Add a student with their grade
- Don't add if grade is not between 0-100
- Return True if added, False otherwise
2. get_class_average(gradebook)
- Calculate and return the average of all grades
- Return 0 if gradebook is empty
3. get_passing_students(gradebook)--Bonus
- Return a list of student names with grade >= 60
- Return empty list if none are passing
Example:
gradebook = {}
add_student(gradebook, "Alice", 85)
add_student(gradebook, "Bob", 55)
add_student(gradebook, "Charlie", 75)
print(get_class_average(gradebook)) # Should print 71.67
print(get_passing_students(gradebook)) # Should print ["Alice", "Charlie"]
"""
# Write your code here:
gradebook = {}
def add_student(gradebook, name, grade):
    """add student to library"""
    if grade < 0:
        return False
    elif grade > 100:
        return False
    if name in gradebook:
        gradebook[name]['grade'] += grade
    else:
        gradebook[name] = {
            'name': name,
            'grade': grade
        }
    return True 

#def get_class_average(gradebook):
    if not gradebook:
        return 0
    return sum(gradebook.values())/len(gradebook)
    
# Bonus -- 10 points
def get_passing_students(gradebook):
    passing = []
    for student_info in gradebook.values():
        if student_info['grade']>=60:
            passing.append(student_info['name'])
    return passing

# Test your functions
if __name__ == "__main__":
    gradebook = {}
    print(add_student(gradebook, "Alice", 85)) # Should print True
    print(add_student(gradebook, "Bob", 150)) # Should print False
    print(add_student(gradebook, "Charlie", 45)) # Should print True
    #print(f"Average: {get_class_average(gradebook):.2f}")
    # Bonus -- 10 pints
    print(f"Passing: {get_passing_students(gradebook)}")


'''
"""Problem 2: Set operations for Course Registration"""
"""
A university needs to track student course enrollments.
Write these functions:
1. find_common_students(course1_students, course2_students)
- Return set of students in BOTH courses
2. find_all_students(course1_students, course2_students)
- Return set of students in EITHER course
3. find_unique_to_course1(course1_students, course2_students)
- Return students ONLY in course1, not in course2
4. *Bonus* check_enrollment(student_name, *course_lists)
- Check if a student is in ANY of the course lists
- Return True if found, False otherwise
- Note: *course_lists means function can take multiple course lists
Example:
cs_students = {"Alice", "Bob", "Charlie", "David"}
math_students = {"Bob", "Charlie", "Eve", "Frank"}
print(find_common_students(cs_students, math_students))
# Should print: {"Bob", "Charlie"}
print(check_enrollment("Alice", cs_students, math_students))
# Should print: True
"""
# Write your code here:
def find_common_students(course1_students, course2_students):
# Your code here
pass
def find_all_students(course1_students, course2_students):
# Your code here
pass
def find_unique_to_course1(course1_students, course2_students):
# Your code here
pass
# Bonus
def check_enrollment(student_name, *course_lists):
# Your code here
pass
# Test your functions
if __name__ == "__main__":
cs_students = {"Alice", "Bob", "Charlie", "David"}
math_students = {"Bob", "Charlie", "Eve", "Frank"}
physics_students = {"Alice", "Eve", "George"}
print("Common:", find_common_students(cs_students, math_students))
print("All:", find_all_students(cs_students, math_students))
print("CS only:", find_unique_to_course1(cs_students, math_students))
# Bonus
print("Alice enrolled?", check_enrollment("Alice", cs_students,
math_students))
# Bonus
print("Henry enrolled?", check_enrollment("Henry", cs_students, math_students,
physics_students))
'''


"""Problem 3: NumPy Array Analysis"""
"""
You have temperature readings for a week (7 days, 3 times per day).
Write functions to analyze this data:
1. calculate_daily_averages(temps)
- temps is a 7x3 array (7 days, 3 readings per day)
- Return array of 7 daily averages
2. find_hottest_day(temps)
- Return the day index (0-6) with highest average temperature
3. count_cold_readings(temps, threshold)
- Count how many readings are below the threshold
- Return the count
4. normalize_temperatures(temps)
- Normalize all temperatures to 0-100 scale
- Formula: (temp - min_temp) / (max_temp - min_temp) * 100
- Return normalized array
Example:
import numpy as np
# 7 days, 3 readings per day (morning, noon, evening)
temps = np.array([
[65, 75, 70], # Day 0
[68, 78, 72], # Day 1
[70, 80, 75], # Day 2
[62, 73, 68], # Day 3
[67, 77, 71], # Day 4
[69, 79, 74], # Day 5
[64, 74, 69] # Day 6
])
"""
import numpy as np
# Write your code here:
def calculate_daily_averages(temps):
    daily_data = temps[len(temps)].reshape(len(temps), 24)
    daily_avgs = np.mean(temps, axis=1)
    return daily_avgs
def find_hottest_day(temps):
    hottest = np.argmax(temps)
    return hottest
def count_cold_readings(temps, threshold):
    colddays = (temps <= threshold)
    return np.sum(colddays)
def normalize_temperatures(temps):
    min_val = temps.min()
    max_val = temps.max()
    if min_val == max_val:
        return np.zeros_like(temps)
    return (temps - min_val) / (max_val - min_val)
# Test your functions
if __name__ == "__main__":
    temps = np.array([
    [65, 75, 70],
    [68, 78, 72],
    [70, 80, 75],
    [62, 73, 68],
    [67, 77, 71],
    [69, 79, 74],
    [64, 74, 69]
])
print("Daily averages:", calculate_daily_averages(temps))
print("Hottest day index:", find_hottest_day(temps))
print("Cold readings (< 70):", count_cold_readings(temps, 70))
print("Normalized (first day):", normalize_temperatures(temps)[0])



"""Problem 4: String Processing"""
"""
Clean and validate user input from a registration form.
Write these functions:
1. clean_name(name)
- Remove leading/trailing spaces
- Convert to title case (First Letter Capital)
- Return cleaned name
2. validate_email(email)
- Check if email contains exactly one '@'
- Check if there's at least one '.' after the '@'
- Return True if valid, False otherwise
3. format_phone(phone)
- Remove all non-digit characters
- If exactly 10 digits, format as: (XXX) XXX-XXXX
- Otherwise return "Invalid"
4. process_registration(data_string)
- data_string format: "name,email,phone"
- Split the string and clean each part
- Return dictionary with cleaned data or None if invalid
Example:
data = " john doe ,john@email.com,555-123-4567"
result = process_registration(data)
# Should return:
# {"name": "John Doe", "email": "john@email.com", "phone": "(555) 123-4567"}
"""
# Write your code here:
def clean_name(name):
    no_spaces = name.strip()
    clean_name = no_spaces.title()
    return clean_name
def validate_email(email):
    if email.count("@") != 1:
        return False
    if email.find('.') >= 1:
        return True
def format_phone(phone):
    cleanphone = phone.join(filter(str.isdigit, phone))
    return cleanphone
def process_registration(data_string):
    fields = data_string.split(", ")
    name = fields[0]
    email = fields[1]
    phone = fields[2]
    clean_info = {}
    clean_info['name'] = clean_name(name)
    clean_info['email'] = validate_email(email)
    clean_info['phone'] = format_phone(phone)
    return clean_info
# Test your functions
if __name__ == "__main__":
    # Test individual functions
    print(clean_name(" john smith ")) # Should print "John Smith"
    print(validate_email("test@email.com")) # Should print True
    print(validate_email("bad.email")) # Should print False
    print(format_phone("555-123-4567")) # Should print "(555) 123-4567"
    print(format_phone("123")) # Should print "Invalid"
    # Test complete processing
    test_data = " alice jones ,alice@example.com,9871234567"
    print(process_registration(test_data))



"""Problem 5: Regular Expressions"""
"""
Use regular expressions to extract information from text.
Write these functions:
1. find_all_phones(text)
- Find all phone numbers in format: XXX-XXX-XXXX or (XXX) XXX-XXXX
- Return list of phone numbers found
2. find_all_prices(text)
- Find all prices in format: $X.XX or $XX.XX or $XXX.XX
- Return list of prices as strings (include the $)
3. extract_emails(text)
- Find all email addresses (simple pattern: word@word.word)
- Return list of email addresses
4. validate_student_id(student_id)
- Valid format: 2 letters followed by 4 digits (e.g., "CS1234")
- Return True if valid, False otherwise
Example:
text = "Contact John at 555-123-4567 or (555) 987-6543.
Email: john@email.com. Course fee: $150.00"
print(find_all_phones(text))
# Should print: ["555-123-4567", "(555) 987-6543"]
"""
import re
# Write your code here:
def find_all_phones(text):
    pattern = r'\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}'
    return re.findall(pattern, text)
    
def find_all_prices(text):
    pattern = r'\$\d{1,3}(?:,\d{3})*\.\d{2}'
    return re.findall(pattern, text)

def extract_emails(text):
    pattern = r"\w+@\w+\.\w+"
    return re.findall(pattern, text)

def validate_student_id(student_id):
    pattern = r'[A-Z]{2}\d{4}'
    return re.findall(pattern, student_id)
# Test your functions
if __name__ == "__main__":
    test_text = """
    For info, call 555-123-4567 or (555) 987-6543.
    Email us at info@school.edu or admin@college.com
    Course fees: $50.00 for materials, $150.50 for tuition
    """
    print("Phones:", find_all_phones(test_text))
    print("Prices:", find_all_prices(test_text))
    print("Emails:", extract_emails(test_text))
    print("Valid ID 'CS1234'?", validate_student_id("CS1234"))
    print("Valid ID '12ABCD'?", validate_student_id("12ABCD"))
    print("Valid ID 'AB12345'?", validate_student_id("AB12345"))
