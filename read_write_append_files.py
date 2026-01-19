"""
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

Expected Output:
Enter some text to write to the file: Hello World, Python
Enter additional text to append to the file: welcome to Programming in Python
Final content of the file:
Hello World, Python
welcome to Programming in Python
"""

def write_to_file(file_name, content):
    """
    Writes content to a file.
    
    Args:
        file_name (str): The name of the file to write to.
        content (str): The content to write to the file.
    """
    try:    
        with open(file_name, 'w') as file:
                file.write(content + '\n')
    except Exception as e:
            print(f"Error writing to file: {e}")
    finally:
            file.close()

def append_to_file(file_name, content):
    """
    Appends content to a file.
    
    Args:
        file_name (str): The name of the file to append to.
        content (str): The content to append to the file.
    """
    try:
        with open(file_name, 'a') as file:
            file.write(content + '\n')
    except Exception as e:
        print(f"Error appending to file: {e}")
    finally:
        file.close()
def read_file(file_name):
    """
    Reads and prints the content of a file.
    
    Args:
        file_name (str): The name of the file to read.
    """
    try:    
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"Error reading file: {e}")
    finally:
        file.close()
    
if __name__ == "__main__":
    user_input = input("Enter some text to write to the file: ")
    write_to_file('output.txt', user_input)
    
    append_input = input("Enter additional text to append to the file: ")
    append_to_file('output.txt', append_input)
    
    print("Final content of the file:")
    read_file('output.txt')