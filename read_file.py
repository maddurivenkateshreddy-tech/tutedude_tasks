"""
Module 5 - Assignments - Files, Exceptions, and Modules
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
 
Expected Output:

If the file exists:
This is python programming. Learning from tutedude.
Program videos are going basic and slow learning curve.

If the file does not exist:
Error: The file 'non_existent_file.txt' does not exist.

"""

def read_file(file_name):
    """
    Reads and prints the content of a file line by line.
    
    Args:
        file_name (str): The name of the file to read.
    """
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

if __name__ == "__main__":
    read_file('sample.txt')
    #read_file('non_existent_file.txt')