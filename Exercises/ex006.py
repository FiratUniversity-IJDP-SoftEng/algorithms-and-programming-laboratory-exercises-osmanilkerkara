# Your Student ID: 210543014
# Your Name and Surname: Osman Ilker Kara
# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Print the original list
print("Original list:", numbers)

# Reverse the list 
numbers.reverse()
print("Reversed list:", numbers)

# Add the numbers 11, 12, and 13 to the list 
numbers.extend([11, 12, 13])
print("List after adding 11, 12, and 13:", numbers)

# Print the list's length
print("Length of the list:", len(numbers))

# Remove first element and last element
numbers.pop(0)  
numbers.pop(-1)  
print("List after removing first and last elements:", numbers)

# Create and print a new sorted list  only even numbers 
even_numbers = sorted([num for num in range(1, 14) if num % 2 == 0])
print("Sorted list with even numbers:", even_numbers)
