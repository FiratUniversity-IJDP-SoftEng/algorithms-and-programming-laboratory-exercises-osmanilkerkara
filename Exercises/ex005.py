# Your Student ID: 210543014
# Your Name and Surname: Osman Ilker Kara
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Calculate spacing
hi_text = "Hi"
space_after_hi = " " * (len(hi_text) + 1) 

# Print formatted output
print(f"{hi_text}{space_after_hi}{last_name}")
print(f"{' ' * len(hi_text)} {first_name}")
