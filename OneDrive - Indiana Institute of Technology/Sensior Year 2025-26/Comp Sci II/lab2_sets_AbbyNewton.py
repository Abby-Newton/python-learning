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