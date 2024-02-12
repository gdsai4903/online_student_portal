"""
Assignment 6: Final Project

This file has all the common functions that several files are using.

@author: Gagandeep Singh
Date: December 2, 2023
"""

import os
import pickle
import textwrap

# Getting the path to current working directory.
CURRENT_PATH = os.getcwd()

# deciding the valid domains.
VALID_DOMAINS = ["gmail.com", "rrc.ca", "academic.rrc.ca", "outlook.com",
                 "icloud.com"]


# Defining the constants
GST = 7  # in percentage (%)
PST = 5  # in percentage (%)
DISCOUNT = 5  # in percentage (%)

# this dictionary will be used to reffer to each course and its fee.
COURSES = {
    "Linear Algebra": [1700, 25 - len("Linear Algebra")],
    "Statistics": [1650, 25 - len("Statistics")],
    "Programming": [1300, 25 - len("Programming")],
    "Communications": [1100, 25 - len("Communications")],
    "Intro to DSML": [1600, 25 - len("Intro to DSML")],
}

# this dictionary will be used to reffer to each additional expense
OTHER_CHARGES = {
    "Association Fee": [150, len("Association Fee")],
    "Textbooks": [2000, len("Textbooks")],
    "Recreational Fee": [50, len("Recreational Fee")],
    "Building Fee": [20, len("Building Fee")],
}

# Setting the position of the reciept
WIDTH = 65
SPACING = " " * 16


def print_header(heading="heading", sub_heading=None):
    """Prints beautiful header

    Args:
        heading (str, optional): Heading that you wish to pring. Defaults to
                                 "heading".
        sub_heading (_type_, optional): Optional sub heading to be printed below
                                        the headhing. Defaults to None.
    """
    print("=" * WIDTH)
    print(f"{heading.upper()}".center(WIDTH))
    if sub_heading:
        print(str("-" * (len(sub_heading) + 4)).center(WIDTH))
        print(f"{sub_heading.title()}".center(WIDTH))
    print("=" * WIDTH)


def print_message(head="Heading", message="meassage"):
    """
    Prints a message as specified in the arguments.

    Arguments:
        1. head (str): this will be title of the message
        2. message (str): This will be the actual message

    Returns:
        returns nothing, just prints the message
    """
    # Printing the success message and displaying the student ID.
    print("\n" + f"{head}".center(WIDTH))
    print(str("-" * (len(message) - 2)).center(WIDTH))
    print(f"*{message}*".center(WIDTH))
    print()


def print_long_message(head="HEADING", message="message", width=WIDTH):
    """
    Prints a long message and wraps it to the width as specified as
    specified in the arguments.

    Arguments:
        1. head (str): this will be title of the message
        2. message (str): This will be the actual message
        3. widht (int): This will be the widht within which the message is
                        wrapped.

    Returns:
        returns nothing, just prints the message
    """
    message = textwrap.fill(message, width)
    # message = message.center(width)
    print("\n" + f"{head}".center(WIDTH))
    print(str("-" * width).center(WIDTH))
    for line in message.splitlines():
        centered_line = line.center(WIDTH)
        print(centered_line)


def read_data(path, file_name):
    """
    Read data form the saved pickle file as a python dictionary

    Arguments:
        1. path (str): path to pickle file
        2. file_name (str): name of the file

    Returns:
        the file object.
    """
    # Loading the saved student data.
    with open(os.path.join(path, file_name), "rb") as f:
        student_dict = pickle.load(f)
    return student_dict


def save_data(file, path, file_name):
    """Save the data into a pickle file

    Args:
        file (python object): the python object you wish to save
        path (str): path to pickle file you wish to save
        file_name (str): name of the file you wish to save

    Returns:
        None
    """
    # Saving the student Dictionary to the system.
    with open(os.path.join(path, file_name), "wb") as f:
        pickle.dump(file, f)


def print_student_details(current_student):
    """Prints the students details from the dictionary."

    Args:
        current_student (dict): the student dictionary you wish to print

    Returns:
        None
    """
    # Displaying the details student have entered.
    print("\nConfirm your Student Details:")
    print("-" * 30)
    print("| Name:         ", current_student["name"].title())
    print("| Date Of Birth:", current_student["DOB"])
    print("| Phone:        ", current_student["phone"])
    print("| Email:        ", current_student["email"])
    print("| Address:      ", current_student["address"].title())
    print("| Father Name:  ", current_student["father_name"].title())
    print("| Mother Name:  ", current_student["mother_name"].title())
    print(f"\n| Student Status: {current_student['status']}")


def print_thankyou():
    """
    print the thankyou message wherever needed
    """
    print("\n" + "=" * WIDTH)
    print("THANK YOU".center(WIDTH))
    print("=" * WIDTH)
    print("\n")


def clear_terminal():
    """
    For clearing the terminal for better UI
    """
    os.system("cls" if os.name == "nt" else "clear")


class PhoneAlreadyExistsError(Exception):
    """phone number aleary in use"""

    pass


class EmailAlreadyExistsError(Exception):
    """email number aleary in use"""

    pass


class WrongLoginCredentials(Exception):
    """Username or password are incorrect"""


class UserAlreadyExistsError(Exception):
    """User already exists"""

    pass


class InvalidUsernameError(Exception):
    """Username is invalid"""

    pass


class InvalidPasswordError(Exception):
    """Password doesn't match the required conditions"""

    pass


class PasswordDontMatchError(Exception):
    """Passwords dont match"""

    pass


class InvalidDOBError(Exception):
    """Date of birth not valid"""

    pass


if __name__ == "__main__":
    print_header("hello", "world")
