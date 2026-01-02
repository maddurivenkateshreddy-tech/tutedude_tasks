"""
Task 1#
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
    o	Addition
    o	Subtraction
    o	Multiplication
    o	Division
3.  Displays the results of each operation on the screen.
 Expected Output:
 Addition: 1 + 2
 Subtraction: 1 - 2
 Multiplication: 1 * 2
 Division: 1 / 2
The output should include the result of each operation performed, for example:
"""

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print(f'Addition: {num1 + num2}')
print(f'Subtraction: {num1 - num2}')
print(f'Multiplication: {num1 * num2}')
try:
    print(f'Division: {num1 / num2}')
except ZeroDivisionError:
    print('Division by zero')

