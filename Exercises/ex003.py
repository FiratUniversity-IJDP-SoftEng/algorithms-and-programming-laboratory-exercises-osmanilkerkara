# Your Student ID: 210543014
# Your Name and Surname: Osman Ilker Kara
from datetime import datetime

# Get current date and time
now = datetime.now()

# Format of date
current_date = now.strftime("%Y-%m-%d")

# Format of month
current_time = now.strftime("%H:%M:%S")

print(f"Current date: {current_date}")
print(f"Current time: {current_time}")
print(f"Current date and time: {current_date} {current_time}")
