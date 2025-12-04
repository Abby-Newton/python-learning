class BankAccount:
def __init__(self, account_number, owner, initial_balance=0):
self.account_number = account_number
self.owner = owner
# TODO: Set private _balance
def deposit(self, amount):
# TODO: Add amount if positive
# Return new balance
pass
def withdraw(self, amount):
# TODO: Subtract if sufficient funds
# Print error if not
# Return balance
pass
@property
def balance(self):
# TODO: Return _balance
pass
def __str__(self):
# TODO: Return formatted string
pass
class SavingsAccount(BankAccount):
def __init__(self, account_number, owner, initial_balance, interest_rate):
# TODO: Call parent constructor
# TODO: Store interest_rate
pass
def add_interest(self):
# TODO: Calculate and add interest
# Return interest amount
pass
def withdraw(self, amount):
# TODO: Check minimum balance of $100
# Use parent's withdraw if ok
pass
# Test your code
if __name__ == "__main__":
# Regular account
regular = BankAccount("1001", "Alice", 500)
print(regular)
regular.deposit(100)
print(f"After deposit: ${regular.balance}")
regular.withdraw(200)
print(f"After withdrawal: ${regular.balance}")
print("\n" + "="*40 + "\n")
# Savings account
savings = SavingsAccount("2001", "Bob", 1000, 0.02)
print(savings)
interest = savings.add_interest()
print(f"Interest earned: ${interest:.2f}")
print(f"New balance: ${savings.balance}")
# Try to go below minimum
savings.withdraw(950) # Should fail
savings.withdraw(500) # Should work
print(f"Final balance: ${savings.balance}")

class Student:
def __init__(self, name, student_id):
self.name = name
self.student_id = student_id
# TODO: Initialize private _grades list
def add_grade(self, grade):
# TODO: Add grade if valid (0-100)
pass
@property
def gpa(self):
# TODO: Return average or 0.0
pass
def get_letter_grade(self):
# TODO: Return letter grade based on GPA
pass
def __str__(self):
# TODO: Return formatted string
pass
class GraduateStudent(Student):
def __init__(self, name, student_id, thesis_topic):
# TODO: Call parent constructor
# TODO: Store thesis_topic
pass
def get_letter_grade(self):
# TODO: Override with stricter grading
pass
class HonorsStudent(Student):
def __init__(self, name, student_id, honors_thesis=None):
# TODO: Call parent constructor
# TODO: Store honors_thesis
pass
@property
def is_eligible_for_honors(self):
# TODO: Check if GPA >= 87.5
pass
def set_thesis(self, topic):
# TODO: Set if eligible
pass
class StudentRoster:
def __init__(self):
# TODO: Initialize student list
pass
def add_student(self, student):
# TODO: Add to list
pass
def find_student(self, student_id):
# TODO: Search and return student
pass
def list_honor_roll(self):
# TODO: Print students with GPA >= 85
pass
def class_average(self):
# TODO: Return average GPA
pass
# Test your code
if __name__ == "__main__":
# Create roster
roster = StudentRoster()
# Add different types of students
s1 = Student("Alice", "001")
s1.add_grade(92)
s1.add_grade(88)
s1.add_grade(95)
s2 = GraduateStudent("Bob", "002", "Machine Learning")
s2.add_grade(85)
s2.add_grade(82)
s3 = HonorsStudent("Carol", "003")
s3.add_grade(95)
s3.add_grade(98)
s3.add_grade(92)
roster.add_student(s1)
roster.add_student(s2)
roster.add_student(s3)
# Test functionality
print("All Students:")
for student in [s1, s2, s3]:
print(f" {student} - Grade: {student.get_letter_grade()}")
print("\nHonor Roll:")
roster.list_honor_roll()
print(f"\nClass Average: {roster.class_average():.1f}")
# Test honors thesis
s3.set_thesis("Advanced Algorithms")
print(f"\nCarol's thesis: {s3.honors_thesis}")