"""
Assignment 6: Final Project

This file has the scripts for the student detials section.

@author: Gagandeep Singh
Date: December 2, 2023
"""

import datetime
import sqlite3

import mailing
import utils

con = sqlite3.connect("database/student.db")
cur = con.cursor()


class Student:
    def __init__(self, username):
        self.username = username
        self.student_id = utils.get_student_id(self.username)

    def get_detials(self):
        """
        This function is to get the details of the student.
        """
        utils.print_header(
            "WELCOME TO ONLINE REGISTRATION PORTAL", "Red River College polytech"
        )
        print("\nPlease enter your details below:")
        print("-" * 32)

        self.first_name = self.get_f_name()
        self.last_name = self.get_l_name()
        self.dob = self.get_dob()
        self.phone = self.get_phone()
        self.email = self.get_email()
        self.address = input("| Address: ").lower()
        self.status = "C"

        # Prompting the student with their student ID
        print("\nYour student ID is:", self.student_id)

        utils.insert_student_details(
            self.username,
            self.first_name,
            self.last_name,
            self.dob,
            self.email,
            self.phone,
            self.address,
        )

        utils.set_status(self.username, "C")

    def get_f_name(self):
        """
        To get the name of the student

        Returns:
            str: name of the student

        Raises:
            ValueError: if field left empty
        """
        while True:
            try:
                student_name = input("| First Name: ").lower()
                if student_name == "":
                    raise ValueError
                break
            except ValueError:
                utils.print_message("WARNING", "you can't leave this field blank")
        return student_name

    def get_l_name(self):
        """
        To get the name of the student

        Returns:
            str: name of the student

        Raises:
            ValueError: if field left empty
        """
        while True:
            try:
                student_name = input("| Last Name: ").lower()
                if student_name == "":
                    raise ValueError
                break
            except ValueError:
                utils.print_message("WARNING", "you can't leave this field blank")
        return student_name

    def get_dob(self):
        # Getting and validating student's age
        while True:
            try:
                student_dob = input("| Date Of Birth (YYYY-MM-DD): ")
                student_dob = datetime.datetime.strptime(student_dob, "%Y-%m-%d")

                self.age = self.calculate_age(student_dob)

                if self.age < 18 or self.age > 35:
                    raise utils.InvalidDOBError

                student_dob = student_dob.date()
                student_dob = student_dob.strftime("%B %d, %Y")
                break

            except utils.InvalidDOBError:
                utils.print_message(
                    "WARNING", "student must betwee 18 to 35 years of age."
                )
                print()

            except Exception:
                utils.print_message("ERROR", "please enter valid date")
        return student_dob

    def get_phone(self):
        """
        To get the phone of the student

        Returns:
            str: phone of the student
        """
        while True:
            try:
                student_phone = input("| Phone: ")

                # checking if the phone is 10 digits long and only numeric
                if (not len(student_phone) == 10) or (not student_phone.isnumeric()):
                    raise ValueError

                if utils.value_exists("people", "phone", "student_phone"):
                    raise utils.PhoneAlreadyExistsError

                break

            except ValueError:
                utils.print_message("ERROR", "please enter valid 10 digit phone")

            except utils.PhoneAlreadyExistsError:
                utils.print_message("WARNIG", "phone number already in use")
        return student_phone

    def get_email(self):
        """
        To get the email of the student

        Returns:
            str: email of the student
        """
        while True:
            try:
                student_email = input("| Email: ").lower()

                if "@" not in student_email:
                    raise ValueError

                if student_email.split("@")[1] not in utils.VALID_DOMAINS:
                    raise ValueError

                if utils.value_exists("people", "email", student_email):
                    raise utils.EmailAlreadyExistsError

                mailing.verify_email(student_email, self.first_name)

                break

            except ValueError:
                utils.print_message("ERROR", "please enter valid email address")

            except utils.EmailAlreadyExistsError:
                utils.print_message("WARNIG", "email already in use")
        return student_email

    def calculate_age(self, date_of_birth):
        """
        To calculate the age of teh student

        Args:
            date_of_birth (datetime object): date of birth of the student

        Returns:
            int: age of the student
        """
        today = datetime.datetime.today()
        age = (
            today.year
            - date_of_birth.year
            - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        )
        return age

    def save_student(self):
        """
        To save the entered student data to the file
        """

        new_student = {
            self.student_id: {
                "name": self.student_name,
                "DOB": self.student_dob,
                "phone": self.student_phone,
                "email": self.student_email,
                "address": self.student_address,
                "father_name": self.student_father_name,
                "mother_name": self.student_mother_name,
                "status": self.status,
            }
        }

        # Adding the student to the main dictionary.
        self.student_dict.update(new_student)

    def get_student_id(self):
        """
        Returns the student id generated for the student

        Returns:
            int: student id of the student
        """
        return self.student_id

    def get_student_status(self):
        return self.status

    def update_status(self, status):
        self.status = status


if __name__ == "__main__":
    utils.clear_terminal()
    utils.print_header("WELCOME", "Red Rived College Polytech")

    # student_dict = read_data(CURRENT_PATH, "data/student_data.pickle")

    new_student = Student("Gdsai4903")
    new_student.get_detials()
    # new_student.save_student()

    utils.print_message("CONGRATULATIONS", "you have been successfully registerd")

    utils.print_thankyou()
