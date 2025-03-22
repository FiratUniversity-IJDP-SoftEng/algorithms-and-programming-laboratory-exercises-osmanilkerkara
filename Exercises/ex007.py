# Your Student ID: 210543014
# Your Name and Surname: Osman Ilker Kara
def count_characters(input_string):
    char_count = {}
    
    # Count frequency of each character in the string
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Sort the dictionary by character
    sorted_char_count = sorted(char_count.items())
    
    # Print the character frequencies
    print("Character frequencies:")
    for char, count in sorted_char_count:
        print(f"{char}: {count}")

# Get input from the user
input_string = input("Enter a string: ")

# Call the function to count characters
count_characters(input_string)
