# Your Student ID: 210543014
# Your Name and Surname: Osman Ilker Kara
def print_pyramid(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

# Get input from the user
n = int(input("Enter the number of rows for the pyramid: "))

# Call the function to print the pyramid
print_pyramid(n)
