"""
Assignment 6: Final Project

This file has all the common functions that several files are using.

@author: Gagandeep Singh
Date: December 2, 2023
"""

import os
import pickle
import textwrap
import sqlite3
import hashlib

# Getting the path to current working directory.
CURRENT_PATH = os.getcwd()

# deciding the valid domains.
VALID_DOMAINS = ["gmail.com", "rrc.ca", "academic.rrc.ca", "outlook.com",
                 "icloud.com"]


# Defining the constants
GST = 7  # in percentage (%)
PST = 5  # in percentage (%)
DISCOUNT = 5  # in percentage (%)

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
    print()


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


def print_student_details(username):
    """Prints the students details from the dictionary."

    Args:
        current_student (dict): the student dictionary you wish to print

    Returns:
        None
    """
    con = sqlite3.connect('database/student.db')
    cur = con.cursor()

    query = "SELECT * FROM student WHERE username = ?"
    cur.execute(query, (username,))
    current_student = cur.fetchone()
    con.close()

    # Displaying the details student have entered.
    print("\nConfirm your Student Details:")
    print("-" * 30)
    print("| Name:         ", current_student[1] + ' ' + current_student[2])
    print("| Date Of Birth:", current_student[3])
    print("| Email:        ", current_student[4])
    print("| Phone:        ", current_student[7])
    print("| Address:      ", current_student[8].title())
    print(f"\n| Student Status: {current_student[9]}")


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

def fetch_user(user_name):
    conn = sqlite3.connect('database/student.db')
    cursor = conn.cursor()

    res = cursor.execute(f"""SELECT * FROM user WHERE user_name = '{user_name}'""")
    return res.fetchall()[0]

def get_user_names():
    conn = sqlite3.connect('database/student.db')
    cursor = conn.cursor()

    res = cursor.execute(f"""SELECT username FROM student""")
    return res.fetchall()

def get_student_id(username):
    con = sqlite3.connect('database/student.db')
    cur = con.cursor()

    query = "SELECT student_id FROM student WHERE username = ?"

    cur.execute(query, (username,))
    student_id = cur.fetchone()[0]

    cur.close()

    return student_id

def get_status(username):
    con = sqlite3.connect('database/student.db')
    cur = con.cursor()

    query = "SELECT status FROM student WHERE username = ?"

    cur.execute(query, (username,))
    status = cur.fetchone()[0]

    cur.close()

    return status

def set_status(username, status):
    con = sqlite3.connect('database/student.db')
    cur = con.cursor()

    query = f"UPDATE student SET status = ? WHERE username = ?"

    cur.execute(query, (status, username))

    con.commit()
    con.close()

def update_value(username, column, value):
    con = sqlite3.connect('database/student.db')
    cur = con.cursor()

    query = f"UPDATE student SET {column} = ? WHERE username = ?"

    cur.execute(query, (value, username))

    con.commit()
    con.close()

def get_details(username, columns:tuple = ()):
    con = sqlite3.connect('database/student.db')
    cur = con.cursor()

    if not columns == ():
        cols = ', '.join(columns)
        query = f"SELECT {cols} FROM student WHERE username='{username}'"
        cur.execute(query)
    else:
        query = f"SELECT * FROM student WHERE username='{username}'"
        cur.execute(query)

    current_student = cur.fetchone()

    con.close()

    return current_student

def insert_user(username, password):
    query = """INSERT INTO student (username, password) VALUES (?, ?)"""

    con = sqlite3.connect("database/student.db")
    cur = con.cursor()

    cur.execute(query, (username, MD5(password)))

    con.commit()
    con.close()

def insert_student_details(username, f_name, l_name, dob, email, phone, addr):
    con = sqlite3.connect('database/student.db')
    cur = con.cursor()

    query = f"""UPDATE student SET (first_name
                                  , last_name
                                  , dob
                                  , email
                                  , phone
                                  , addr)
                    = (?,?,?,?,?,?)
                    WHERE username=?"""

    cur.execute(query, (f_name
                      , l_name
                      , dob
                      , email
                      , phone
                      , addr
                      , username))
    con.commit()

def value_exists(table, column, value):
        """
        Check if a value exists in a specified column of a table.

        Parameters:
        table (str): The name of the table.
        column (str): The name of the column.
        value (str): The value to check for.

        Returns:
        bool: True if the value exists, False otherwise.
        """
        con = sqlite3.connect("database/student.db")
        cur = con.cursor()

        query = f"SELECT 1 FROM {table} WHERE {column} = ?"
        cur.execute(query, (value,))
        result = cur.fetchone()

        con.close()

        return result is not None

def MD5(password):
    return hashlib.md5(password.encode()).hexdigest()

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
    username = 'gsingh456'
    print(get_details(username, ('email',))[0])
