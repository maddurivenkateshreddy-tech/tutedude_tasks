"""
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

Expected Output:
Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements of list: [1,2,3,4,5]
Reversed extracted elements: [5,4,3,2,1]

"""

# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
print("Original List:", numbers)
# Extract the first five elements from the list
extracted_elements = numbers[:5]
print("Extracted first five elements of list:", extracted_elements)
# Reverse the extracted elements
reverse_extracted_elements = extracted_elements.reverse()
print("Reversed extracted elements:", extracted_elements)