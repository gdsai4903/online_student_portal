"""
Assignment 6: Final Project

This file has the scripts for the student detials section.

@author: Gagandeep Singh
Date: December 2, 2023
"""
import random
import datetime
from send_email import verify_email
from functions import *


class Student:
    def __init__(self):
        self.student_dict = read_data(CURRENT_PATH, "data/student_data.pickle")
        # Assigning the student with new student ID.
        self.student_id = random.randint(100000, 999999)

        # Making sure the student_id doesn't already exists.
        while self.student_id in self.student_dict.keys():
            self.student_id = random.randint(100000, 999999)

    def get_detials(self):
        """
        This function is to get the details of the student.
        """
        print_header(
            "WELCOME TO ONLINE REGISTRATION PORTAL", "Red River College polytech"
        )
        print("\nPlease enter your details below:")
        print("-" * 32)

        # Getting and validating student name
        while True:
            try:
                self.student_name = input("| Name: ").lower()
                if self.student_name == "":
                    raise ValueError
                break
            except ValueError:
                print_message("WARNING", "you can't leave this field blank")

        # Getting and validating student's age
        while True:
            try:
                self.student_dob = input("| Date Of Birth (MM/DD/YYYY): ")
                self.student_dob = datetime.datetime.strptime(
                    self.student_dob, "%m/%d/%Y"
                )

                self.age = self.calculate_age(self.student_dob)

                if self.age < 18 or self.age > 35:
                    raise InvalidDOBError

                self.student_dob = self.student_dob.date()
                self.student_dob = self.student_dob.strftime("%B %d, %Y")
                break

            except InvalidDOBError:
                print_message("WARNING", "student must betwee 18 to 35 years of age.")
                print()

            except Exception as e:
                print_message("ERROR", f"please enter valid date{e}")

        # Getting and validating student's phone
        while True:
            try:
                self.student_phone = input("| Phone: ")

                # checking if the phone is 10 digits long and only numeric
                if (not len(self.student_phone) == 10) or (
                    not self.student_phone.isnumeric()
                ):
                    raise ValueError

                for student in self.student_dict.keys():
                    if self.student_phone == self.student_dict[student]["phone"]:
                        raise PhoneAlreadyExistsError

                break

            except ValueError:
                print_message("ERROR", "please enter valid 10 digit phone")

            except PhoneAlreadyExistsError:
                print_message("WARNIG", "phone number already in use")

        # Getting and validating student's email
        while True:
            try:
                self.student_email = input("| Email: ").lower()

                if not "@" in self.student_email:
                    raise ValueError

                if not self.student_email.split("@")[1] in VALID_DOMAINS:
                    raise ValueError

                for student in self.student_dict.keys():
                    if self.student_email == self.student_dict[student]["email"]:
                        raise EmailAlreadyExistsError

                verify_email(self.student_email, self.student_name)

                break

            except ValueError:
                print_message("ERROR", "please enter valid email address")

            except EmailAlreadyExistsError:
                print_message("WARNIG", "email already in use")

        self.student_address = input("| Address: ").lower()
        self.student_father_name = input("| Father Name: ").lower()
        self.student_mother_name = input("| Mother Name: ").lower()
        self.status = "Candidate"

        # Prompting the student with their student ID
        print("\nYour new student ID is:", self.student_id)

        self.new_student = {
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

        self.save_student()

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
        # Adding the student to the main dictionary.
        self.student_dict.update(self.new_student)

        # Saving the dictionary.
        save_data(self.student_dict, CURRENT_PATH, "data/student_data.pickle")

    def get_student_id(self):
        return self.student_id

    def get_student_status(self):
        return self.status

    def update_status(self, status):
        self.status = status


if __name__ == "__main__":
    clear_terminal()
    print_header("WELCOME", "Red Rived College Polytech")

    student_dict = read_data(CURRENT_PATH, "data/student_data.pickle")

    new_student = Student()
    new_student.get_detials()
    new_student.save_student()

    print_message("CONGRATULATIONS", "you have been successfully registerd")

    print_thankyou()
