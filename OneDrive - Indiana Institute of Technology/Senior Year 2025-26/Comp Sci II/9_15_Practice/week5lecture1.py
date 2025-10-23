"""
CS1350 Computer Science II
Week 5 Lecture 1: Advanced String Operations
Student Skeleton Code

Name: Abby Newton
Date: September 15, 2025
"""

# ============================================================
# UNIT 1: String Methods - Changing Case and Cleaning
# ============================================================

def practice_1a_beginner():
    """
    Beginner: Clean up a messy name
    """
    print("\n" + "="*50)
    print("EXERCISE 1A: Clean the Name (Beginner)")
    print("="*50)
    
    # Messy name from user input
    messy_name = "   jOhN sMiTh   "
    print(f"Messy name: '{messy_name}'")
    
    # TODO 1: Remove spaces from both ends
    # Use: messy_name.strip()
    no_spaces = messy_name.strip()  # Replace None with your code
    
    # TODO 2: Convert to title case (John Smith)
    # Use: .title() on your no_spaces variable
    clean_name = no_spaces.title()  # Replace None with your code
    
    print(f"After removing spaces: '{no_spaces}'")
    print(f"Final clean name: '{clean_name}'")
    
    # Check your work
    if clean_name == "John Smith":
        print("✅ Perfect! You cleaned the name correctly!")
    else:
        print("❌ Not quite right. Try again!")
        

def practice_1b_intermediate():
    """
    Intermediate: Standardize email addresses
    """
    print("\n" + "="*50)
    print("EXERCISE 1B: Email Standardizer (Intermediate)")
    print("="*50)
    
    emails = [
        "  JOHN@GMAIL.COM",
        "Alice@Yahoo.com  ",
        "  Bob@HOTMAIL.COM  "
    ]
    
    print("Messy emails:")
    for email in emails:
        print(f"  '{email}'")
    
    cleaned_emails = []
    for email in emails:
        # TODO 1: Remove spaces
        cleaned = email.strip()  # Replace with email.strip()
        
        # TODO 2: Convert to lowercase
        cleaned = cleaned.lower()  # Replace with cleaned.lower()
        
        # TODO 3: Add to cleaned_emails list
        # Use: cleaned_emails.append(cleaned)
        cleaned_emails.append(cleaned)  # Remove this pass and add your code
        
    print("\nCleaned emails:")
    for email in cleaned_emails:
        print(f"  ✓ {email}")


def practice_1c_advanced():
    """
    Advanced: Process multiple data fields
    """
    print("\n" + "="*50)
    print("EXERCISE 1C: Data Processor (Advanced)")
    print("="*50)
    
    user_data = {
        "name": "  JANE DOE  ",
        "email": "  Jane@Email.COM ",
        "username": "  JaNe_DoE_123  ",
        "country": "united states"
    }
    
    print("Original data:")
    for key, value in user_data.items():
        print(f"  {key}: '{value}'")
    
    cleaned_data = {}
    
    # TODO: Clean all fields appropriately
    # Name: strip spaces and use title case
    cleaned_data["name"] = user_data["name"].strip().title()  # Replace with user_data["name"].strip().title()
    
    # Email: strip spaces and lowercase
    cleaned_data["email"] = user_data["email"].strip().title()  # Replace with appropriate methods
    
    # Username: strip spaces and lowercase
    cleaned_data["username"] = user_data["username"].strip().title()  # Replace with appropriate methods
    
    # Country: strip spaces and title case
    cleaned_data["country"] = user_data["country"].strip().title()  # Replace with appropriate methods
    
    print("\nCleaned data:")
    for key, value in cleaned_data.items():
        print(f"  {key}: '{value}'")


# ============================================================
# UNIT 2: String Searching and Checking
# ============================================================

def practice_2a_beginner():
    """
    Beginner: Find words in a sentence
    """
    print("\n" + "="*50)
    print("EXERCISE 2A: Find Words (Beginner)")
    print("="*50)
    
    sentence = "Python programming is really fun and programming is useful"
    print(f"Sentence: {sentence}")
    
    # TODO 1: Check if "Python" is in the sentence
    # Use: "Python" in sentence
    has_python = "Python" in sentence  # Replace None
    
    # TODO 2: Count how many times "programming" appears
    # Use: sentence.count("programming")
    prog_count = sentence.count("programming")  # Replace None
    
    # TODO 3: Find the position of "fun"
    # Use: sentence.find("fun")
    fun_position = sentence.find("fun")  # Replace None
    
    print(f"Contains 'Python': {has_python}")
    print(f"'programming' appears: {prog_count} times")
    print(f"'fun' starts at position: {fun_position}")


def practice_2b_intermediate():
    """
    Intermediate: Check password strength
    """
    print("\n" + "="*50)
    print("EXERCISE 2B: Password Checker (Intermediate)")
    print("="*50)
    
    passwords = ["abc123", "PASSWORD", "Pass123!", "12345678"]
    
    for password in passwords:
        print(f"\nChecking: {password}")
        
        # TODO 1: Check if password has any digits
        has_digit = any(char.isdigit() for char in password)
        
        # TODO 2: Check if password has any uppercase
        has_upper = any(char.isupper() for char in password)  # Replace with any(char.isupper() for char in password)
        
        # TODO 3: Check if password has any lowercase
        has_lower = any(char.islower() for char in password)  # Replace with appropriate check
        
        # TODO 4: Check if length is at least 8
        long_enough = len(password) >= 8  # Replace with len(password) >= 8
        
        print(f"  Has digit: {has_digit}")
        print(f"  Has uppercase: {has_upper}")
        print(f"  Has lowercase: {has_lower}")
        print(f"  Length >= 8: {long_enough}")
        
        # Check if strong (all requirements met)
        if all([has_digit, has_upper, has_lower, long_enough]):
            print("  💪 STRONG PASSWORD")
        else:
            print("  ⚠️ WEAK PASSWORD")


def practice_2c_advanced():
    """
    Advanced: Detect and categorize file types
    """
    print("\n" + "="*50)
    print("EXERCISE 2C: File Type Detector (Advanced)")
    print("="*50)
    
    files = [
        "document.pdf",
        "image.jpg",
        "photo.PNG",
        "script.py",
        "data.CSV",
        "video.mp4",
        "archive.zip",
        "webpage.html"
    ]
    
    # Categories
    documents = []
    images = []
    code = []
    other = []
    
    for filename in files:
        # Convert to lowercase for checking
        lower_name = filename.lower()
        
        # TODO: Categorize files based on extension
        if lower_name.endswith(('.pdf', '.doc', '.txt')):
            documents.append(filename)
        elif lower_name.endswith(('.jpg', '.png', '.gif', '.jpeg')):
            # TODO: Add to images list
            images.append(filename)  # Replace with images.append(filename)
        elif lower_name.endswith(('.py', '.js', '.html', '.css')):
            # TODO: Add to code list
            code.append(filename)  # Replace with code.append(filename)
        else:
            # TODO: Add to other list
            other.append(filename)  # Replace with other.append(filename)
    
    print("📁 File Categories:")
    print(f"Documents: {documents}")
    print(f"Images: {images}")
    print(f"Code files: {code}")
    print(f"Other: {other}")


# ============================================================
# UNIT 3: String Replacement and Splitting
# ============================================================

def practice_3a_beginner():
    """
    Beginner: Replace words in text
    """
    print("\n" + "="*50)
    print("EXERCISE 3A: Word Replacer (Beginner)")
    print("="*50)
    
    story = "The cat sat on the cat mat. The cat was happy."
    print(f"Original: {story}")
    
    # TODO 1: Replace "cat" with "dog"
    # Use: story.replace("cat", "dog")
    dog_story = story.replace("cat", "dog")  # Replace None
    
    # TODO 2: Replace "mat" with "rug"
    # Use the dog_story from above
    final_story = dog_story  # Replace None
    
    # TODO 3: Split the story into sentences (split on ". ")
    # Use: final_story.split(". ")
    sentences = final_story.split(". ")  # Replace None
    
    print(f"After replacing cat: {dog_story}")
    print(f"Final story: {final_story}")
    print(f"Sentences: {sentences}")


def practice_3b_intermediate():
    """
    Intermediate: Process CSV data
    """
    print("\n" + "="*50)
    print("EXERCISE 3B: CSV Processor (Intermediate)")
    print("="*50)
    
    # CSV data as strings
    csv_data = [
        "Alice,Smith,28,Teacher",
        "Bob,Jones,35,Engineer",
        "Carol,White,42,Doctor"
    ]
    
    print("Processing employee data:\n")
    
    employees = []
    for line in csv_data:
        # TODO 1: Split each line by comma
        fields = line.split(", ")  # Replace with line.split(",")
        
        # TODO 2: Create a formatted string
        # Format: "FirstName LastName (Age) - Job"
        if fields:  # Check if fields exists
            formatted = f"{fields[0]} {fields[1]} {fields[2]} - {fields[3]}" # Replace with f"{fields[0]} {fields[1]} ({fields[2]}) - {fields[3]}"
            employees.append(formatted)
    
    # TODO 3: Join all employees with newline
    employee_list = "\n".join(employees)  # Replace with "\n".join(employees)
    
    print("Employee Directory:")
    print(employee_list)


def practice_3c_advanced():
    """
    Advanced: Build a template replacement system
    """
    print("\n" + "="*50)
    print("EXERCISE 3C: Template System (Advanced)")
    print("="*50)
    
    # Email template
    template = """
    Dear {name},
    
    Your appointment is scheduled for {date} at {time}.
    Please arrive at {location}.
    
    Your confirmation code is: {code}
    
    Best regards,
    {company}
    """
    
    # Appointment data
    appointment = {
        "name": "John Smith",
        "date": "Monday, Sept 20",
        "time": "2:00 PM",
        "location": "Main Office",
        "code": "APT-001",
        "company": "MediCare Clinic"
    }
    
    # TODO: Replace all placeholders in template
    email = template
    
    # Replace each placeholder
    email = email.replace("{name}", appointment["name"])
    email = email.replace("{date}", appointment["date"])
    email = email.replace("{time}", appointment["time"])
    email = email.replace("{location}", appointment["location"])
    email = email.replace("{code}", appointment["code"])
    email = email.replace("{company}", appointment["company"])
    # TODO: Continue replacing other placeholders
    # email = email.replace("{time}", appointment["time"])
    # email = email.replace("{location}", appointment["location"])
    # email = email.replace("{code}", appointment["code"])
    # email = email.replace("{company}", appointment["company"])
    
    print(f"Email for {appointment['name']}:")
    print(email)


# ============================================================
# UNIT 4: String Formatting
# ============================================================

def practice_4a_beginner():
    """
    Beginner: Format personal information
    """
    print("\n" + "="*50)
    print("EXERCISE 4A: Info Formatter (Beginner)")
    print("="*50)
    
    # Personal information
    name = "John Doe"
    age = 25
    height = 5.9  # feet
    weight = 170.5  # pounds
    
    # TODO 1: Create f-string with name and age
    # Format: "Name: John Doe, Age: 25"
    info1 = f"Name: {name}, Age: {age}"  # Replace with f"Name: {name}, Age: {age}"
    
    # TODO 2: Format height to 1 decimal place
    # Format: "Height: 5.9 feet"
    info2 = f"Height: {height: .1f} feet"  # Replace with f"Height: {height:.1f} feet"
    
    # TODO 3: Format weight to no decimal places
    # Format: "Weight: 171 lbs"
    info3 = f"Weight: {weight: .0f} lbs"  # Replace with f"Weight: {weight:.0f} lbs"
    
    print(info1)
    print(info2)
    print(info3)


def practice_4b_intermediate():
    """
    Intermediate: Format a grade report
    """
    print("\n" + "="*50)
    print("EXERCISE 4B: Grade Report (Intermediate)")
    print("="*50)
    
    students = [
        {"name": "Alice", "score": 92.5, "grade": "A"},
        {"name": "Bob", "score": 78.3, "grade": "C"},
        {"name": "Charlie", "score": 85.7, "grade": "B"}
    ]
    
    # Print header
    print(f"{'Name':<15} {'Score':>10} {'Grade':>10}")
    print("-" * 35)
    
    for student in students:
        # TODO 1: Format name left-aligned in 15 characters
        name_formatted = f"{student['name']:<15}"  # Replace with f"{student['name']:<15}"
        
        # TODO 2: Format score right-aligned with 1 decimal
        score_formatted = f"{student['score']:>10.1f}"  # Replace with f"{student['score']:>10.1f}"
        
        # TODO 3: Format grade right-aligned in 10 characters
        grade_formatted = f"{student['grade']:>10}"  # Replace with f"{student['grade']:>10}"
        
        # TODO 4: Combine and print all formatted parts
        # Uncomment the next line when ready
        print(f"{name_formatted}{score_formatted}{grade_formatted}")
    
    # Calculate and display average
    avg_score = sum(s["score"] for s in students) / len(students)
    # TODO 5: Format average with 2 decimal places
    print("-" * 35)
    print(f"Class Average: {avg_score:.2f}")


def practice_4c_advanced():
    """
    Advanced: Create a formatted data table
    """
    print("\n" + "="*50)
    print("EXERCISE 4C: Sales Data Table (Advanced)")
    print("="*50)
    
    # Sales data
    sales_data = [
        {"product": "Laptop", "units": 15, "price": 899.99},
        {"product": "Mouse", "units": 45, "price": 29.99},
        {"product": "Keyboard", "units": 28, "price": 79.99}
    ]
    
    # TODO: Create a formatted table
    # Calculate totals for each product
    for item in sales_data:
        item["total"] = item["units"] * item["price"]
    
    # Print header
    print("┌" + "─"*50 + "┐")
    print(f"│{'SALES REPORT':^50}│")
    print("├" + "─"*50 + "┤")
    
    # TODO: Format and print each row
    grand_total = 0
    for item in sales_data:
        # Format each field appropriately
        # Uncomment and complete:
        row = f"│{item['product']:<15}│{item['units']:>8}│${item['price']:>9.2f}│${item['total']:>11.2f}│"
        print(row)
        grand_total += item["total"]
    
    # TODO: Print grand total
    print(f"│{'GRAND TOTAL':>36}│${grand_total:>11.2f}│")


# ============================================================
# UNIT 5: String Slicing and Indexing
# ============================================================

def practice_5a_beginner():
    """
    Beginner: Extract parts of strings
    """
    print("\n" + "="*50)
    print("EXERCISE 5A: String Extraction (Beginner)")
    print("="*50)
    
    # Full name
    full_name = "John Michael Smith"
    print(f"Full name: {full_name}")
    
    # TODO 1: Get the first name (first 4 characters)
    # Use: full_name[:4]
    first_name = full_name[:4]  # Replace None
    
    # TODO 2: Get the last name (last 5 characters)
    # Use: full_name[-5:]
    last_name = full_name[-5:]  # Replace None
    
    # Email address
    email = "user@example.com"
    print(f"\nEmail: {email}")
    
    # TODO 3: Get username (everything before @)
    at_position = email.find("@")
    username = email[:at_position]  # Replace with email[:at_position]
    
    # TODO 4: Get domain (everything after @)
    domain = email[at_position+1:]  # Replace with email[at_position+1:]
    
    print(f"\nExtracted from name:")
    print(f"  First name: {first_name}")
    print(f"  Last name: {last_name}")
    print(f"\nExtracted from email:")
    print(f"  Username: {username}")
    print(f"  Domain: {domain}")


def practice_5b_intermediate():
    """
    Intermediate: Mask sensitive information
    """
    print("\n" + "="*50)
    print("EXERCISE 5B: Credit Card Masker (Intermediate)")
    print("="*50)
    
    # Credit card numbers to mask
    cards = [
        "4532-1234-5678-9012",
        "5412 3456 7890 1234",
        "378234567890123"
    ]
    
    for card in cards:
        print(f"\nOriginal: {card}")
        
        # Remove spaces and dashes
        clean_card = card.replace("-", "").replace(" ", "")
        
        # TODO 1: Get last 4 digits
        last_four = clean_card[-4:]  # Replace with clean_card[-4:]
        
        # TODO 2: Create masked version
        # Show only last 4 digits, mask the rest with *
        if len(clean_card) >= 4:
            masked = "*" * (len(clean_card)-4) + last_four  # Replace with "*" * (len(clean_card) - 4) + last_four
            
            print(f"Masked: {masked}")


def practice_5c_advanced():
    """
    Advanced: Parse structured text data
    """
    print("\n" + "="*50)
    print("EXERCISE 5C: Log File Parser (Advanced)")
    print("="*50)
    
    # Log file entries
    log_entries = [
        "[2024-09-15 10:30:45] INFO: User login successful - user123",
        "[2024-09-15 10:31:02] ERROR: Database connection failed - timeout",
        "[2024-09-15 10:31:15] WARNING: High memory usage - 85%"
    ]
    
    parsed_logs = []
    
    for entry in log_entries:
        # Find the positions of brackets and markers
        timestamp_end = entry.find("]")
        level_start = timestamp_end + 2  # Skip "] "
        level_end = entry.find(":", level_start)
        
        # TODO 1: Extract timestamp (between [ and ])
        timestamp = entry[1:timestamp_end]  # Replace with entry[1:timestamp_end]
        
        # TODO 2: Extract log level (INFO, ERROR, WARNING)
        level = entry[level_start:level_end]  # Replace with entry[level_start:level_end]
        
        # TODO 3: Extract message (everything after level:)
        message = entry[level_end+2:]  # Replace with entry[level_end+2:]
        
        # Store parsed data
        parsed = {
            "timestamp": timestamp,
            "level": level,
            "message": message
            }
        parsed_logs.append(parsed)
    
    # Display parsed data
    print("Parsed Log Entries:\n")
    for log in parsed_logs:
        print(f"Time: {log['timestamp']}")
        print(f"Level: {log['level']}")
        print(f"Message: {log['message']}")
        print("-" * 40)


# ============================================================
# UNIT 6: Putting It All Together
# ============================================================

def practice_6_final_project():
    """
    Final Project: Build a simple text processor
    Combine multiple string operations
    """
    print("\n" + "="*50)
    print("FINAL PROJECT: Text Processor")
    print("="*50)
    
    # Sample text to process
    sample_text = """
      HELLO world!   This is a TEST message.  
    Please   clean   and   FORMAT this text PROPERLY.
    contact us at: ADMIN@COMPANY.COM or call 555-123-4567
    """
    
    print("Original text:")
    print(sample_text)
    print("\n" + "-"*50)
    
    
    # TODO: Implement a complete text processing pipeline
    # Step 1: Clean up whitespace
    # - Remove leading/trailing spaces
    # - Replace multiple spaces with single space

    
    # Step 2: Standardize case
    # - Sentences should be properly capitalized
    # - Email should be lowercase
    
    # Step 3: Extract information
    # - Find and extract the email
    # - Find and extract the phone number
    
    # Step 4: Format output nicely
    
    # Your code here:
    processed_text = sample_text  # Start with original
    
    # Add your processing steps...
    no_spaces_text = processed_text.strip()
    no_spaces_text = len(no_spaces_text)
    no_double_spaces_text = processed_text.replace("  ", " ")
    no_double_spaces_text = len(no_double_spaces_text)
    sentences_format = processed_text.upper()
    sentences_format = len(sentences_format)
    email_format = processed_text.lower()
    email_format = len(email_format)
    email = processed_text.find("@")
    email = len(email)
    phone_number = processed_text.find("number")
    phone_number = len(phone_number)
    
    
    print("\nProcessed text:")
    print(processed_text)


# ============================================================
# MAIN PROGRAM - Run all exercises
# ============================================================

def main():
    """
    Main program to run exercises
    Uncomment the exercises you want to run
    """
    print("="*60)
    print("CS1350 - Week 5: Advanced String Operations")
    print("="*60)
    
    # UNIT 1 Exercises
    practice_1a_beginner()
    practice_1b_intermediate()
    practice_1c_advanced()
    
    # UNIT 2 Exercises
    practice_2a_beginner()
    practice_2b_intermediate()
    practice_2c_advanced()
    
    # UNIT 3 Exercises
    practice_3a_beginner()
    practice_3b_intermediate()
    practice_3c_advanced()
    
    # UNIT 4 Exercises
    practice_4a_beginner()
    practice_4b_intermediate()
    practice_4c_advanced()
    
    # UNIT 5 Exercises
    practice_5a_beginner()
    practice_5b_intermediate()
    practice_5c_advanced()
    
    # UNIT 6 Final Project
    practice_6_final_project()
    
    print("\n" + "="*60)
    print("End of exercises. Great work!")
    print("="*60)


# Run the program
if __name__ == "__main__":
    main()