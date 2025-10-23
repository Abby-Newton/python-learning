def practice_1_beginner():
    """
    Beginner: Understanding why we need files
    """
    print("\n" + "="*50)
    print("EXERCISE 1.1: Save Your Name")
    print("="*50)
    # TODO 1: Get user's name
    name = input("Enter your name: ")
    # TODO 2: Open a file called "myname.txt" for writing
    # Hint: Use open("myname.txt", "w")
    file = open("myname.txt", "w") # Replace None with open() function
    # TODO 3: Write the name to the file
    # Hint: Use file.write(name)
    file.write(str(name))
    # TODO 4: Close the file
    # Hint: Use file.close()
    file.close()
    print(f"Name '{name}' saved to myname.txt!")
    # TODO 5: Read it back
    # Open the file for reading with "r" mode
    file = open("myname.txt", "r") # Replace with open() for reading
    # Read the content
    saved_name = file.read() # Replace with file.read()
    # Close the file
    file.close()
    print(f"Read back: '{saved_name}'")
# Run the exercise
practice_1_beginner()


def practice_1_intermediate():
    """
    Intermediate: Create a settings saver
    """
    print("\n" + "="*50)
    print("EXERCISE 1.2: Settings Manager")
    print("="*50)
    # Game settings to save
    username = input("Enter username: ")
    difficulty = input("Enter difficulty (easy/medium/hard): ")
    sound = input("Sound on? (yes/no): ")
    # TODO 1: Save all settings to "settings.txt"
    # Open file for writing
    file = open("settings.txt", "w") # Replace with open("settings.txt", "w")
    # TODO 2: Write each setting on a new line
    # Write username, then newline, then difficulty, etc.
    # Hint: file.write(username + "\n")
    file.write(username + "\n")
    file.write(difficulty + "\n")
    file.write(sound + "\n")
    # TODO 3: Close the file
    file.close()
    print("Settings saved!")
    # TODO 4: Load settings back
    file = open("settings.txt", "r")
    saved_file = file.read()
    file.close()
    print("\nLoading settings...")
# Run the exercise
practice_1_intermediate()


def practice_1_advanced():
    """
    Advanced: Build a persistent counter system
    """
    print("\n" + "="*50)
    print("EXERCISE 1.3: Persistent Counter")
    print("="*50)
    counter_file_name = "counter.txt"
    # TODO 1: Check if counter file exists and load value
    counter_file = open(counter_file_name, "r")
    counter = int(counter_file.read())
    counter_file.close()
    print(f"Loaded existing counter: {counter}")
    # TODO 2: Increment counter
    counter += 1
    print(f"Incremented to: {counter}")
    # TODO 3: Save updated counter
    # Your code here to save counter
    visits = counter
    # TODO 4: Create a visit log
    # Append to a file called "visits.txt"
    # Include timestamp (you can use a simple counter as timestamp)
    visit_file = open("visits.txt", "a") # "a" for append
    # Write something like "Visit #1\n"
    # TODO 5: Read and display last 5 visits
    saved_file = visit_file.read
    visit_file.close()
    print("\nLast visits:")
# Read visits.txt and show last 5 lines
# Run the exercise
practice_1_advanced()


def practice_2_beginner():
    """
    Beginner: Work with file objects
    """
    print("\n" + "="*50)
    print("EXERCISE 2.1: File Object Basics")
    print("="*50)
    # TODO 1: Create a text file with 3 lines
    number_text = open("numbers.txt", "w")
    # Write three numbers, each on a new line
    number_text.write("10\n")
    number_text.write("20\n")
    number_text.write("30\n")
    # TODO: Write 20 and 30
    number_text.close()
    # TODO 2: Open the file and check its properties
    number_text = open("numbers.txt", "r")
    # Print file name
    print(f"File name: {number_text.name}")
    # TODO: Print file mode
    # Hint: Use file.mode
    print(f"File mode: {number_text.mode}")
    # TODO: Check if file is closed
    # Hint: Use file.closed
    print(f"Is file closed? {number_text.closed}")
    # TODO 3: Read one line at a time until EOF
    while True:
        line = number_text.readline()
        if line == "": # Check for EOF
            print("Reached end!")
            break
        print(f"Read: {line.strip()}")
    number_text.close()
    print(f"Is file closed now? {number_text.closed}")
# Run the exercise
practice_2_beginner()


def practice_2_intermediate():
    """
    Intermediate: Track file position
    """
    print("\n" + "="*50)
    print("EXERCISE 2.2: File Position Tracking")
    print("="*50)
    # Create a file with alphabet
    alphabet_file = open("alphabet.txt", "w")
    alphabet_file.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alphabet_file.close()
    # TODO 1: Open and read specific positions
    alphabet_file = open("alphabet.txt", "r")
    # Read first 5 characters
    chunk1 = alphabet_file.read(5)
    print(f"First 5: {chunk1}")
    # TODO 2: Check current position
    position = alphabet_file.tell() # Replace with file.tell()
    print(f"Current position: {position}")
    #   TODO 3: Read next 5 characters
    chunk2 = alphabet_file.read(5) # Replace with file.read(5)
    print(f"Next 5: {chunk2}")
    # TODO 4: Check position again
    # Your code here
    position2 = alphabet_file.tell()
    print(f"New position: {position2}")
    # TODO 5: Read until EOF
    remaining = alphabet_file.read() # Read the rest
    print(f"Remaining: {remaining}")
    alphabet_file.close()
# Run the exercise
practice_2_intermediate()


def practice_2_advanced():
    """
    Advanced: Work with multiple files
    """
    print("\n" + "="*50)
    print("EXERCISE 2.3: Multi-File Log System")
    print("="*50)
    from datetime import datetime
    def timestamped(msg):
        return f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {msg}\n"
    # TODO 1: Create three different log files
    info_log = open("info.log", "w")
    error_log = open("error.log", "w")
    debug_log = open("debug.log", "w")
    # TODO 2: Write appropriate messages to each
    # Info log: Normal operations
    info_log.write("System started\n")
    info_log.write(timestamped("User login successful"))
    info_log.write(timestamped("File upload complete"))
    # TODO: Add more info messages
    # Error log: Problems
    error_log.write(timestamped("Failed to connect to database"))
    error_log.write(timestamped("Permission denied when accessing /etc/passwd"))
    # TODO: Write error messages
    # Debug log: Detailed information
    debug_log.write(timestamped("Debug mode enabled"))
    debug_log.write(timestamped("Variable x = 42"))
    debug_log.write(timestamped("Loop completed after 10 iterations"))
    # TODO: Write debug information
    # TODO 3: Close all files
    # Your code here
    info_log.close()
    error_log.close()
    debug_log.close()
    # TODO 4: Create a master log reader
    print("\n📊 Log Summary:")
    # Read and count lines in each log
    for log_name in ["info.log", "error.log", "debug.log"]:
        log_file = open(log_name, "r")
        lines = log_file.readlines()
        log_file.close()
        print(f"{log_name}: {len(lines)} entries")
    # TODO 5: Show first line of each log
    if lines:
        print(f" First entry: {lines[0].strip()}")
# Run the exercise
practice_2_advanced()


def practice_3_beginner():
    """
    Beginner: Basic file operations
    """
    print("\n" + "="*50)
    print("EXERCISE 3.1: Student Grades File")
    print("="*50)
    # TODO 1: Write student grades to file
    grades_file = open("grades.txt", "w")
    # Write these grades (each on new line):
    # Alice: 90
    # Bob: 85
    # Charlie: 92
    grades_file.write("Alice: 90\n")
    # TODO: Write Bob and Charlie
    grades_file.close()
    print("Grades written!")
    # TODO 2: Read the file using read()
    grades_file = open("grades.txt", "r")
    content = None # Replace with file.read()
    print(f"\nAll grades:\n{content}")
    grades_file.close()
    # TODO 3: Read line by line
    print("\nReading line by line:")
    grades_file = open("grades.txt", "r")
    # TODO: Use readline() three times
    line1 = None # First student
    line2 = None # Second student
    line3 = None # Third student
    print(f"Student 1: {line1}")
    print(f"Student 2: {line2}")
    print(f"Student 3: {line3}")
    grades_file.close()
# Run the exercise
practice_3_beginner()


def practice_3_intermediate():
    """
    Intermediate: Update and append files
    """
    print("\n" + "="*50)
    print("EXERCISE 3.2: Todo List Manager")
    print("="*50)
    # TODO 1: Create initial todo list
    todos = [
        "Buy groceries\n",
        "Study Python\n",
        "Exercise\n"
        ]
    todo_file = open("todo.txt", "w")
    # TODO: Use writelines() to write todos
    todo_file.writelines(todos)
    todo_file.close()
    print("Initial todos created!")
    # TODO 2: Read and display with numbers
    todo_file = open("todo.txt", "r")
    lines = None # Replace with readlines()
    todo_file.close()
    print("\nCurrent Todo List:")
    for i, task in enumerate(lines, 1):
        print(f"{i}. {task.strip()}")
    # TODO 3: Append new tasks
    new_task = input("\nAdd a task: ")
    todo_file = open("todo.txt", "a") # Append mode
    # TODO: Write the new task with newline
    todo_file.close()
    # TODO 4: Show updated list
    print("\nUpdated Todo List:")
    # Read and display again
# Run the exercise
practice_3_intermediate()


def practice_3_advanced():
    """
    Advanced: Use seek for file navigation
    """
    print("\n" + "="*50)
    print("EXERCISE 3.3: Random Access File")
    print("="*50)
    # Create a file with position markers
    positions_file = open("positions.txt", "w")
    positions_file.write("0123456789" * 5) # 50 characters
    positions_file.close()
    # TODO 1: Read specific ranges using seek
    positions_file = open("positions.txt", "r")
    # Read characters 0-9
    chunk1 = positions_file.read(10)
    print(f"Chars 0-9: {chunk1}")
    #TODO 2: Jump to position 20 and read 10 chars
    positions_file.seek(20)
    chunk2 = None # Replace with read(10)
    print(f"Chars 20-29: {chunk2}")
    # TODO 3: Get current position
    current = None # Replace with file.tell()
    print(f"Current position: {current}")
    # TODO 4: Go back to beginning
    # Use seek(0)
    # TODO 5: Create a "bookmark" system
    bookmarks = {}
    # Save positions
    positions_file.seek(10)
    bookmarks["chapter1"] = positions_file.tell()
    positions_file.seek(25)
    bookmarks["chapter2"] = positions_file.tell()
    positions_file.seek(40)
    bookmarks["chapter3"] = positions_file.tell()
    print(f"\nBookmarks: {bookmarks}")
    # Jump to bookmarks
    for name, position in bookmarks.items():
        positions_file.seek(position)
        content = positions_file.read(5)
        print(f"{name} (pos {position}): {content}")
    positions_file.close()
# Run the exercise
practice_3_advanced()


def practice_4_beginner():
    """
    Beginner: Convert to with statements
    """
    print("\n" + "="*50)
    print("EXERCISE 4.1: Using With Statement")
    print("="*50)
    # TODO 1: Rewrite using 'with'
    # Old way:
    # file = open("hello.txt", "w")
    # file.write("Hello World!")
    # file.close()
    # New way with 'with':
    with open("hello.txt", "w") as hello_file:
        # TODO: Write "Hello World!"
        pass # Replace with file.write()
        print("File written with 'with'!")
        # TODO 2: Read using 'with'
        # Complete this:
    with open("hello.txt", "r") as hello_file:
        content = None # Replace with file.read()
        print(f"Content: {content}")
        # TODO 3: Append using 'with'
        with open("hello.txt", "a") as hello_file:
        # TODO: Add " Python is fun!"
            pass
        # TODO 4: Verify the complete content
    with open("hello.txt", "r") as hello_file:
        # TODO: Read and print everything
        pass
# Run the exercise
practice_4_beginner()


def practice_4_intermediate():
    """
    Intermediate: File copying with 'with'
    """
    print("\n" + "="*50)
    print("EXERCISE 4.2: Safe File Copy")
    print("="*50)
    # Create source file
    with open("source.txt", "w") as source_file:
        source_file.write("Important data line 1\n")
        source_file.write("Important data line 2\n")
        source_file.write("Important data line 3\n")
        print("Source file created")
        # TODO 1: Copy file using nested 'with'
        # Read from source.txt and write to backup.txt
    with open("source.txt", "r") as source:
        with open("backup.txt", "w") as backup:
            # TODO: Read all content from source
            content = None # Replace with source.read()
            # TODO: Write to backup
            # backup.write(content)
            print("File copied!")
            # TODO 2: Verify copy using single 'with' for multiple files
    with open("source.txt", "r") as source, open("backup.txt", "r") as backup:
        src_content = None # TODO: Read source
        bak_content = None # TODO: Read backup
    if src_content == bak_content:
        print("✓ Copy successful!")
    else:
        print("✗ Copy failed!")
    # TODO 3: Line-by-line copy with line numbers
    with open("source.txt", "r") as source:
        with open("numbered.txt", "w") as numbered:
            for i, line in enumerate(source, 1):
                # TODO: Write line with number
                # Format: "1: Important data line 1\n"
                pass
# Run the exercise
practice_4_intermediate()


def practice_4_advanced():
    """
    Advanced: Multi-file log processing
    """
    print("\n" + "="*50)
    print("EXERCISE 4.3: Log Analysis System")
    print("="*50)
    # Create sample log files
    with open("app.log", "w") as log:
        log.write("[INFO] Application started\n")
        log.write("[ERROR] Connection failed\n")
        log.write("[INFO] Retrying connection\n")
        log.write("[WARNING] Low memory\n")
        log.write("[INFO] Connection established\n")
        log.write("[ERROR] Data corruption detected\n")
        # TODO 1: Process log and separate by type
    errors = []
    warnings = []
    info = []
    with open("app.log", "r") as log:
        for line in log:
        # TODO: Check line type and categorize
            if "[ERROR]" in line:
                errors.append(line)
                # TODO: Add similar for WARNING and INFO
        # TODO 2: Write categorized logs using multiple files
    with open("errors.log", "w") as err_log, \
        open("warnings.log", "w") as warn_log, \
        open("info.log", "w") as info_log:
        # TODO: Write each list to appropriate file
        # err_file.writelines(errors)
        # etc.
        pass
    print(f"Processed: {len(errors)} errors, {len(warnings)} warnings, {len(info)} info")
    # TODO 3: Create summary report
    with open("summary.txt", "w") as summary:
        summary.write("Log Analysis Summary\n")
        summary.write("=" * 30 + "\n")
        # TODO: Write statistics
        # Total entries, error count, etc.
    # TODO: Include first error if any
    if errors:
        summary.write(f"\nFirst error: {errors[0]}")
        # TODO 4: Read and display summary
    with open("summary.txt", "r") as summary:
        print("\n📊 Summary Report:")
        print(summary.read())
# Run the exercise
practice_4_advanced()


def practice_5_beginner():
    """
    Beginner: Simple contact list
    """
    print("\n" + "="*50)
    print("EXERCISE 5.1: Contact List")
    print("="*50)
    # TODO 1: Create contacts file
    with open("contacts.txt", "w") as contacts:
        contacts.write("My Contacts\n")
        contacts.write("-" * 20 + "\n")
    # TODO 2: Add three contacts
    contacts = [
        "Alice: 555-1234",
        "Bob: 555-5678",
        "Charlie: 555-9012"
        ]
    with open("contacts.txt", "a") as contacts:
        # TODO: Write each contact
        for contact in contacts:
            pass # Replace with f.write()
    # TODO 3: Read and display all contacts
    print("\n📞 Contact List:")
    with open("contacts.txt", "r") as contacts:
        # TODO: Read and print all lines
        pass
    # TODO 4: Search for a contact
    search_name = "Bob"
    found = False
    with open("contacts.txt", "r") as contacts:
        for line in contacts:
            if search_name in line:
                print(f"\nFound: {line.strip()}")
                found = True
                break
    if not found:
        print(f"{search_name} not found")
# Run the exercise
practice_5_beginner()



def practice_5_intermediate():
    """
    Intermediate: Todo list application
    """
    print("\n" + "="*50)
    print("EXERCISE 5.2: Todo App")
    print("="*50)
    def init_todo():
        """Initialize todo file"""
        with open("todos.txt", "w") as todos:
            todos.write("TODO LIST\n")
            todos.write("=" * 30 + "\n")
    def add_task(task):
        """Add a task"""
        # TODO: Implement adding task with timestamp
        with open("todos.txt", "a") as todos:
            # Add format: "[ ] Task description"
            pass
    def complete_task(task_num):
        """Mark task as complete"""
        # TODO: Read all lines
        with open("todos.txt", "r") as todos:
            lines = todos.readlines()
            # TODO: Update the specified task
            # Change "[ ]" to "[X]" for task_num
            # TODO: Write back
        with open("todos.txt", "w") as todos:
            todos.writelines(lines)
    def show_tasks():
        """Display all tasks"""
        print("\n📝 Tasks:")
        with open("todos.txt", "r") as todos:
            # Skip headers
            todos.readline()
            todos.readline()
            # TODO: Display tasks with numbers
            task_num = 1
            for line in todos:
                if line.strip():
                    print(f"{task_num}. {line.strip()}")
                    task_num += 1
    # Test the app
    init_todo()
    add_task("Study Python")
    add_task("Exercise")
    add_task("Read book")
    show_tasks()
    # Complete a task
    complete_task(2)
    show_tasks()
# Run the exercise
practice_5_intermediate()


def practice_5_advanced():
    """
    Advanced: Sales data analyzer
    """
    print("\n" + "="*50)
    print("EXERCISE 5.3: Sales Analyzer")
    print("="*50)
    # Create sample sales data
    with open("sales.txt", "w") as sales:
        sales.write("Date,Product,Amount\n")
        sales.write("2024-01-01,Laptop,999.99\n")
        sales.write("2024-01-01,Mouse,29.99\n")
        sales.write("2024-01-02,Keyboard,79.99\n")
        sales.write("2024-01-02,Laptop,999.99\n")
        sales.write("2024-01-03,Monitor,299.99\n")
        sales.write("2024-01-03,Mouse,29.99\n")
    # TODO 1: Read and parse sales data
    sales = []
    with open("sales.txt", "r") as sales:
        sales.readline() # Skip header
        for line in sales:
            # TODO: Split by comma and store
            parts = line.strip().split(",")
            if len(parts) == 3:
                sales.append({
                    "date": parts[0],
                    "product": parts[1],
                    "amount": float(parts[2])
                    })
    # TODO 2: Calculate statistics
    total_sales = sum(s["amount"] for s in sales)
    num_transactions = len(sales)
    # TODO 3: Find product totals
    product_totals = {}
    for sale in sales:
        product = sale["product"]
        amount = sale["amount"]
        if product in product_totals:
            product_totals[product] += amount
        else:
            product_totals[product] = amount
    # TODO 4: Generate report
    with open("sales_report.txt", "w") as sales_report:
        sales_report.write("SALES REPORT\n")
        sales_report.write("=" * 40 + "\n\n")
        sales_report.write(f"Total Sales: ${total_sales:.2f}\n")
        sales_report.write(f"Transactions: {num_transactions}\n")
        sales_report.write(f"Average Sale: ${total_sales/num_transactions:.2f}\n\n")
        sales_report.write("Product Summary:\n")
        sales_report.write("-" * 30 + "\n")
        for product, total in product_totals.items():
            sales_report.write(f"{product}: ${total:.2f}\n")
    # TODO 5: Display report
    print("\n📈 Sales Report Generated:")
    with open("sales_report.txt", "r") as sales_report:
        print(sales_report.read())
# Run the exercise
practice_5_advanced()