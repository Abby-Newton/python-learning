def practice_1_beginner():
    """
    Beginner: Convert text to CSV
    """
    print("\n" + "="*50)
    print("EXERCISE 1.1: Text to CSV Converter")
    print("="*50)
    # Create a text file with data
    with open("employees.txt", "w") as employees:
        employees.write("John Smith 35 Engineer\n")
        employees.write("Jane Doe 28 Designer\n")
        employees.write("Bob Johnson 42 Manager\n")
    # TODO 1: Read text file and convert to CSV
    with open("employees.txt", "r") as employees:
        with open("employees.csv", "w") as employees_csv:
            # Write CSV header
            employees_csv.write("First,Last,Age,Job\n")
            # TODO: Read each line and convert
            for line in employees:
                parts = line.strip().split()
                # parts[0] = first name, parts[1] = last name, etc.
                # TODO: Write as CSV line
                # Format: John,Smith,35,Engineer
                csv_line = f"{parts[0]},{parts[1]},{parts[2]},{parts[3]}" # Replace with comma-separated values
                employees_csv.write(csv_line + "\n")
    # TODO 2: Read and verify CSV
    print("\nCSV Contents:")
    with open("employees.csv", "r") as employees_csv:
        # TODO: Read and display
        for line in employees_csv:
            print(line.strip())
# Run the exercise
practice_1_beginner()


def practice_1_intermediate():
    """
    Intermediate: Process CSV data
    """
    print("\n" + "="*50)
    print("EXERCISE 1.2: Grade Calculator")
    print("="*50)
    # Create grades CSV
    with open("grades.csv", "w") as grades:
        grades.write("Student,Math,Science,English\n")
        grades.write("Alice,95,87,92\n")
        grades.write("Bob,78,85,88\n")
        grades.write("Charlie,92,94,85\n")
        grades.write("Diana,88,91,95\n")
    # TODO 1: Read CSV and calculate averages
    with open("grades.csv", "r") as grades:
        header = grades.readline().strip().split(",")
        print(f"Subjects: {header[1:]}")
        student_averages = []
        for line in grades:
            parts = line.strip().split(",")
            name = parts[0]
            # TODO: Convert grades to numbers
            grades = list(map(int, parts[1:])) # Convert parts[1:] to integers
            # TODO: Calculate average
            average = sum(grades)/len(grades) # Calculate average grade
            student_averages.append((name, average))
            print(f"{name}: {average:.1f}")
    # TODO 2: Save results to new CSV
    with open("averages.csv", "w") as averages:
        averages.write("Student,Average\n")
        # TODO: Write each student's average
        for name, avg in student_averages:
            averages.write(f"{name},{avg:.1f}\n")
# Run the exercise
practice_1_intermediate()


def practice_1_advanced():
    """
    Advanced: JSON database system
    """
    print("\n" + "="*50)
    print("EXERCISE 1.3: JSON Database")
    print("="*50)
    import json
    # TODO 1: Create a product database in JSON
    products = {
        "inventory": [
            {"id": 1, "name": "Laptop", "price": 999.99, "stock": 5},
            {"id": 2, "name": "Mouse", "price": 29.99, "stock": 15},
            {"id": 3, "name": "Keyboard", "price": 79.99, "stock": 8}
        ],
        "last_updated": "2024-01-15",
        "store": "Tech Store"
    }
    # TODO: Save to JSON
    with open("products.json", "w") as file:
        json.dump(products, file, indent=4)
    print("Product database created")
    # TODO 2: Load and modify JSON
    with open("products.json", "r") as file:
        data = json.load(file)
    # Add a new product
    new_product = {
        "id": 4,
        "name": "Monitor",
        "price": 299.99,
        "stock": 3
    }
    # TODO: Add to inventory
    data["inventory"].append(new_product)
    print("New Product added")
    # TODO 3: Update stock levels
    for item in data["inventory"]:
        if item["name"]=="Laptop":
            item["stock"]-= 1
        if item["name"]=="Mouse":
            item["stock"]+=2
    data["last_updated"]="2025-10-20"
    # TODO 4: Save updated data
    with open("products.json", "w") as products:
        # TODO: Save the modified data
        json.dump(data,products,indent=4)
    print("Product database updated and saved")
    # TODO 5: Generate report from JSON
    print("\nInventory Report:")
    for item in data["inventory"]:
        print(f"{item['name']}: ${item['price']}(Stock: {item['stock']})")
# Run the exercise
practice_1_advanced()


def practice_2_beginner():
    """
    Beginner: Basic JSON operations
    """
    print("\n" + "="*50)
    print("EXERCISE 2.1: JSON Contact Card")
    print("="*50)
    import json
    # TODO 1: Create a contact dictionary
    contacts = {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "555-1234",
        "age": 25
    }
    # TODO 2: Convert to JSON string
    json_str = json.dumps(contacts) # Replace with json.dumps(contact)
    print(f"JSON String: {json_str}")
    # TODO 3: Save to file
    with open("contacts.json", "w") as contact:
        # TODO: Use json.dump to save contact
        json.dump(contacts,contact)
    print("Contact saved to file")
    # TODO 4: Load from file
    with open("contacts.json", "r") as contact:
        loaded_contact = json.load(contact) # Replace with json.load(f)
    # TODO 5: Access data
    print(f"\nLoaded contact:")
    print(f"Name: {loaded_contact['name']}")
    print(f"Email: {loaded_contact['email']}")
# Run the exercise
practice_2_beginner()


def practice_2_intermediate():
    """
    Intermediate: Application settings in JSON
    """
    print("\n" + "="*50)
    print("EXERCISE 2.2: Settings Manager")
    print("="*50)
    import json
    # Default settings
    default_settings = {
        "app_name": "My App",
        "version": "1.0.0",
        "user_preferences": {
        "theme": "dark",
        "font_size": 12,
        "auto_save": True
        },
        "recent_files": [],
        "window_size": [800, 600]
    }
    # TODO 1: Save default settings
    with open("settings.json", "w") as settings_json:
        # TODO: Save with nice formatting
        json.dump(default_settings, settings_json, indent=4)
    print("Default settings created")
    # TODO 2: Load and modify settings
    with open("settings.json", "r") as settings_json:
        settings = json.load(settings_json)
    settings["user_preferences"]["theme"] = "light"
    settings["user_preferences"]["font_size"] = 14
    settings["recent_files"].append("project1.txt")
    settings["version"]="1.1.0"
    # TODO 3: Save updated settings
    with open("settings.json", "w") as settings_json:
        # TODO: Save updated settings
        json.dump(settings, settings_json, indent=4)
    print("Updated settings saved")
    # TODO 4: Create backup
    with open("settings.json", "r") as settings_json:
        updated_settings = settings_json.read()
    with open("settings_backup.json", "w") as settings_backup:
        settings_backup.write(updated_settings)
    print("Settings backed up")
# Run the exercise
practice_2_intermediate()


def practice_2_advanced():
    """
    Advanced: Mini database with JSON
    """
    print("\n" + "="*50)
    print("EXERCISE 2.3: Student Database")
    print("="*50)
    import json
    # TODO 1: Create database structure
    database = {
        "metadata": {
            "record_count": 0
        },
        "students": {}
    }
    # TODO 2: Add students function
    def add_student(db, student_id, name, grades):
        gpa = sum(grades)/len(grades)
        db["students"][str(student_id)] = {
            "name": name,
            "grades": grades,
            "gpa": gpa
        }
        db["metadata"]["record_count"] += 1
    # Add sample students
    add_student(database, 1001, "Alice", [95, 87, 92, 88])
    add_student(database, 1002, "Bob", [78, 85, 80, 82])
    add_student(database, 1003, "Charlie", [92, 94, 96, 91])
    # TODO 3: Save database
    with open("student_db.json", "w") as db_file:
        json.dump(database, db_file, indent=4)
    print("Database created")
    # TODO 4: Query function
    def find_student(db_file, student_id):
        with open(db_file, "r") as file:
            data = json.load(file)
            return data["students"].get(str(student_id))
    # Test query
    result = find_student("student_db.json", 1001)
    if result:
        print(f"\nFound: {result['name']}")
        print(f"GPA: {result['gpa']:.2f}")
    # TODO 5: Generate report
    with open("student_db.json", "r") as student_db:
        db = json.load(student_db)
    report = {
        "total_students": db["metadata"]["record_count"],
        "high_achievers": [],
        "needs_support": []
    }
    for sid, student in db["students"].items():
        # update report
        if student["gpa"] >= 90:
            report["high_achievers"].append(student["name"])
        elif student["gpa"] < 80:
            report["needs_support"].append(student["name"])
    # Save report
    with open("report.json", "w") as report_json:
        json.dump(report, report_json, indent=4)
    print(f"\n📊 Report generated:")
    print(f"High achievers: {report['high_achievers']}")
    print(f"Needs support: {report['needs_support']}")
# Run the exercise
practice_2_advanced()