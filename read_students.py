import os
from prettytable import PrettyTable
from functions import read_data

# Getting the path to the current working directory.
CURRENT_PATH = os.getcwd()

student_dict = read_data(CURRENT_PATH, 'data/student_data.pickle')

# pprint.pprint(student_dict)

print()
print()
print()
print()

# Creating a list of columns for the table
columns = [field.upper() for field in list(student_dict[list(student_dict.keys())[0]].keys())[:5]]
columns = ['STUDENT ID'] + columns + ['STATUS']

# # Create a PrettyTable instance
table = PrettyTable(title = "STUDENT DATA", align = 'l')

# # Add columns to the table
table.field_names = columns

# Add data to the table
for student_id, details in sorted(student_dict.items()):
    table.add_row([student_id, details['name'].title(), details['DOB'], 
details['phone'], details['email'], details['address'].title(), details['status']])

# Print the table
print(table)
print()
print()
print()
