"""
CS1350 Computer Science II
Week 5 Lecture 1: Advanced String Operations
Student Skeleton Code

Name: Abby Newton
Date: September 15, 2025
"""

import time
import random
import string
from collections import Counter
""""
CS1350 - Week 2, Lab 2: Set Operations
Name: Abby Newton
Date: 9/8/25
Partner: None
"""
def warmup_1():
    """Create sets from different sources"""
    text = "hello world"
    char_set = set(['h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'])
    even_numbers = {x for x in range(21)}
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    desired = [1, 2, 3, 4]
    unique = set(numbers)|set(desired)
    return char_set, even_numbers, unique
print(warmup_1())

def warmup_2():
    '''Practice basic set operations'''
    fruits = {'apple', 'banana', 'orange'}
    citrus = {'orange', 'lemon', 'lime'}
    citrus_fruits = set(fruits) & set(citrus)
    non_citrus = set(fruits) - set(citrus)
    all_fruits = set(fruits) | set(citrus)
    return citrus_fruits, non_citrus, all_fruits
print(warmup_2())

def create_enrollment_data():
    """Create sample enrollment data"""
    enrollments = {
        'CS1350':{'Alice', 'Bob', 'Carol', 'David', 'Eve'},
        'MATH2010':{'Alice', 'Carol', 'Frank', 'Grace'},
        'PHYS1410':{'Bob', 'David', 'Frank', 'Henry'},
        'ENGL1010':{'Eve', 'Grace', 'Henry', 'Ivy'},
        'CHEM1010': {'Alice', 'Bob', 'Ivy', 'Jack'},
        'CS2040': {'Carol', 'David', 'Eve', 'Jack'}
    }
    
    student_courses = {
        'Alice':{'CS1350', 'MATH2010', 'CHEM1010'},
        'Bob':{'CS1350', 'PHYS1410', 'CHEM1010'},
        'Carol':{'CS1350', 'MATH2010', 'CS2040'},
        'David':{'CS1350', 'PHYS1410', 'CS2040'},
        'Eve':{'CS1350', 'ENGL1010', 'CS2040'},
        'Frank':{'MATH2010', 'PHYS1410', },
        'Grace':{'MATH2010', 'ENGL1010', },
        'Henry':{'PHYS1410', 'ENGL1010', },
        'Ivy':{'ENGL1010', 'CHEM1010'},
        'Jack':{'CHEM1010', 'CS2040'}
    }
    return enrollments, student_courses
course_enrollments, student_schedules = create_enrollment_data()

def find_common_students(course1, course2, enrollments):
    """ 
    Find students enrolled in both courses.
    Args:
        course1: First course code
        course2: Second course code
        enrollments: Dictionary of course enrollments
    Returns:
        Set of students in both courses
    """
    students_course1 = enrollments.get(course1, set())
    students_course2 = enrollments.get(course2, set())
    enrollments = {
        'CS1350':{'Alice', 'Bob', 'Carol', 'David', 'Eve'},
        'MATH2010':{'Alice', 'Carol', 'Frank', 'Grace'},
        'PHYS1410':{'Bob', 'David', 'Frank', 'Henry'},
        'ENGL1010':{'Eve', 'Grace', 'Henry', 'Ivy'},
        'CHEM1010': {'Alice', 'Bob', 'Ivy', 'Jack'},
        'CS2040': {'Carol', 'David', 'Eve', 'Jack'}
        }
    return set(students_course1) & set(students_course2)
pass

def find_popular_combinations(student_schedules):
    """Find the most common course pairs taken together.

    Args:
        student_schedules: Dictionary of student course sets

    Returns:
        List of (course_pair, count) tuples, sorted by count
    """
    student_schedules = {
        'Alice':{'CS1350', 'MATH2010', 'CHEM1010'},
        'Bob':{'CS1350', 'PHYS1410', 'CHEM1010'},
        'Carol':{'CS1350', 'MATH2010', 'CS2040'},
        'David':{'CS1350', 'PHYS1410', 'CS2040'},
        'Eve':{'CS1350', 'ENGL1010', 'CS2040'},
        'Frank':{'MATH2010', 'PHYS1410'},
        'Grace':{'MATH2010', 'ENGL1010'},
        'Henry':{'PHYS1410', 'ENGL1010'},
        'Ivy':{'ENGL1010', 'CHEM1010'},
        'Jack':{'CHEM1010', 'CS2040'}
        }
    course_pair = find_common_students
    count = Counter()
    return sorted(student_schedules(course_pair, count))
pass
    
def find_exclusive_students(course, enrollments):
    """
    Find students who ONLY take this one course.
    
    Args:
        course: Course code
        enrollments: Dictionary of course enrollments
        
    Returns:
        Set of students taking only this course
    """
    course = enrollments.get(course, set())
    enrollments = {
        'CS1350':{'Alice', 'Bob', 'Carol', 'David', 'Eve'},
        'MATH2010':{'Alice', 'Carol', 'Frank', 'Grace'},
        'PHYS1410':{'Bob', 'David', 'Frank', 'Henry'},
        'ENGL1010':{'Eve', 'Grace', 'Henry', 'Ivy'},
        'CHEM1010': {'Alice', 'Bob', 'Ivy', 'Jack'},
        'CS2040': {'Carol', 'David', 'Eve', 'Jack'}
        }
    return set(enrollments.keys[1] - enrollments.keys[2] - enrollments.keys[3] - enrollments.keys[4] - enrollments.keys[5])
pass

def recommend_courses(student, student_schedules):
    """
    Recommend courses based on what similar students take.
    
    Args:
        student: Student name
        student_schedules: Dictionary of student course sets
    
    Returns:
        Set of recommended courses (not currently taken)
    """
    student = student_schedules.get(student, set())
    student_schedules = {
        'Alice':{'CS1350', 'MATH2010', 'CHEM1010'},
        'Bob':{'CS1350', 'PHYS1410', 'CHEM1010'},
        'Carol':{'CS1350', 'MATH2010', 'CS2040'},
        'David':{'CS1350', 'PHYS1410', 'CS2040'},
        'Eve':{'CS1350', 'ENGL1010', 'CS2040'},
        'Frank':{'MATH2010', 'PHYS1410', },
        'Grace':{'MATH2010', 'ENGL1010', },
        'Henry':{'PHYS1410', 'ENGL1010', },
        'Ivy':{'ENGL1010', 'CHEM1010'},
        'Jack':{'CHEM1010', 'CS2040'}
        }
    return set(student_schedules.keys[1](student_schedules.values)) - set(student_schedules.keys[2](student_schedules.values))
pass

def test_enrollment_analysis():
    """Test all enrollmnet analysis functions"""
    
    print("=== Testing Enrollment Analysis ===")
    
    #Test 1: Common Student
    common = find_common_students('CS1350', 'MATH2010', course_enrollments)
    print(f"Students in both CS1350 and MATH2010: {common}")
    assert common == {'Alice', 'Carol'}, "Common students test failed"
    
    #Test 2:Popular combinations
    popular = find_popular_combinations(student_schedules)
    print(f"Popular course combinations: {popular[:3]}") #Top 3
    
    #Test 3: Exclusive students
    exclusive = find_exclusive_students('CS1350', course_enrollments)
    print(f"Students taking only CS1350: {exclusive}")
    
    #Test 4: Course recommendations
    recommendations = recommend_courses('Frank', student_schedules)
    print(f"Recommended courses for Frank: {recommendations}")
    
    #Run tests
    test_enrollment_analysis()
    
def process_text(text):
    """
    Process text into a set of words (lowercase, no punctuation).

    Args:
        text: String of text to process
            
    Returns:
        Set of unique words
    """
    text = "Hello World!"
    textprocessed1 = text.lower()
    textprocessed2 = textprocessed1.translate(str.maketrans('','', string.punctuation))
    print("Processed text:", textprocessed2)
    pass
    
def calculate_similarity(text1, text2):
    """
    Calculate Jaccard similarity between two texts.
    Jaccard = [intersection] / [union]

    Args:
        text1: First text string
        text2: Second text string
            
    Returns:
        Float between 0 and 1 (1 = identical vocabulary)
    """
    text1 = "Hello World!"
    text2 = "Hi World!"
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())
    intersection = set1 & set2
    union = set1 | set2
    Jaccard = intersection / union
    print("Text similarities:", Jaccard)
    pass

def find_unique_words(text1, text2):
    """
    Find words unique to each text.

    Args:
        text1: First text string
        text2: Second text string 
        
    Returns:
        Tuple of (words_only_in_text1, words_only_in_text2)
    """
    text1 = "Hello World!"
    text2 = "Hi World!"
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    unique_words = words1 | words2
    print("The unique words are:", unique_words)
    pass
    
def detect_common_phrases(texts, min_occurrences = 3):
    """
    Find words that appear in at least min_occurrences texts.

    Args:
        texts: : list of text strings
        min_occurrences: Minimum number of texts word must appear in
        
    Returns:
        Set of common words
    """
    texts = ["Hello World!", "Hi World!", "Adios World!"]
    set1 = set(texts[1].lower().split())
    set2 = set(texts[2].lower().split())
    set3 = set(texts[3].lower().split())
    intersection = set1 & set2 & set3
    union = set1 | set2 | set3
    Jaccard = intersection / union
    min_occurrences = min(Jaccard)
    print("The minimum occurences is:", min_occurrences)
    pass
text_samples = {
    'student1':"""
    Python is a powerful programming language. It has efficient 
    high-level data structures and a simple approach to object-oriented 
    programming. Python's elegant syntax and dynamic typing make it 
    an ideal language for scripting.
    """,
    'student2':"""
    Python is a high-level programming language. It features dynamic
    typing and elegant syntax. Python has simple but effective approach
    to object-oriented programming and powerful data structures.
    """,
    'student3':"""
    Java is a class-based, object-oriented programming language. It is
    designed to have as few implementation dependencies as possible.
    Java applications are  typically complied to bytecode.""",
    'original':"""
    Python is a high-level, general-purpose programming language. Its
    design philosophy emphasizes code readability with the use of 
    significant indentation. Python is dynamically typed and garbage-collected.
    """
    }

def plagiarism_check(submissions, threshold=0.7):
    """
    Check for potential plagiarism among submissions.

    Args:
        submissions: Dictionary of {student_id:text}
        threshold: Similarity threshold for flagging (0-1),
        
    Returns:
        List of (student1, student2, similarity) tuples above threshold
    """
    submissions = {'Abby':'2316336', 'Ben':'2316446', 'Clark':'2316556'}
    threshold = 0.7
    print("the plagiarism is:", plagiarism_check(submissions, threshold))
    pass

def writing_style_analysis(text):
    """
    Analyze writing style characteristics.

    Args:
        text: Text to analyze
        
    Returns:
        Dictionary with style metrics:
        - vocabulary_size: Number of unique words
        - average_word_length: Average length of words
        - word_diversity: Ratio of unique words to total words
    """
    text = "Hello World!"
    cleaned = text.translate(str.maketrans('', '', string.punctuation)).lower.split()
    vocabulary_size = len(set(cleaned))
    average_word_length = sum(len(word) for word in cleaned) / len(cleaned)
    word_diversity = len(set(cleaned)) / len(cleaned)
    print('vocab size:', vocabulary_size, 'word length average', average_word_length, 'diversity', word_diversity)
    pass

print("\n=== Plagiarism Detection Results ===")
results = plagiarism_check(text_samples, threshold=0.5)
for student1, student2, similarity in results:
    print(f"{student1} vs {student2}:{similarity:.2%}similar")
    
def create_social_network():
    """Create a sample social network"""
    
    network = {
        'Alice':{'Bob', 'Carol', 'David'},
        'Bob': {'Alice', 'David', 'Eve', 'Frank'},
        'Carol': {'Alice', 'Eve', 'Grace'},
        'David': {'Alice', 'Bob', 'Frank', 'Henry'},
        'Eve': {'Bob', 'Carol', 'Grace', 'Henry'},
        'Frank': {'Bob', 'David', 'Henry', 'Ivy'},
        'Grace': {'Carol', 'Eve', 'Ivy'},
        'Henry': {'David', 'Eve', 'Frank', 'Ivy'},
        'Ivy': {'Frank', 'Grace', 'Henry'}
    }
    return network
social_network = create_social_network()

def find_mutual_friends(person1, person2, network):
    """
    Find mutual friends between two people.
    
    Args:
        person1: First person's name
        person2: Second person's name
        network: Social network dictionary
    
    Returns:
        Set of mutual friends
"""
    person1 = 'Abby'
    person2 = 'Ben'
    network = {person1: {'Ben', 'Alex', 'Riley'}, person2:{'Abby', 'Alex', 'Sam'}}
    friends1 = network.get(person1, set())
    friends2 = network.get(person2, set())
    print('Mutual friends :', friends1 & friends2)
# TODO: Implement this
pass

def suggest_friends(person, network, max_suggestions=3):
    """
    Suggest new friends based on mutual connections.
    People with the most mutual friends are suggested first.
    
    Args:
        person: Person to suggest friends for
        network: Social network dictionary
        max_suggestions: Maximum number of suggestions
    Returns:
        List of (suggested_person, mutual_friend_count) tuples
"""
    person = 'Abby'
    network = {person:{'Ben', 'Alex', 'Sam'}}
    max_suggestions = 3
    if network.keys > max_suggestions:  
        print('too many suggestions')
    else:
        print('suggestions:', network.keys)
# TODO: Find friends of friends who aren't direct friends
# TODO: Count mutual connections
# TODO: Return top suggestions
pass

def find_influencers(network, min_connections=4):
    """
    Find people with at least min_connections friends.
    Args:
        network: Social network dictionary
        min_connections: Minimum number of connections
    Returns:
        Set of influencer names
"""
    network = {'Abby': {'Ben', 'Alex', 'Riley'}, 'Ben':{'Abby', 'Alex', 'Sam'}}
    min_connections = 4
    influencers = set()
    for person, friends in network.items():
        if len(friends) >= min_connections:
            influencers.add(person)
    print('influencers:', influencers)
# TODO: Implement this
pass

def find_isolated_groups(network):
    """
    Find groups of people who are all connected to each other
    but have no connections outside the group.
    
    Args:
        network: Social network dictionary
    Returns:
        List of sets, each containing an isolated group
    """
    network = {'Abby': {'Ben', 'Alex', 'Riley'}, 'Ben':{'Abby', 'Alex', 'Sam'}}
    if network[1] != network[2]:
        print('isolated:', network)
    else:
        print('no one is isolated')
# TODO: Advanced - find cliques with no external connections
pass

def test_social_network():
    """Test social network analysis"""
    print("\n=== Social Network Analysis ===")
    
    # Test mutual friends
    mutual = find_mutual_friends('Alice', 'Bob', social_network)
    print(f"Mutual friends of Alice and Bob: {mutual}")
    
    # Test friend suggestions
    suggestions = suggest_friends('Alice', social_network)
    print(f"Friend suggestions for Alice: {suggestions}")
    
    # Test influencer detection
    influencers = find_influencers(social_network)
    print(f"Network influencers: {influencers}")
    
# Run tests
test_social_network()

def performance_comparison():
    """Compare set vs list performance for membership testing"""

    # Create large collections
    size = 100000
    data_list = list(range(size))
    data_set = set(range(size))
    
    # Test membership for non-existent element
    test_element = size + 1

    # TODO: Time list membership test (1000 iterations)
    start_list = time.time()
    result_list = test_element in data_list
    end_list = time.time()
    list_time = end_list - start_list
    
    # TODO: Time set membership test (1000 iterations)
    start_set = time.time()
    result_set = test_element in data_set
    end_set = time.time()
    set_time = end_set - start_set
    
    # TODO: Calculate and print speedup factor
    print(f'List membership test took: {list_time:.6f} seconds', result_list)
    print(f'Set membership test took: {set_time:.6f} seconds', result_set)
    pass

def word_chain_game():
    """
    Create a word chain game where each word must:
    1. Start with the last letter of the previous word
    2. Not be used before

    Use sets to track used words and valid words.
    """
    valid_words = {'apple', 'elephant', 'tiger', 'rabbit',
        'turtle', 'eagle', 'elk', 'koala', 'ant'}
    used_words = set()
    current_word = input('word:').strip.lower()
    if current_word not in valid_words:
        print('pick a valid word')
        return
    used_words.add(current_word)
    while True:
        last_letter = current_word[-1]
        print(f"\nCurrent word: {current_word}")
        next_word = input(f"Enter a word starting with '{last_letter}':").strip().lower()
        if next_word == 'quit':
            print('Thanks! Bye')
            break
        if next_word in used_words:
            print('already used this word')
            continue
        if next_word not in valid_words:
            print('word not valid')
            continue
        if next_word[0] != last_letter:
            print('does not start with ', {last_letter})
            continue
        used_words.add(next_word)
        current_word = next_word
    # TODO: Implement game logic
    pass

#1. When would you choose a set over a list for storing data?
# I would choose a set over a list if I needed unique items, a fast way to check data, performing mathematical operations, or if order does not matter.
#2. Which set operation (union, intersection, difference) did you find most useful? Why?
# Probably intersection is the most useful because I frequently would need to find common elements in different datasets.
#3. How much faster was set membership testing compared to list? Why?
# Way faster using sets than lists because sets allow direct access to elements, versus lists scan each element one by one.
#4. What real-world problem could you solve using sets?
# There are many real-world problems that could be solved using sets including detectting duplicates, finding mutuals, finding unique elements, managing an inventory, and recommending items. Most of these can be used on social media platforms but also for data synthesis. 