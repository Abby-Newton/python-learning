# Required import for all problems
import re

# Optional: For timing in Problem 6
import time

def problem1():
    """
    Extract information using regex groups.
    """
    # a) Extract date components from various date formats
    dates_text = """
    Important dates:
        - Project due: 2024-03-15
        - Meeting on: 12/25/2024
        - Holiday: July 4, 2025
    """
    # TODO: Write a pattern that captures dates in format YYYY-MM-DD
    pattern_iso = r"\b\d{4}-\d{2}-\d{2}\b" # Your pattern here
    # TODO: Extract all ISO format dates (YYYY-MM-DD)
    iso_dates = re.findall(pattern_iso, dates_text) # Use re.findall
    # b) Parse email addresses and extract username and domain
    emails_text = "Contact john.doe@example.com or alice_smith@university.edu for info"
    # TODO: Write pattern with named groups for username and domain
    pattern_email = r"(?P<username>[\w\._]+)@(?P<domain>[\w\.-]+\.\w+)" # Use (?P<name>...) syntax
    # TODO: Extract all emails with their components
    email_parts = [] # List of dictionaries with 'username' and 'domain' keys
    for match in re.finditer(pattern_email, emails_text):
        email_parts.append({
            'username': match.group('username'),
            'domain': match.group('domain')})
    # c) Extract phone numbers with area codes
    phones_text = "Call (555) 123-4567 or 800-555-1234 for support"
    # TODO: Write pattern to capture area code and number separately
    pattern_phone = r"(?:\((\d{3})\)|(\d{3}))[-\s]?(\d{3}-\d{4})" # Capture area code in group 1, rest in group 2
    # TODO: Extract all phone numbers as tuples (area_code, number)
    phone_numbers = [] # List of tuples
    for match in re.finditer(pattern_phone, phones_text):
        area_code = match.group(1) if match.group(1) else match.group(2)
        number = match.group(3)
        phone_numbers.append((area_code, number))
    # d) Find repeated words in text
    repeated_text = "The the quick brown fox jumped over the the lazy dog"
    # TODO: Write pattern to find consecutive repeated words
    pattern_repeated = r"\b(\w+)\s+\1\b" # Hint: Use backreference \1
    # TODO: Find all repeated words
    repeated_words = [match.group(1).lower() for match in re.finditer(pattern_repeated, repeated_text, flags=re.IGNORECASE)] # List of repeated words (just the word, not the duplicate)
    return {
        'iso_dates': iso_dates,
        'email_parts': email_parts,
        'phone_numbers': phone_numbers,
        'repeated_words': repeated_words
    }
# Test your function
# Expected outputs:
# iso_dates: ['2024-03-15']
# email_parts: [{'username': 'john.doe', 'domain': 'example.com'}, ...]
# phone_numbers: [('555', '123-4567'), ('800', '555-1234')]
# repeated_words: ['the', 'the']

def problem2():
    """
    Use alternation to create flexible patterns.
    """
    # a) Match different file extensions
    files_text = """
    Documents: report.pdf, notes.txt, presentation.pptx
    Images: photo.jpg, diagram.png, icon.gif, picture.jpeg
    Code: script.py, program.java, style.css
    """
    # TODO: Pattern to match image files (jpg, jpeg, png, gif)
    pattern_images = r"\b[\w\-]+\.(?:jpg|jpeg|png|gif)\b" # Use alternation
    # TODO: Find all image filenames
    image_files = [re.findall(pattern_images, files_text, flags=re.IGNORECASE)] # Complete filenames with extensions
    # b) Match different date formats
    mixed_dates = "Meeting on 2024-03-15 or 03/15/2024 or March 15, 2024"
    # TODO: Pattern to match all three date formats using alternation
    pattern_dates = r"\b(?:\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4})\b" # Match ISO, US, and text formats
    # TODO: Find all dates regardless of format
    all_dates = [re.findall(pattern_dates, mixed_dates)]
    # c) Extract prices in different formats
    prices_text = "$19.99, USD 25.00, 30 dollars, €15.50, £12.99"
    # TODO: Pattern to match prices with different currency symbols
    pattern_prices = r"(?:\$|USD |€|£)?\d+(?:\.\d{2})? ?(?:dollars)?" # Match $, USD, dollars, €, £
    # TODO: Extract all prices with their currency indicators
    prices = [re.findall(pattern_prices, prices_text, flags=re.IGNORECASE)] # List of matched price strings
    # d) Match programming language mentions
    code_text = """
    We use Python for data science, Java for enterprise apps,
    JavaScript or JS for web development, and C++ or CPP for systems.
    """
    # TODO: Pattern to match language names and their abbreviations
    pattern_langs = r"\b(?:Python|Java|JavaScript|JS|C\+\+|CPP)\b" # Match full names and common abbreviations
    # TODO: Find all programming language mentions
    languages = [re.findall(pattern_langs, code_text, flags=re.IGNORECASE)] # Include both full names and abbreviations
    return {
        'image_files': image_files,
        'all_dates': all_dates,
        'prices': prices,
        'languages': languages
    }

def problem3():
    """
    Practice with findall() and finditer() methods.
    """
    log_text = """
    [2024-03-15 10:30:45] INFO: Server started on port 8080
    [2024-03-15 10:31:02] ERROR: Connection failed to database
    [2024-03-15 10:31:15] WARNING: High memory usage detected (85%)
    [2024-03-15 10:32:00] INFO: User admin logged in from 192.168.1.100
    [2024-03-15 10:32:30] ERROR: File not found: config.yml
    """
    # a) Use findall() to extract all timestamps
    # TODO: Pattern for timestamp [YYYY-MM-DD HH:MM:SS]
    pattern_timestamp = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]"
    # TODO: Extract all timestamps
    matches = re.findall(pattern_timestamp, log_text)
    timestamps = [ts.strip("[]") for ts in matches] # Using findall()
    # b) Use findall() with groups to extract log levels and messages
    # TODO: Pattern with groups for log level and message
    pattern_log = r"\] (\w+): (.+)" # Capture level and message separately
    # TODO: Extract tuples of (level, message)
    log_entries = re.findall(pattern_log, log_text) # List of tuples using findall()
    # c) Use finditer() to get positions of all IP addresses
    # TODO: Pattern for IP addresses
    pattern_ip = r"\b(?:\d{1,3}\.){3}\d{1,3}\b" # Match IPv4 addresses
    # TODO: Find all IP addresses with their positions
    ip_addresses = [] # List of dicts with 'ip', 'start', 'end' keys
    for match in re.finditer(pattern_ip, log_text):
        ip_addresses.append({
            'ip': match.group(),
            'start': match.start(),
            'end': match.end()
        })
    # d) Use finditer() to create a highlighted version of errors
    # TODO: Replace ERROR entries with **ERROR** (highlighted)
    highlighted_log = log_text # Modified version with highlighted errors
    # TODO: Create function to highlight all ERROR entries
    def highlight_errors(text):
        """
        Surround all ERROR log entries with ** markers.
        Return modified text.
        """
        #Your implementation here
        result = []
        last_pos = 0
        pattern_error_line = r".*ERROR:.*(?:\n|$)"
        for match in re.finditer(pattern_error_line, text):
            start, end = match.span()
            result.append(text[last_pos:start])
            result.append("**" + match.group().rstrip() + "**\n")
            last_pos = end
        result.append(text[last_pos:])
        return "".join(result)
    highlighted_log = highlight_errors(log_text)
    return {
        'timestamps': timestamps,
        'log_entries': log_entries,
        'ip_addresses': ip_addresses,
        'highlighted_log': highlighted_log
    }

def problem4():
    """
    Practice text transformation using re.sub().
    """
    # a) Clean and format phone numbers
    messy_phones = """
    Contact list:
        - John: 555.123.4567
        - Jane: (555) 234-5678
        - Bob: 555 345 6789
        - Alice: 5554567890
    """
    # TODO: Standardize all phone numbers to format: (555) 123-4567
    def standardize_phones(text):
        """
        Convert all phone number formats to (XXX) XXX-XXXX.
        """
        # Your pattern and substitution here
        pattern = r"""
        \(?(\d{3})\)?      # area code, optional parentheses
        [\s\.\-]?          # optional separator (space, dot, dash)
        (\d{3})            # first 3 digits
        [\s\.\-]?          # optional separator
        (\d{4})            # last 4 digits"""
        replacement = r"(\1) \2-\3"
        return re.sub(pattern, replacement, text)
    cleaned_phones = standardize_phones(messy_phones)
    # b) Redact sensitive information
    sensitive_text = """
    Customer: John Doe
    SSN: 123-45-6789
    Credit Card: 4532-1234-5678-9012
    Email: john.doe@email.com
    Phone: (555) 123-4567
    """
    # TODO: Redact SSN and Credit Card numbers
    def redact_sensitive(text):
        """
        Replace SSN with XXX-XX-XXXX and
        Credit Card with XXXX-XXXX-XXXX-XXXX.
        """
        # Your implementation here
        text = re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "XXX-XX-XXXX", text)
        text = re.sub(r"\b\d{4}-\d{4}-\d{4}-\d{4}\b", "XXXX-XXXX-XXXX-XXXX", text)
        return text # Modified text
    redacted_text = redact_sensitive(sensitive_text)
    # c) Convert markdown links to HTML
    markdown_text = """
    Check out [Google](https://google.com) for search.
    Visit [GitHub](https://github.com) for code.
    Read documentation at [Python Docs](https://docs.python.org).
    """
    # TODO: Convert [text](url) to <a href="url">text</a>
    def markdown_to_html(text):
        """
        Convert markdown links to HTML anchor tags.
        """
        # Your pattern and substitution here
        pattern = r"\[([^\]]+)\]\(([^)]+)\)"
        replacement = r'<a href="\2">\1</a>'
        return re.sub(pattern, replacement, text)
        return text # Modified text
    html_text = markdown_to_html(markdown_text)
    # d) Implement a simple template system
    template = """
    Dear {name},
    Your order #{order_id} for {product} has been shipped.
    Tracking number: {tracking}
    """
    values = {
        'name': 'John Smith',
        'order_id': '12345',
        'product': 'Python Book',
        'tracking': 'TRK789XYZ'
    }
    # TODO: Replace {key} with corresponding values
    def fill_template(template, values):
        """
        Replace all {key} placeholders with values from dictionary.
        """
        # Your implementation here
        pattern = r"\{(\w+)\}"
        def replacer(match):
            key = match.group(1)
            return values.get(key, match.group(0))  
        return re.sub(pattern, replacer, template)
    filled_template = fill_template(template, values)
    return {
        'cleaned_phones': cleaned_phones,
        'redacted_text': redacted_text,
        'html_text': html_text,
        'filled_template': filled_template
    }

def problem5():
    """
    Use compiled patterns for efficiency and clarity.
    """
    # Create a class to hold compiled patterns
    class PatternLibrary:
        """
        Library of compiled regex patterns for common use cases.
        """
        # TODO: Compile these patterns
        # Use re.IGNORECASE, re.MULTILINE, re.VERBOSE as appropriate
        # a) Email validation pattern (case insensitive)
        EMAIL = re.compile(
            r"^[\w\.-]+@[\w\.-]+\.\w{2,}$",
            re.IGNORECASE
        ) # re.compile(...)
        # b) URL pattern (with optional protocol)
        URL = re.compile(
            r"^(https?://)?(www\.)?[\w-]+(\.[\w-]+)+(/[\w./?%&=-]*)?$",
            re.IGNORECASE
        ) # re.compile(...)
        # c) US ZIP code (5 digits or 5+4 format)
        ZIP_CODE = re.compile(
            r"^\d{5}(-\d{4})?$"
        ) # re.compile(...)
        # d) Strong password (verbose pattern with comments)
        # Requirements: 8+ chars, uppercase, lowercase, digit, special char
        PASSWORD = re.compile(r"""
            ^                   # start of string
            (?=.*[a-z])         # at least one lowercase letter
            (?=.*[A-Z])         # at least one uppercase letter
            (?=.*\d)            # at least one digit
            (?=.*[!@#$%^&*(),.?":{}|<>_\-+=~`])  # at least one special character
            .{8,}               # at least 8 characters long
            $                   # end of string
        """, re.VERBOSE) # re.compile(..., re.VERBOSE)
        # e) Credit card number (with spaces or dashes optional)
        CREDIT_CARD = re.compile(
            r"^(?:\d{4}[- ]?){3}\d{4}$"
        ) # re.compile(...)
    # Test your patterns
    test_data = {
        'emails': ['valid@email.com', 'invalid.email', 'user@domain.co.uk'],
        'urls': ['https://example.com', 'www.test.org', 'invalid://url'],
        'zips': ['12345', '12345-6789', '1234', '123456'],
        'passwords': ['Weak', 'Strong1!Pass', 'nouppercas3!', 'NoDigits!'],
        'cards': ['1234 5678 9012 3456', '1234-5678-9012-3456',
        '1234567890123456']
    }
    # TODO: Validate each item using your compiled patterns
    validation_results = {
    'emails': [bool(PatternLibrary.EMAIL.fullmatch(email)) for email in test_data['emails']], # List of booleans
    'urls': [bool(PatternLibrary.URL.fullmatch(url)) for url in test_data['urls']], # List of booleans
    'zips': [bool(PatternLibrary.ZIP_CODE.fullmatch(zip_code)) for zip_code in test_data['zips']], # List of booleans
    'passwords': [bool(PatternLibrary.PASSWORD.fullmatch(pw)) for pw in test_data['passwords']], # List of booleans
    'cards': [bool(PatternLibrary.CREDIT_CARD.fullmatch(card.replace(' ', '').replace('-', ''))) for card in test_data['cards']] # List of booleans
    }
    # TODO: Implement validation logic
    # For each category, check if pattern matches
    return validation_results

def problem6():
    """
    Create a log file analyzer using regex.
    """
    # Sample web server log (Apache/Nginx format)
    log_data = """
    192.168.1.1 - - [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200
    5234
    192.168.1.2 - - [15/Mar/2024:10:30:46 +0000] "POST /api/login HTTP/1.1" 401
    234
    192.168.1.1 - - [15/Mar/2024:10:30:47 +0000] "GET /images/logo.png HTTP/1.1"
    304 0
    192.168.1.3 - - [15/Mar/2024:10:30:48 +0000] "GET /admin/dashboard HTTP/1.1"
    403 0
    192.168.1.2 - - [15/Mar/2024:10:30:49 +0000] "POST /api/login HTTP/1.1" 200
    1234
    192.168.1.4 - - [15/Mar/2024:10:30:50 +0000] "GET /products HTTP/1.1" 200
    15234
    192.168.1.1 - - [15/Mar/2024:10:30:51 +0000] "GET /contact HTTP/1.1" 404 0
    """
    # TODO: Parse log entries to extract:
    # - IP address
    # - Timestamp
    # - HTTP method (GET, POST, etc.)
    # - URL path
    # - Status code
    # - Response size
    # a) Create pattern to parse log lines
    lines = [line.strip() for line in log_data.strip().splitlines() if line.strip()]
    log_pattern = re.compile(
        r'^(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - '
        r'\[(?P<timestamp>[^\]]+)\] '
        r'"(?P<method>\w+) '
        r'(?P<path>\S+) '
        r'HTTP/[\d.]+" '
        r'(?P<status>\d{3})?'
        r'(?:\s(?P<extra_status>\d+))?' 
    ) # Your comprehensive pattern here
    response_size_pattern = re.compile(r'^(\d+)(?:\s+(\d+))?$')
    # b) Extract all log entries as structured data
    parsed_logs = [] # List of dictionaries
    for i in range(0, len(lines), 2):
        first_line = lines[i]
        second_line = lines[i+1] if i+1 < len(lines) else ''

        m = log_pattern.match(first_line)
        if not m:
            continue
        m_size = response_size_pattern.match(second_line)
        if m_size:
             size = int(m_size.group(1))
        else:
            size = 0
        entry = {
            'ip': m.group('ip'),
            'timestamp': m.group('timestamp'),
            'method': m.group('method'),
            'path': m.group('path'),
            'status': int(m.group('status')) if m.group('status') else None,
            'response_size': size
        }
        parsed_logs.append(entry)
    # c) Analyze the logs
    analysis = {
        'total_requests': 0,
        'unique_ips': [],
        'error_count': 0, # 4xx and 5xx status codes
        'total_bytes': 0,
        'most_requested_path': '',
        'methods_used': [] # Unique HTTP methods
    }
    # TODO: Implement log parsing and analysis
    paths = [entry['path'] for entry in parsed_logs if entry['path']]
    if paths:
        freq = {}
        for path in paths:
            freq[path] = freq.get(path, 0) + 1
        most_common_path = max(freq, key=freq.get)
        analysis['most_requested_path'] = most_common_path
    return {
        'parsed_logs': parsed_logs,
        'analysis': analysis
    }

def bonus_challenge():
    """
    Convert markdown formatting to HTML.
    Support: **bold**, *italic*, [links](url), # headers
    """
    markdown = """
    # Main Header
    This is a **bold** word and this is *italic*.
    Check out [this link](https://example.com).
    ## Subheader
    Another paragraph with **multiple** *formatting* options.
    """
    # TODO: Implement markdown to HTML conversion
    # Handle headers, bold, italic, and links
    html_lines = []
    for line in markdown.strip().split('\n'):
        line = line.strip()
        if line.startswith('## '):
            content = line[3:].strip()
            line = f"<h2>{content}</h2>"
        elif line.startswith('# '):
            content = line[2:].strip()
            line = f"<h1>{content}</h1>"
        else:
            line = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", line)
            line = re.sub(r"\*(.+?)\*", r"<em>\1</em>", line)
            line = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', line)
            line = f"<p>{line}</p>"
        html_lines.append(line)
    html_output = "" # Your converted HTML
    return html_output

# Add this at the bottom of your file to test all problems
if __name__ == "__main__":
    print("Problem 1 Results:")
    print(problem1())
    print("\nProblem 2 Results:")
    print(problem2())
    print("\nProblem 3 Results:")
    print(problem3())
    print("\nProblem 4 Results:")
    print(problem4())
    print("\nProblem 5 Results:")
    print(problem5())
    print("\nProblem 6 Results:")
    print(problem6())
    #print("\nProblem 7 Results:")
    #print(problem7())
    # Uncomment if attempting bonus
    print("\nBonus Challenge Results:")
    print(bonus_challenge())