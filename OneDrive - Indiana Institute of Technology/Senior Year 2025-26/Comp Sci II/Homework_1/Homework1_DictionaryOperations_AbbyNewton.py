# Example contact structure
contact = {
    'first_name': 'John',
    'last_name': 'Doe',
    'phone': '555-123-4567',
    'email': 'john.doe@email.com',
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'ST',
        'zip_code': '12345'
    },
    'category': 'personal', # 'personal', 'work', 'family'
    'notes': 'Met at conference',
    'created_date': '2024-01-15',
    'last_modified': '2024-01-15'
}

# Contact database structure
contacts_db = {
    'contact_001': {contact},
    'contact_002': {contact},
    # ... more contacts
}

def add_contact(contacts_db, contact_data):
    """
    Add a new contact to the database.
    Generate unique ID and add contact with proper validation.
    Args:
        contacts_db (dict): The main contacts database
        contact_data (dict): Contact information dictionary
    Returns:
        str: The generated contact ID, or None if addition failed
    """
    import uuid
    required_fields = ['name', 'email']
    if not all(field in contact_data and contact_data[field] for field in required_fields):
        return None
    contact_id = str(uuid.uuid4())
    contacts_db[contact_id] = contact_data
    return contact_id
pass

def display_contact(contacts_db, contact_id):
    """
    Display a formatted view of a single contact.
    Args:
        contacts_db (dict): The main contacts database
        contact_id (str): Unique identifier for the contact
    Returns:
        bool: True if contact found and displayed, False otherwise
    """
    contact = contacts_db.get(contact_id)
    if not contact:
        print(f"Contact ID '{contact_id}' not found.")
        return False
    print("Contact Information")
    print("-" * 20)
    print(f"ID: {contact_id}")
    for key, value in contact.items():
        print(f"{key.capitalize()}: {value}")
    print("-" * 20)
pass

def list_all_contacts(contacts_db):
    """
    Display a summary list of all contacts (ID, name, phone).
    Args:
        contacts_db (dict): The main contacts database
    """
    if not contacts_db:
        print("No contacts found.")
        return
    print("All Contacts Summary")
    print("-" * 40)
    print(f"{'ID':<18} {'Name':<15} {'Phone':<15}")
    print("-" * 40)
    for contact_id, contact in contacts_db.items():
        name = contact.get('name', 'N/A')
        phone = contact.get('phone', 'N/A')
        print(f"{contact_id[:16]:<18} {name:<15} {phone:<15}")
    print("-" * 40)
pass

def search_contacts_by_name(contacts_db, search_term):
    """
    Search contacts by first or last name (case-insensitive partial match).
    Args:
        contacts_db (dict): The main contacts database
        search_term (str): Name to search for
    Returns:
        dict: Dictionary of matching contacts {contact_id: contact_data}
    """
    if not search_term:
        return {}
    search_term = search_term.lower()
    results = {}
    for contact_id, contact in contacts_db.items():
        name = contact.get('name', '')
        if search_term in name.lower():
            results[contact_id] = contact
    return results
pass

def search_contacts_by_category(contacts_db, category):
    """
    Find all contacts in a specific category.
    Args:
        contacts_db (dict): The main contacts database
        category (str): Category to filter by
    Returns:
        dict: Dictionary of matching contacts
    """
    if not category:
        return {}
    category = category.lower()
    results = {}
    for contact_id, contact in contacts_db.items():
        contact_category = contact.get('category', '').lower()
        if contact_category == category:
            results[contact_id] = contact
    return results
pass

def find_contact_by_phone(contacts_db, phone_number):
    """
    Find contact by phone number (exact match).
    Args:
        contacts_db (dict): The main contacts database
        phone_number (str): Phone number to search for
    Returns:
        tuple: (contact_id, contact_data) if found, (None, None) if not found
    """
    for contact_id, contact in contacts_db.items():
        if contact.get('phone') == phone_number:
            return contact_id, contact
    return None, None
pass

def update_contact(contacts_db, contact_id, field_updates):
    """
    Update specific fields of an existing contact.
    Automatically update last_modified timestamp.
    Args:
        contacts_db (dict): The main contacts database
        contact_id (str): Contact to update
        field_updates (dict): Dictionary of fields to update
    Returns:
        bool: True if update successful, False otherwise
    """
    contact = contacts_db.get(contact_id)
    if not contact:
        return False  
    for field, value in field_updates.items():
        contact[field] = value
    from datetime import datetime
    contact['last_modified'] = datetime.now().isoformat()
    return True
pass

def delete_contact(contacts_db, contact_id):
    """
    Remove a contact from the database with confirmation.
    Args:
        contacts_db (dict): The main contacts database
        contact_id (str): Contact to delete
    Returns:
        bool: True if deletion successful, False otherwise
    """
    if contact_id not in contacts_db:
        print(f"Contact ID '{contact_id}' not found.")
        return False
    contact = contacts_db[contact_id]
    name = contact.get('name', 'Unknown')
    confirmation = input(f"Are you sure you want to delete '{name}' (ID: {contact_id})? [y/N]: ").strip().lower()
    if confirmation == 'y':
        del contacts_db[contact_id]
        print(f"Contact '{name}' has been deleted.")
        return True
    else:
        print("Deletion canceled.")
        return False
pass

def merge_contacts(contacts_db, contact_id1, contact_id2):
    """
    Merge two contacts, keeping the most recent information.
    Prompt user for conflicts in overlapping fields.
    Args:
        contacts_db (dict): The main contacts database
        contact_id1 (str): First contact ID
        contact_id2 (str): Second contact ID
    Returns:
        str: ID of the merged contact, or None if merge failed
    """
    contact1 = contacts_db.get(contact_id1)
    contact2 = contacts_db.get(contact_id2)
    if not contact1 or not contact2:
        print("One or both contact IDs not found.")
        return None
    merged_contact = {}
    def parse_timestamp(ts):
        if not ts:
            return 0
        try:
            import time
            time_struct = time.strptime(ts, '%Y-%m-%dT%H:%M:%S')
            return time.mktime(time_struct)
        except Exception:
            return 0
    all_keys = set(contact1.keys()) | set(contact2.keys())
    for key in all_keys:
        val1 = contact1.get(key)
        val2 = contact2.get(key)
        if val1 == val2:
            merged_contact[key] = val1
        elif val1 is None:
            merged_contact[key] = val2
        elif val2 is None:
            merged_contact[key] = val1
        else:
            print(f"Conflict in field '{key}':")
            print(f"1: {val1}")
            print(f"2: {val2}")
            choice = input("Choose value (1 or 2): ").strip()
            while choice not in ('1', '2'):
                choice = input("Please enter '1' or '2': ").strip()
            merged_contact[key] = val1 if choice == '1' else val2
    import time
    merged_contact['last_modified'] = time.strftime('%Y-%m-%dT%H:%M:%S')
    contacts_db[contact_id1] = merged_contact
    del contacts_db[contact_id2]
    print(f"Contacts merged into ID '{contact_id1}'.")
    return contact_id1
pass

def generate_contact_statistics(contacts_db):
    """
    Generate comprehensive statistics about the contact database.
    Args:
        contacts_db (dict): The main contacts database
    Returns:
        dict: Statistics including:
            - total_contacts: int
            - contacts_by_category: dict
            - contacts_by_state: dict (from address)
            - average_contacts_per_category: float
            - most_common_area_code: str
            - contacts_without_email: int
    """
    from collections import Counter, defaultdict
import re

def generate_contacts_stats(contacts_db):
    """
    Generate comprehensive statistics about the contact database.

    Args:
        contacts_db (dict): The main contacts database

    Returns:
        dict: Statistics including:
            - total_contacts: int
            - contacts_by_category: dict
            - contacts_by_state: dict (from address)
            - average_contacts_per_category: float
            - most_common_area_code: str
            - contacts_without_email: int
    """
    total_contacts = len(contacts_db)
    from collections import defaultdict
    contacts_by_category = defaultdict(int)
    contacts_by_state = defaultdict(int)
    contacts_without_email = 0
    from collections import Counter
    area_code_counter = Counter()
    area_code_pattern = re.compile(r'\(?(\d{3})\)?[-.\s]?\d{3}[-.\s]?\d{4}')
    for contact in contacts_db.values():
        category = contact.get('category', '').strip().lower()
        if category:
            contacts_by_category[category] += 1
        else:
            contacts_by_category['uncategorized'] += 1
        address = contact.get('address', '')
        state_match = re.search(r'\b([A-Z]{2})\b', address)
        if state_match:
            state = state_match.group(1)
            contacts_by_state[state] += 1
        else:
            contacts_by_state['unknown'] += 1
        if not contact.get('email'):
            contacts_without_email += 1
        phone = contact.get('phone', '')
        area_code_match = area_code_pattern.search(phone)
        if area_code_match:
            area_code_counter[area_code_match.group(1)] += 1
    num_categories = len(contacts_by_category)
    average_contacts_per_category = (total_contacts / num_categories) if num_categories else 0.0
    most_common_area_code = None
    if area_code_counter:
        most_common_area_code = area_code_counter.most_common(1)[0][0]
    return {
        'total_contacts': total_contacts,
        'contacts_by_category': dict(contacts_by_category),
        'contacts_by_state': dict(contacts_by_state),
        'average_contacts_per_category': average_contacts_per_category,
        'most_common_area_code': most_common_area_code,
        'contacts_without_email': contacts_without_email}
pass

def find_duplicate_contacts(contacts_db):
    """
    Identify potential duplicate contacts based on:
        - Same phone number
        - Same email address
        - Same first+last name combination
    Args:
        contacts_db (dict): The main contacts database
    Returns:
        dict: Dictionary with duplicate types as keys and lists of contact IDs as values
    Example: {
            'phone_duplicates': [['contact_001', 'contact_003']],
            'email_duplicates': [['contact_002', 'contact_005']],
            'name_duplicates': [['contact_001', 'contact_004']]
    }
    """
    def collect_duplicates(mapping):
        return [ids for ids in mapping.values() if len(ids) > 1]
    from collections import defaultdict
    phone_map = defaultdict(list)
    email_map = defaultdict(list)
    name_map = defaultdict(list)
    for contact_id, contact in contacts_db.items():
        phone = contact.get('phone', '').strip().lower()
        email = contact.get('email', '').strip().lower()
        first_name = contact.get('first_name', '').strip().lower()
        last_name = contact.get('last_name', '').strip().lower()
        if phone:
            phone_map[phone].append(contact_id)
        if email:
            email_map[email].append(contact_id)
        if first_name and last_name:
            full_name = f"{first_name} {last_name}"
            name_map[full_name].append(contact_id)
    return {
        'phone_duplicates': collect_duplicates(phone_map),
        'email_duplicates': collect_duplicates(email_map),
        'name_duplicates': collect_duplicates(name_map),}
pass

def export_contacts_by_category(contacts_db, category):
    """
    Export contacts from a specific category as a formatted string.
    Include all contact information in a readable format.
    Args:
        contacts_db (dict): The main contacts database
        category (str): Category to export
    Returns:
        str: Formatted string representation of all contacts in category
    """
    category = category.strip().lower()
    filtered_contacts = [
        (cid, data) for cid, data in contacts_db.items()
        if data.get('category', '').strip().lower() == category
    ]
    if not filtered_contacts:
        return f"No contacts found in category '{category}'."
    lines = [f"Contacts in category '{category}':\n"]
    for contact_id, contact in filtered_contacts:
        lines.append(f"Contact ID: {contact_id}")
        for key, value in contact.items():
            lines.append(f"  {key.capitalize()}: {value}")
        lines.append("") 
    return "\n".join(lines)
pass

def main_menu():
    """
    Display and handle the main menu for the contact management system.
    Should include options for:
        1. Add new contact
        2. Search contacts
        3. List all contacts
        4. Update contact
        5. Delete contact
        6. Generate statistics
        7. Find duplicates
        8. Export by category
        9. Exit
    """
    while True:
        print("\nContact Management System")
        print("1. Add new contact")
        print("2. Search contacts")
        print("3. List all contacts")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Generate statistics")
        print("7. Find duplicates")
        print("8. Export by category")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ").strip()
        if choice == '1':
            print("Add new contact selected.")
        elif choice == '2':
            print("Search contacts selected.")
        elif choice == '3':
            print("List all contacts selected.")
        elif choice == '4':
            print("Update contact selected.")
        elif choice == '5':
            print("Delete contact selected.")
        elif choice == '6':
            print("Generate statistics selected.")
        elif choice == '7':
            print("Find duplicates selected.")
        elif choice == '8':
            print("Export by category selected.")
        elif choice == '9':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 9.")
pass

def run_contact_manager():
    """
    Main function to run the contact management system.
    Initialize empty database and start the menu loop.
    """
    contacts_db = {} 
    main_menu()  
if __name__ == "__main__":
    main_menu()
pass

def save_contacts_to_file(contacts_db, filename):
    """
    Save contacts database to a text file in a readable format.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for contact_id, contact in contacts_db.items():
            f.write(f"Contact ID: {contact_id}\n")
            for key, value in contact.items():
                f.write(f"  {key.capitalize()}: {value}\n")
            f.write("\n")
pass

def load_contacts_from_file(filename):
    """
    Load contacts database from a text file.
    Return empty dict if file doesn't exist.
    """
    import os
    if not os.path.exists(filename):
        return {}
    contacts_db = {}
    with open(filename, 'r', encoding='utf-8') as f:
        contact_id = None
        contact_data = {}
        for line in f:
            line = line.strip()
            if not line:
                if contact_id:
                    contacts_db[contact_id] = contact_data
                    contact_id = None
                    contact_data = {}
                continue
            if line.startswith("Contact ID:"):
                if contact_id:
                    contacts_db[contact_id] = contact_data
                contact_id = line[len("Contact ID:"):].strip()
                contact_data = {}
            else:
                if ':' in line:
                    key, value = line.split(':', 1)
                    contact_data[key.strip().lower()] = value.strip()
        if contact_id:
            contacts_db[contact_id] = contact_data
    return contacts_db
pass

def test_create_contact():
    """Test contact creation with valid and invalid data."""
    contacts_db = {}
    valid_contact = {
        'first_name': 'John',
        'last_name': 'Doe',
        'phone': '123-456-7890',
        'email': 'john.doe@example.com',
        'category': 'friends'
    }
    contact_id = add_contact(contacts_db, valid_contact)
    assert contact_id is not None, "Failed to add valid contact"
    assert contact_id in contacts_db, "Contact ID not found in database"
    invalid_contact = {
        'first_name': 'Jane',
        'last_name': 'Smith',
        'email': 'jane.smith@example.com',
        'category': 'family'
    }
    contact_id_invalid = add_contact(contacts_db, invalid_contact)
    assert contact_id_invalid is None, "Invalid contact should not be added"
    print("All tests passed.")
pass

def test_search_functionality():
    """Test all search functions with various scenarios."""
    contacts_db = {
        'c1': {'first_name': 'Alice', 'last_name': 'Smith', 'phone': '123-456-7890', 'email': 'alice@example.com', 'category': 'work'},
        'c2': {'first_name': 'Bob', 'last_name': 'Jones', 'phone': '555-123-4567', 'email': 'bob@example.com', 'category': 'family'},
        'c3': {'first_name': 'Alice', 'last_name': 'Johnson', 'phone': '123-555-7890', 'email': 'alicej@example.com', 'category': 'friends'},
    }
    results = search_contacts_by_name(contacts_db, 'alice')
    assert 'c1' in results and 'c3' in results, "Failed to find both Alice contacts"
    assert len(results) == 2, "Unexpected number of search results for 'alice'"
    results = search_contacts_by_name(contacts_db, 'SMITH')
    assert 'c1' in results and len(results) == 1, "Search by last name failed"
    def search_contact_by_phone(contacts_db, phone_number):
        for contact_id, contact in contacts_db.items():
            if contact.get('phone') == phone_number:
                return contact_id, contact
        return None, None
    contact_id, contact = search_contact_by_phone(contacts_db, '555-123-4567')
    assert contact_id == 'c2', "Failed to find Bob by phone"
    contact_id, contact = search_contact_by_phone(contacts_db, '000-000-0000')
    assert contact_id is None and contact is None, "Non-existent phone should return None"
    def find_contacts_by_category(contacts_db, category):
        category = category.strip().lower()
        return {
            cid: data for cid, data in contacts_db.items()
            if data.get('category', '').strip().lower() == category
        }
    results = find_contacts_by_category(contacts_db, 'work')
    assert 'c1' in results and len(results) == 1, "Failed to find contacts by category 'work'"
    results = find_contacts_by_category(contacts_db, 'nonexistent')
    assert len(results) == 0, "Nonexistent category should return empty dict"
    print("All search function tests passed.")
pass

def test_contact_operations():
    """Test add, update, delete operations."""
    contacts_db = {}
    contact_data = {
        'first_name': 'Jane',
        'last_name': 'Doe',
        'phone': '111-222-3333',
        'email': 'jane.doe@example.com',
        'category': 'friends'
    }
    contact_id = add_contact(contacts_db, contact_data)
    assert contact_id is not None, "Failed to add contact"
    assert contact_id in contacts_db, "Contact not found after addition"
    updates = {'phone': '999-888-7777'}
    updated = update_contact(contacts_db, contact_id, updates)
    assert updated, "Update operation failed"
    assert contacts_db[contact_id]['phone'] == '999-888-7777', "Phone not updated correctly"
    deleted = delete_contact(contacts_db, contact_id)
    assert deleted, "Delete operation failed"
    assert contact_id not in contacts_db, "Contact still present after deletion"
    print("Add, update, and delete tests passed.")
pass

def test_data_analysis():
    """Test statistics and duplicate detection."""
    contacts_db = {
        'c1': {
            'first_name': 'Alice',
            'last_name': 'Smith',
            'phone': '123-456-7890',
            'email': 'alice@example.com',
            'category': 'work',
            'address': {'state': 'CA'}
        },
        'c2': {
            'first_name': 'Bob',
            'last_name': 'Jones',
            'phone': '555-123-4567',
            'email': 'bob@example.com',
            'category': 'family',
            'address': {'state': 'NY'}
        },
        'c3': {
            'first_name': 'Alice',
            'last_name': 'Smith',
            'phone': '123-456-7890',  # Duplicate phone
            'email': 'alice.smith@example.com',
            'category': 'work',
            'address': {'state': 'CA'}
        },
        'c4': {
            'first_name': 'Charlie',
            'last_name': 'Brown',
            'phone': '111-222-3333',
            'email': '',
            'category': 'friends',
            'address': {'state': 'TX'}}}
    from collections import Counter
    def generate_statistics(contacts_db):
        total_contacts = len(contacts_db)
        categories = [contact.get('category', '').strip().lower() for contact in contacts_db.values()]
        contacts_by_category = dict(Counter(filter(None, categories)))
        states = []
        for contact in contacts_db.values():
            address = contact.get('address', {})
            if isinstance(address, dict):
                state = address.get('state', '').strip().upper()
                if state:
                    states.append(state)
        contacts_by_state = dict(Counter(states))
        avg_contacts_per_category = (
            sum(contacts_by_category.values()) / len(contacts_by_category) if contacts_by_category else 0.0
            )
        area_codes = []
        for contact in contacts_db.values():
            phone = contact.get('phone', '')
            area_code = None
            if phone:
                import re
                match = re.match(r'\(?(\d{3})\)?[-.\s]?', phone)
                if match:
                    area_code = match.group(1)
            if area_code:
                area_codes.append(area_code)
        most_common_area_code = Counter(area_codes).most_common(1)
        most_common_area_code = most_common_area_code[0][0] if most_common_area_code else None
        #contacts_wihout_email = sum(1 for contact in contacts_db.values() if not contact.get('email'))
        return {
        'total_contacts': total_contacts,
        'contacts_by_category': contacts_by_category,
        'contacts_by_state': contacts_by_state,
        'average_contacts_per_category': avg_contacts_per_category,
        'most_common_area_code': most_common_area_code,
        #'contacts_without_email': contacts_without_email
    }
    stats = generate_statistics(contacts_db)
    assert stats['total_contacts'] == 4, "Incorrect total contacts"
    assert stats['contacts_by_category'].get('work', 0) == 2, "Incorrect contacts by category"
    assert stats['contacts_by_state'].get('CA', 0) == 2, "Incorrect contacts by state"
    assert stats['contacts_without_email'] == 1, "Incorrect count of contacts without email"
    from collections import defaultdict
    def find_duplicates(contacts_db):
        phone_map = defaultdict(list)
        email_map = defaultdict(list)
        name_map = defaultdict(list)
        for cid, contact in contacts_db.items():
            phone = contact.get('phone')
            if phone:
                phone_map[phone].append(cid)
            email = contact.get('email')
            if email:
                email_map[email.lower()].append(cid)  # case-insensitive email
            first = contact.get('first_name', '').strip().lower()
            last = contact.get('last_name', '').strip().lower()
            if first and last:
                full_name = f"{first} {last}"
                name_map[full_name].append(cid)
        def filter_duplicates(d):
            return [ids for ids in d.values() if len(ids) > 1]
        return {
            'phone_duplicates': filter_duplicates(phone_map),
            'email_duplicates': filter_duplicates(email_map),
            'name_duplicates': filter_duplicates(name_map)}
    duplicates = find_duplicates(contacts_db)
    assert any({'c1', 'c3'} <= set(group) for group in duplicates.get('phone_duplicates', [])), "Failed to detect phone duplicates"
    assert any({'c1', 'c3'} <= set(group) for group in duplicates.get('name_duplicates', [])), "Failed to detect name duplicates"
    assert 'email_duplicates' in duplicates and len(duplicates['email_duplicates']) == 0, "Unexpected email duplicates found"
    print("Statistics and duplicate detection tests passed.")
pass

def run_all_tests():
    """Run all test functions and report results."""
    tests = [add_contact, 
            display_contact, 
            list_all_contacts, 
            search_contacts_by_name, 
            search_contacts_by_category, 
            find_contact_by_phone, 
            update_contact, 
            delete_contact, 
            merge_contacts, 
            generate_contact_statistics, 
            generate_contacts_stats, 
            find_duplicate_contacts, 
            export_contacts_by_category, 
            main_menu, 
            run_contact_manager, 
            save_contacts_to_file, 
            load_contacts_from_file, 
            test_create_contact, 
            test_search_functionality, 
            test_contact_operations, 
            test_data_analysis]
    for test_func in tests:
        try:
            test_func()
            print(f"{test_func.__name__}: PASSED")
        except AssertionError as e:
            print(f"{test_func.__name__}: FAILED - {e}")
        except Exception as e:
            print(f"{test_func.__name__}: ERROR - {e}")
pass

# Example of expected program flow
contacts = {}
# Add some test contacts
contact1_id = add_contact(contacts, {
    'first_name': 'Alice',
    'last_name': 'Johnson',
    'phone': '555-123-4567',
    'email': 'alice@email.com',
    'category': 'work'
    })
# Search and display
results = search_contacts_by_name(contacts, 'Alice')
for contact_id, contact_data in results.items():
    display_contact(contacts, contact_id)
# Generate statistics
stats = generate_contact_statistics(contacts)
print(f"Total contacts: {stats['total_contacts']}")