import re
# No other imports allowed
# All regex patterns must use raw strings (r"pattern")
# Test your code with the provided test cases

def format_receipt(items, prices, quantities):
    """
    Create a formatted receipt using string methods.
    Args:
        items: List of item names
        prices: List of prices (floats)
        quantities: List of quantities (integers)
    Returns:
        str: Formatted receipt with aligned columns
    Format Requirements:
        - Item name: left-aligned, 20 characters
        - Quantity: center-aligned, 5 characters
        - Price: right-aligned, 8 characters with 2 decimal places
        - Total: right-aligned at bottom
        - Use dashes for separator lines
    Example:
        >>> items = ["Coffee", "Sandwich", "Cookie"]
        >>> prices = [3.50, 8.99, 2.00]
        >>> quantities = [2, 1, 3]
        >>> print(format_receipt(items, prices, quantities))
        ========================================
        Item            Qty             Price
        ========================================
        Coffee          2               $ 7.00
        Sandwich        1               $ 8.99
        Cookie          3               $ 6.00
        ========================================
        TOTAL                           $ 21.99
        ========================================
    """
    header = "========================================" + "\n"
    title = f"{'item':<20}{'qty':^5}{'price':>14}\n"
    midline = "========================================" + "\n"
    lines = [header, title, midline]
    total = 0.00
    for item, qty, price in zip(items, quantities, prices):
        totline = price * qty
        total += totline
        line = f"{'item':<20}{str(qty):^5}{'$':>3}{totline:>7.2f}\n"
        lines.append(line)
    lines.append(midline)
    totline = f"total{'':>27}{'$':>3}{total:>7.2f}\n"
    lines.append(totline)
    lines.append(midline)
    return "".join(lines)
pass

def process_user_data(raw_data):
    """
    Clean and process user input data using string methods.
    Args:
        raw_data: Dictionary with messy user input
            - 'name': May have extra spaces, wrong capitalization
            - 'email': May have spaces, uppercase letters
            - 'phone': May have various formats
            - 'address': May have inconsistent formatting
    Returns:
        dict: Cleaned data with:
            - 'name': Properly capitalized, trimmed
            - 'email': Lowercase, no spaces
            - 'phone': Digits only
            - 'address': Title case, single spaces
            - 'username': Generated from name (first_last)
            - 'validation': Dict of validation results
    Example:
        >>> data = {
        ... 'name': ' john DOE ',
        ... 'email': ' JOHN.DOE @EXAMPLE.COM ',
        ... 'phone': '(555) 123-4567',
        ... 'address': '123 main street, apt 5'
        ... }
        >>> result = process_user_data(data)
        >>> result['name']
        'John Doe'
        >>> result['email']
        'john.doe@example.com'
        >>> result['phone']
        '5551234567'
        >>> result['username']
        'john_doe'
    """
    cleaned = {}
    name = raw_data.get('name', '').strip()
    cleaned['name'] = ' '.join(word.capitalize() for word in name.split())
    cleaned['email'] = raw_data.get('email', '').replace(' ', '').lower()
    phone = raw_data.get('phone', '')
    cleaned['phone'] = ''.join(filter(str.isdigit, phone))
    address = raw_data.get('address', '')
    address = ' '.join(address.split())
    cleaned['address'] = address.title()
    parts = name.lower().split()
    if len(parts) >= 2:
        username = f"{parts[0]}_{parts[-1]}"
    elif parts:
        username = parts[0]
    else:
        username = 'none'
    cleaned['username'] = username
    validation = {
        'name_valid': len(cleaned['name']) > 0,
        'email_valid': bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', cleaned['email'])),
        'phone_valid': len(cleaned['phone']) >= 7,  # simplistic check, assumes at least 7 digits
        'address_valid': len(cleaned['address']) > 0}
    cleaned['validation'] = validation
    return cleaned
pass

def analyze_text(text):
    """
    Perform comprehensive text analysis using string methods.
    Args:
        text: Multi-line string of text
    Returns:
        dict: Analysis results containing:
            - 'total_chars': Total character count
            - 'total_words': Total word count
            - 'total_lines': Number of lines
            - 'avg_word_length': Average word length (rounded to 2 decimal)
            - 'most_common_word': Most frequently used word (case-insensitive)
            - 'longest_line': The longest line in the text
            - 'words_per_line': List of word counts per line
            - 'capitalized_sentences': Number of sentences starting with capital
            - 'questions': Number of sentences ending with '?'
            - 'exclamations': Number of sentences ending with '!'
    Example:
        >>> text = '''Hello world! How are you?
        ... This is a test. Another line here!'''
        >>> result = analyze_text(text)
        >>> result['total_words']
        11
        >>> result['questions']
        1
        """
    analysis = {}
    lines = text.splitlines()
    words = re.findall(r'\b\w+\b', text)
    total_chars = len(text)
    total_words = len(words)
    total_lines = len(lines)
    if total_words == True:
        avg_word_length = round(sum(len(word) for word in words) / total_words, 2)
    else:
        avg_word_length = 0
    word_counts = {}
    for word in words:
        word_lower = word.lower()
        if word_lower in word_counts:
            word_counts[word_lower] += 1
        else:
            word_counts[word_lower] = 1
    if word_counts == True:
        most_common_word = word_counts.most_common(1)[0][0]
    else:
        'none'
    longest_line = max(lines, key=len) if lines else ''
    words_per_line = [len(re.findall(r'\b\w+\b', line)) for line in lines]
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())  # splits on .!? followed by space/newline
    capitalized_sentences = sum(1 for s in sentences if s.strip() and s.strip()[0].isupper())
    questions = sum(1 for s in sentences if s.strip().endswith('?'))
    exclamations = sum(1 for s in sentences if s.strip().endswith('!'))
    analysis['total_chars'] = total_chars
    analysis['total_words'] = total_words
    analysis['total_lines'] = total_lines
    analysis['avg_word_length'] = avg_word_length
    analysis['most_common_word'] = most_common_word
    analysis['longest_line'] = longest_line
    analysis['words_per_line'] = words_per_line
    analysis['capitalized_sentences'] = capitalized_sentences
    analysis['questions'] = questions
    analysis['exclamations'] = exclamations
    return analysis
pass

def find_patterns(text):
    """
    Find basic patterns in text using regex.
    Args:
        text: String to search
    Returns:
        dict: Found patterns:
            - 'integers': List of all integers
            - 'decimals': List of all decimal numbers
            - 'words_with_digits': Words containing digits
            - 'capitalized_words': Words starting with capital letter
            - 'all_caps_words': Words in all capitals (min 2 chars)
            - 'repeated_chars': Words with repeated characters (aa, ll, etc.)
    Example:
        >>> text = "I have 25 apples and 3.14 pies. HELLO W0RLD!"
        >>> result = find_patterns(text)
        >>> result['integers']
        ['25']
        >>> result['decimals']
        ['3.14']
        >>> result['all_caps_words']
        ['HELLO']
        >>> result['words_with_digits']
        ['W0RLD']
    """
    patterns = {
    'integers': r'\b\d+\b', # Fill in pattern
    'decimals': r'\b\d+\.\d+\b', # Fill in pattern
    'words_with_digits': r'\b\w*\d\w*\b', # Fill in pattern
    'capitalized_words': r'\b[A-Z][a-z]*\b', # Fill in pattern
    'all_caps_words': r'\b[A-Z]{2,}\b', # Fill in pattern
    'repeated_chars': r'\b\w*(\w)\1\w*\b' # Fill in pattern
    }
    results = {}
    for key, pattern in patterns.items():
        matches = re.findall(pattern, text)
        results[key] = matches

    return results
pass

def validate_format(input_string, format_type):
    """
    Validate if input matches specified format using regex.
    Args:
        input_string: String to validate
        format_type: Type of format to check
    Returns:
        tuple: (is_valid: bool, extracted_parts: dict or None)
        Format types:
            - 'phone': (XXX) XXX-XXXX or XXX-XXX-XXXX
            - 'date': MM/DD/YYYY (validate month 01-12, day 01-31)
            - 'time': HH:MM AM/PM or HH:MM (24-hour)
            - 'email': basic email format (username@domain.extension)
            - 'url': http:// or https:// followed by domain
            - 'ssn': XXX-XX-XXXX (just format, not validity)
        For valid inputs, extract parts (area_code, month, hour, etc.)
    Example:
        >>> validate_format("(555) 123-4567", "phone")
        (True, {'area_code': '555', 'prefix': '123', 'line': '4567'})
        >>> validate_format("13/45/2024", "date")
        (False, None)
    """
# Define patterns for each format type
    patterns = {
    'phone': r'^(?:\((?P<area_code>\d{3})\)|(?P<area_code2>\d{3}))[- ](?P<prefix>\d{3})[- ](?P<line>\d{4})$', # Fill in pattern with groups
    'date': r'^(?P<month>0[1-9]|1[0-2])/(?P<day>0[1-9]|[12]\d|3[01])/(?P<year>\d{4})$', # Fill in pattern with groups
    'time': r'^(?:(?P<hour12>0?[1-9]|1[0-2]):(?P<minute12>[0-5]\d)\s*(?P<ampm>AM|PM))|(?P<hour24>[01]?\d|2[0-3]):(?P<minute24>[0-5]\d)$', # Fill in pattern with groups
    'email': r'^(?P<username>[\w\.-]+)@(?P<domain>[\w\.-]+)\.(?P<extension>\w+)$', # Fill in pattern with groups
    'url': r'^(?P<scheme>https?)://(?P<domain>[\w.-]+\.\w+)(?:[/?#].*)?$', # Fill in pattern with groups
    'ssn': r'^(?P<area>\d{3})-(?P<group>\d{2})-(?P<serial>\d{4})$' # Fill in pattern with groups
    }
pass

def extract_information(text):
    """
    Extract specific information from unstructured text.
    Args:
        text: Unstructured text containing various information
    Returns:
        dict: Extracted information:
            - 'prices': List of prices (formats: $X.XX, $X,XXX.XX)
            - 'percentages': List of percentages (X% or X.X%)
            - 'years': List of 4-digit years (1900-2099)
            - 'sentences': List of complete sentences (end with . ! or ?)
            - 'questions': List of questions (sentences ending with ?)
            - 'quoted_text': List of text in double quotes
    Example:
        >>> text = 'The price is $19.99 (20% off). "Great deal!" she said.'
        >>> result = extract_information(text)
        >>> result['prices']
        ['$19.99']
        >>> result['percentages']
        ['20%']
        >>> result['quoted_text']
        ['Great deal!']
    """
    patterns = {
        'prices': r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?',              
        'percentages': r'\b\d+(\.\d+)?%',                           
        'years': r'\b(19[0-9]{2}|20[0-9]{2})\b',                    
        'sentences': r'[^.!?]*[.!?]',                               
        'quoted_text': r'"(.*?)"',                                  
    }
    result = {}
    result['prices'] = re.findall(patterns['prices'], text)
    result['percentages'] = re.findall(patterns['percentages'], text)
    result['years'] = re.findall(patterns['years'], text)
    result['quoted_text'] = re.findall(patterns['quoted_text'], text)
    raw_sentences = re.findall(patterns['sentences'], text)
    cleaned_sentences = [s.strip() for s in raw_sentences if s.strip()]
    result['sentences'] = cleaned_sentences
    result['questions'] = [s for s in cleaned_sentences if s.endswith('?')]
    return result
pass

def clean_text_pipeline(text, operations):
    """
    Apply a series of cleaning operations using both string methods and regex.
    Args:
        text: Input text to clean
        operations: List of operation names to apply in order
    Operations:
        - 'trim': Remove leading/trailing whitespace
        - 'lowercase': Convert to lowercase
        - 'remove_punctuation': Remove all punctuation
        - 'remove_digits': Remove all digits
        - 'remove_extra_spaces': Replace multiple spaces with single space
        - 'remove_urls': Remove URLs (http/https)
        - 'remove_emails': Remove email addresses
        - 'capitalize_sentences': Capitalize first letter of sentences
    Returns:
        dict: {
        'original': Original text,
        'cleaned': Final cleaned text,
        'steps': List of text after each operation
        }
    Example:
        >>> text = " Hello WORLD! Visit https://example.com "
        >>> ops = ['trim', 'lowercase', 'remove_urls', 'remove_extra_spaces']
        >>> result = clean_text_pipeline(text, ops)
        >>> result['cleaned']
        'hello world! visit'
        """
    original_text = text
    steps = []
    for op in operations:
        if op == 'trim':
            text = text.strip()
        elif op == 'lowercase':
            text = text.lower()
        elif op == 'remove_punctuation':
            text = re.sub(r'[^\w\s]', '', text)
        elif op == 'remove_digits':
            text = re.sub(r'\d+', '', text)
        elif op == 'remove_extra_spaces':
            text = re.sub(r'\s+', ' ', text).strip()
        elif op == 'remove_urls':
            text = re.sub(r'https?://\S+', '', text)
        elif op == 'remove_emails':
            text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '', text)
        elif op == 'capitalize_sentences':
            sentences = re.split(r'([.!?]\s*)', text)
            result = []
            i = 0
            for s in sentences:
                if i % 2 == 0:
                    result.append(s.capitalize())
                else:
                    result.append(s)
                i += 1

            text = ''.join(result)
        steps.append(text)
    return {
        'original': original_text,
        'cleaned': text,
        'steps': steps}
pass

def smart_replace(text, replacements):
    """
    Perform intelligent text replacements using patterns.
    Args:
        text: Input text
        replacements: Dict of replacement rules
        Replacement types:
            - 'censor_phone': Replace phone numbers with XXX-XXX-XXXX
            - 'censor_email': Replace email with [EMAIL]
            - 'fix_spacing': Fix spacing around punctuation
            - 'expand_contractions': Expand contractions (don't -> do not)
            - 'number_to_word': Convert single digits to words (1 -> one)
    Returns:
        str: Text with replacements applied
    Example:
        >>> text = "Call me at 555-123-4567. I'm busy."
        >>> rules = {'censor_phone': True, 'expand_contractions': True}
        >>> smart_replace(text, rules)
        'Call me at XXX-XXX-XXXX. I am busy.'
    """
    # Define contractions dictionary
    contractions = {
    "don't": "do not",
    "won't": "will not",
    "can't": "cannot",
    "I'm": "I am",
    "you're": "you are",
    "it's": "it is",
    "he's": "he is",
    "she's": "she is",
    "we're": "we are",
    "they're": "they are",
    "I've": "I have",
    "you've": "you have",
    "we've": "we have",
    "they've": "they have"
    }
    digit_words = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    if replacements.get('censor_phone'):
        text = re.sub(r'\b\d{3}[- ]?\d{3}[- ]?\d{4}\b', 'XXX-XXX-XXXX', text)
    if replacements.get('censor_email'):
        text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '[EMAIL]', text)
    if replacements.get('fix_spacing'):
        text = re.sub(r'\s+([.,!?;:])', r'\1', text)              
        text = re.sub(r'([.,!?;:])(?=\S)', r'\1 ', text)        
        text = re.sub(r'\s{2,}', ' ', text)                  
    if replacements.get('expand_contractions'):
        for contraction, full in contractions.items():
            text = re.sub(r'\b' + contraction + r'\b', full, text)
            capital_contraction = contraction[0].upper() + contraction[1:]
            capital_full = full[0].upper() + full[1:]
            text = re.sub(r'\b' + capital_contraction + r'\b', capital_full, text)
    if replacements.get('number_to_word'):
        text = re.sub(r'\b\d\b', lambda m: digit_words[m.group()], text)
    return text
pass

def analyze_log_file(log_text):
    """
    Analyze a simplified log file format using string methods and regex.
    Log format: [YYYY-MM-DD HH:MM:SS] LEVEL: Message
    Example: [2024-01-15 10:30:45] ERROR: Database connection failed
    Args:
        log_text: Multi-line string of log entries
    Returns:
        dict: Analysis results:
            - 'total_entries': Total number of log entries
            - 'error_count': Number of ERROR entries
            - 'warning_count': Number of WARNING entries
            - 'info_count': Number of INFO entries
            - 'dates': List of unique dates (YYYY-MM-DD)
            - 'error_messages': List of ERROR messages only
            - 'time_range': Tuple of (earliest_time, latest_time)
            - 'most_active_hour': Hour with most log entries (0-23)
    Example:
        >>> log = '''[2024-01-15 10:30:45] ERROR: Connection failed
        ... [2024-01-15 10:31:00] INFO: Retry attempt 1
        ... [2024-01-15 11:00:00] WARNING: High memory usage'''
        >>> result = analyze_log_file(log)
        >>> result['error_count']
        1
        >>> result['dates']
        ['2024-01-15']
    """
    log_pattern = r'\[(\d{4}-\d{2}-\d{2}) (\d{2}):(\d{2}):(\d{2})\] (\w+): (.+)'
    total_entries = 0
    error_count = 0
    warning_count = 0
    info_count = 0
    dates = set()
    error_messages = []
    times = []
    hour_counter = {}
    for line in log_text.splitlines():
        match = re.match(log_pattern, line)
        if not match:
            continue 
        date_str = match.groups()
        hour_str = match.groups()
        minute = match.groups()
        second = match.groups()
        level = match.groups()
        message = match.groups()
        total_entries += 1
        dates.add(date_str)
        full_time_str = f'{date_str} {hour_str}:{minute}:{second}'
        date_part = full_time_str.split(' ')
        time_part = full_time_str.split(' ')
        year = map(int, date_part.split('-'))
        month = map(int, date_part.split('-'))
        day = map(int, date_part.split('-'))
        hour = map(int, time_part.split(':'))
        minute = map(int, time_part.split(':'))
        second = map(int, time_part.split(':'))
        times.append((year, month, day, hour, minute, second))
        hour_counter[int(hour_str)] += 1
        level_upper = level.upper()
        if level_upper == 'ERROR':
            error_count += 1
            error_messages.append(message)
        elif level_upper == 'WARNING':
            warning_count += 1
        elif level_upper == 'INFO':
            info_count += 1
    if times:
        format_time = f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"
        earliest_time_str = format_time(min(times))
        latest_time_str = format_time(max(times))
        time_range = (earliest_time_str, latest_time_str)
    else:
        time_range = (None, None)
    if hour_counter == True:
        most_active_hour = hour_counter.most_common(1)[0][0]
    else:
        most_active_hour = 'none'
    return {
        'total_entries': total_entries,
        'error_count': error_count,
        'warning_count': warning_count,
        'info_count': info_count,
        'dates': sorted(dates),
        'error_messages': error_messages,
        'time_range': time_range,
        'most_active_hour': most_active_hour}
pass

def run_tests():
    """Test all functions with sample data."""
    print("="*50)
    print("Testing Part 1: String Methods")
    print("="*50)
    # Test 1.1: Receipt formatting
    items = ["Coffee", "Sandwich"]
    prices = [3.50, 8.99]
    quantities = [2, 1]
    receipt = format_receipt(items, prices, quantities)
    print("Receipt Test:")
    print(receipt)
    # Test 1.2: User data processing
    test_data = {
    'name': ' john DOE ',
    'email': ' JOHN@EXAMPLE.COM ',
    'phone': '(555) 123-4567',
    'address': '123 main street'
    }
    cleaned = process_user_data(test_data)
    print(f"\nCleaned name: {cleaned.get('name', 'ERROR')}")
    print(f"Cleaned email: {cleaned.get('email', 'ERROR')}")
    print("\n" + "="*50)
    print("Testing Part 2: Regular Expressions")
    print("="*50)
    # Test 2.1: Pattern finding
    test_text = "I have 25 apples and 3.14 pies"
    patterns = find_patterns(test_text)
    print(f"Found integers: {patterns.get('integers', [])}")
    print(f"Found decimals: {patterns.get('decimals', [])}")
    # Test 2.2: Format validation
    phone_valid = validate_format("(555) 123-4567", "phone")
    phone_parts = validate_format("(555) 123-4567", "phone")
    print(f"\nPhone validation: {phone_valid}")
    if phone_parts:
        print(f"Extracted parts: {phone_parts}")
    # Test 2.3: Information extraction
    info_text = 'The price is $19.99 (20% off).'
    info = extract_information(info_text)
    print(f"\nPrices found: {info.get('prices', [])}")
    print(f"Percentages found: {info.get('percentages', [])}")
    print("\n" + "="*50)
    print("Testing Part 3: Combined Operations")
    print("="*50)
    # Test 3.1: Cleaning pipeline
    dirty_text = " Hello WORLD! "
    operations = ['trim', 'lowercase', 'remove_extra_spaces']
    cleaned_result = clean_text_pipeline(dirty_text, operations)
    print(f"Original: '{cleaned_result.get('original', '')}'")
    print(f"Cleaned: '{cleaned_result.get('cleaned', '')}'")
    print("\n" + "="*50)
    print("Testing Part 4: Log Analysis")
    print("="*50)
    # Test 4.1: Log analysis
    sample_log = """[2024-01-15 10:30:45] ERROR: Connection failed
    [2024-01-15 10:31:00] INFO: Retry attempt
    [2024-01-15 10:32:00] WARNING: Timeout warning"""
    log_analysis = analyze_log_file(sample_log)
    print(f"Total entries: {log_analysis.get('total_entries', 0)}")
    print(f"Error count: {log_analysis.get('error_count', 0)}")
    print(f"Unique dates: {log_analysis.get('dates', [])}")
    print("\n" + "="*50)
    print("All tests completed!")
    print("="*50)
if __name__ == "__main__":
    run_tests()