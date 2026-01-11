"""
Assignment 3 - Module 4:

Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
        o    Square root of the number
        o    Natural logarithm (log base e) of the number
        o    Sine of the number (in radians)
3.   Displays the calculated results.
 Expected Output:
 For example, if the user enters 25, the output should be:
    Square root: 5.0    
    Natural logarithm: 3.2188758248682006
    Sine: -0.13235175009777303
"""
from math import sqrt, log, sin

def calculate_math_operations(number):
    """
    Calculate square root, natural logarithm, and sine of a number.
    
    Args:
        number (float): The number to perform calculations on.  
    Returns:
        dict: A dictionary containing the results of the calculations.
    """  
    resultSqrt = sqrt(number)
    resultLog = log(number)
    resultSin = sin(number)
    return resultSqrt, resultLog, resultSin

if __name__ == "__main__":
    user_input = float(input("Enter a number to perform math operations: "))
    resultSqrt , resultLog, resultSin = calculate_math_operations(user_input)
    print(f"Square root: {resultSqrt}")
    print(f"Natural logarithm: {resultLog}")
    print(f"Sine: {resultSin}")