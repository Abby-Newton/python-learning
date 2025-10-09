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