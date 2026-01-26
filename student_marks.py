"""
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

Expected Output:
Enter Student Name: Alice
Alice's marks 85
"""

# student dictonary
student_marks = { "Alice": 85, "Lishi": 92, "Jeshwin": "89", "Sthuthi": 80 }

print(type(student_marks))

name = input("Enter Student Name");
if student_marks.get(name):
    print(f"{name}'s marks {student_marks[name]}")
else:
    print(f"{name}'s not found")