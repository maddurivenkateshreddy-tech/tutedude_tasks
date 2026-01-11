"""
Assignment 3 - Module 4: 
Task 1: Calculate Factorial Using a Function 

Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
 
Expected Output:
For example, if the function is called with 5, it should return: 120

"""

def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    Args:
        n (int): The number to calculate the factorial for.
    Returns:
        int: The factorial of the number.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def factorial_recursive(n):
    """
    Calculate the factorial of a number using recursion.
    Args:
        n (int): The number to calculate the factorial for.
    Returns:
        int: The factorial of the number.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    sample_number = int(input("Enter a number to calculate its factorial: "))
    print(f"Factorial of {sample_number} using loop: {factorial(sample_number)}")
    print(f"Factorial of {sample_number} using recursion: {factorial_recursive(sample_number)}")

