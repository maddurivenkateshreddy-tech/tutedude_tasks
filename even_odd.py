"""
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
Expected Output:
The program should output a message like:
The number 4 is even.  

"""

number = input('Enter your number: ')
if number:
    try:
        num = int(number)
    except ValueError:
        print('Please enter a valid integer.')
        exit           
    if num % 2 == 0:
        print(f'The number {num} is even.')
    else:
        print(f'The number {num} is odd.')
else:
    print('No input provided.')