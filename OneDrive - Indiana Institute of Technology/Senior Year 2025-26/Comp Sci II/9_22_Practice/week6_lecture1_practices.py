import re

'''
practice 1_a
'''

# Match years (exactly 4 digits)
text = "Born in 1995, graduated 2017, now it's 24"
pattern1a = r"\d{4}"  # Fill in the repetition

matches = re.findall(pattern1a, text)
print(f"Years found: {matches}")

'''
practice 1_b
'''
# Validate hex color codes (#RGB or #RRGGBB)
colors = ["#FFF", "#FFFFFF", "#12AB56", "#GGG", "#12"]
# Write pattern for 3 or 6 hex digits after #
# Hint: [0-9A-Fa-f]{3} or {6}
pattern1b = r"[0-9A-Fa-f]{3} or {6}"
matches = re.findall(pattern1b, colors)
print(f"Colors found: {matches}")

'''
practice 1_c
'''
# Extract and validate US Social Security Numbers
# Format: XXX-XX-XXXX where X is a digit
text = "SSN: 123-45-6789, Invalid: 12-345-6789, 123-4-5678"
# Write pattern using {n} for each section
pattern1c = r"\d{3}-\d{2}-\d{4}"
matches = re.findall(pattern1c, text)
print(f"SSN found: {matches}")

'''
practice 2_a
'''
# Match repeated words like "very very" or "really really"
text = "It's very very important and really really cool"
pattern2a = r"(very)+ or (really)+"  # Fill in to match repeated words

matches = re.findall(pattern2a, text)
print(f"Repeated words: {matches}")

'''
practice 2_b
'''
# Extract date components (MM/DD/YYYY)
dates = ["12/25/2024", "01/01/2025", "13/40/2024"]
# Write pattern with groups for month, day, year
pattern2b = r"(\w+)/(\w+)/(\w+)"
# Validate and extract each component
matches = re.findall(pattern2b, dates)
print(f"Group of Months: {matches.group(0)}")
print(f"Group of Days: {matches.group(1)}")
print(f"Group of Years: {matches.group(2)}")

'''
practice 2_c
'''
# Parse URLs: protocol://domain/path
urls = ["http://example.com/page", "https://site.org/path/to/file"]
# Create groups for protocol, domain, and path
pattern2c = r"(\w+)//(\w+).(\w+)/(\w+)"
# Print each component separately
matches = re.findall(pattern2c, urls)
print(f"Group of protocols: {matches.group(1)}")
print(f"Group of domainss: {matches.group(2)}")
print(f"Group of paths: {matches.group(3)}")

'''
practice 3_a
'''
# Extract name and age from text
text = "My name is Alice and I am 25 years old"
pattern3a = r"name is (\w+) and I am (\d+)"

# Complete the code to print name and age separately
match = re.search(pattern3a, text)
if match:
    # Print the captured groups
    print(f"Name: {match.group(0)}")
    print(f"Age: {match.group(1)}")
    pass

'''
practice 3_b
'''
# Parse email addresses with named groups
emails = ["john.doe@company.com", "alice_smith@university.edu"]
# Write pattern with named groups for username and domain
pattern3b = r"(?P<username>\w+)@(?P<domain>\w+).(?P<path>\w+)"
# Pattern: (?P<user>...) @ (?P<domain>...)
match = re.search(pattern3b, emails)
if match:
    # Print the captured groups
    print(f"Username: {match.group('username')}")
    print(f"Domain: {match.group('domain')}")
    pass

'''
practice 3_c
'''
# Extract and validate time in HH:MM:SS format
times = ["12:30:45", "25:00:00", "10:65:30", "09:15:22"]
# Write pattern with groups for hours, minutes, seconds
pattern3c = r"(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+)"
# Validate each component (hours: 00-23, minutes/seconds: 00-59)
match = re.search(pattern3c, times)
if match:
    # Print the captured groups
    print(f"Hours: {match.group('hours')}")
    print(f"Minutes: {match.group('minutes')}")
    print(f"Seconds: {match.group('seconds')}")
    pass

'''
practice 4_a
'''
text = "Hello there! Hi everyone. Hey you. Goodbye."
pattern = r"___"  # Fill in: Match Hello, Hi, or Hey

matches = re.findall(pattern, text)
print(f"Greetings: {matches}")

'''
practice 4_b
'''
# Validate file extensions for documents
files = ["report.doc", "image.jpg", "data.xlsx", "notes.txt"]
# Match .doc, .docx, .pdf, or .txt files
# Use alternation with proper grouping

'''
practice 4_c
'''
# Parse different date formats
dates = ["2024-01-15", "15/01/2024", "Jan 15, 2024", "January 15, 2024"]
# Write pattern to match:
# - YYYY-MM-DD
# - DD/MM/YYYY
# - Mon DD, YYYY
# Use alternation to handle all formats

'''
practice 5-a
'''
# Find a number and print its position
text = "The temperature is 72 degrees"
pattern = r"\d+"

match = re.search(pattern, text)
if match:
    # Print the number and where it was found
    # Use match.group() and match.span()
    pass

'''
practice 5_b
'''
# Extract URL components and their positions
url = "https://www.example.com/path/to/page"
pattern = r"(https?)://([^/]+)(.*)"

# Use the match object to extract:
# - Protocol (http or https)
# - Domain
# - Path
# - Position of each component

'''
practice 5_c
'''
# Build a function that returns match details as dictionary
def get_match_info(text, pattern):
    """
    Return dictionary with:
    - 'found': Boolean
    - 'match': The matched text
    - 'groups': All captured groups
    - 'position': (start, end) tuple
    - 'before': Text before match
    - 'after': Text after match
    """
    # Implement this function
    pass

# Test with: "Price: $19.99 (discounted)"
# Pattern: r"\$(\d+)\.(\d{2})"

'''
practice 6_a
'''
# Check if string starts with "Hello"
texts = ["Hello World", "Say Hello", "Hello", "HELLO"]
pattern = r"Hello"

for text in texts:
    # Use re.match to check if text starts with Hello
    # Print whether it matches or not
    pass

'''
practice 6_b
'''
# Validate phone number format from start of string
# Format: (XXX) XXX-XXXX or XXX-XXX-XXXX
phones = ["(555) 123-4567", "555-123-4567", "Call 555-1234", "123-4567"]
# Write validation using re.match

'''
practice 6_c
'''
# Parse variable assignments (var = value)
assignments = ["x = 10", "name = 'John'", "flag = True", "= invalid", "no equals"]
# Write pattern to match and extract variable name and value
# Pattern should match from start: variable_name = value