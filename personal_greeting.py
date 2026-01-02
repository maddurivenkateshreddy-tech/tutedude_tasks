"""
Task 2:
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
Expected Output:
The program should output a greeting like:
Hello, !fullName! Welcome to the Python program
"""

firstname = input('Enter first name: ')
lastname = input('Enter last name: ')
fullname = None
if firstname and lastname:
    fullname = firstname + ' ' + lastname
else:
    print('Enter values for firstname and lastname')
if fullname:
    print(f'Hello, {fullname}! Welcome to the Python program.')