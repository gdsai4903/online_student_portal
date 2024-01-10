"""
Assignment 6: Final Project

This file has the login and the register scripts.

@author: Gagandeep Singh
Date: December 2, 2023
"""
import re
import platform
from functions import *
import getpass


class LoginParent:
    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def is_valid_password(self, password):
        # Check if the password has at least 8 characters
        if len(password) < 8:
            return False

        # Check if the password has at least one uppercase letter
        if not any(char.isupper() for char in password):
            return False

        # Check if the password has at least one lowercase letter
        if not any(char.islower() for char in password):
            return False

        # Check if the password has at least one digit
        if not any(char.isdigit() for char in password):
            return False

        # Check if the password has at least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False

        # If all checks pass, the password is valid
        return True

    def get_hidden_input(self, prompt="Enter your password: "):
        """
        This function is used to get a hidden input from the user.

        Args:
            prompt (str, optional): The prompt to display to the user. Defaults to "Enter your password: ".

        Returns:
            str: The hidden input from the user.
        """
        if platform.system() == "Windows":
            import msvcrt
            print(prompt, end="", flush=True)

            password = ""
            while True:
                char = msvcrt.getch().decode("utf-8")

                # Break the loop on Enter
                if char == "\r":
                    break

                # Handle backspace
                elif char == "\x08":
                    if password:
                        password = password[:-1]
                        print("\b \b", end="", flush=True)

                # Mask the character with an asterisk
                else:
                    password += char
                    print("*", end="", flush=True)

            print()  # Move to the next line after the password input
            return password
        else:
            return getpass.getpass(prompt)
        


class Login(LoginParent):
    def __init__(self):
        print_header("LOGIN", "log into your RRC account")

        self.user_dict = read_data(CURRENT_PATH, "data/user_data.pickle")

        print("\nEnter your login credentials below.")

        while True:
            print("\nUsername:")
            self.username = input("> ").strip()

            print("\nPassword:")
            self.password = super().get_hidden_input("> ")

            try:
                if (not self.username in self.user_dict.keys()) or (
                    not self.password == self.user_dict[self.username]["password"]
                ):
                    raise WrongLoginCredentials

                break

            except WrongLoginCredentials:
                print_message("CAUTION", "username or password are incorrect")

        self.user = self.user_dict

    def get_user(self):
        return self.user, self.username

    def get_student_id(self):
        """
        this is to get the student id from the user table

        Returns:
            int: the student id from the user table
        """
        return self.user[self.username]["student id"]

    def update_student_id(self, student_id):
        """
        This is to update the student id in the user table from the default 
        value that is 0.

        Args:
            student_id (int): the student id assigned to the new student.

        Returns:
            None
        """
        self.user[self.username]["student id"] = student_id
        self.user_dict.update(self.user)
        save_data(self.user_dict, CURRENT_PATH, "data/user_data.pickle")


class Register(LoginParent):
    def __init__(self):
        print_header("REGISTER", "create your new account with RRC")

        # Reading user data
        self.user_dict = read_data(CURRENT_PATH, "data/user_data.pickle")

        print("\nCreate your credentials below.")

        while True:
            try:
                print("\nUsername:")
                self.username = input("> ").strip()
                if self.username in self.user_dict.keys():
                    raise UserAlreadyExistsError

                if not self.is_valid_username(self.username):
                    raise InvalidUsernameError
                break

            except UserAlreadyExistsError:
                print_message("CAUTION", "username already taken")

            except InvalidUsernameError:
                print_long_message(
                    "WARNING",
                    "invalid username, it must be 5 to 20 characters long and must not contain any special character except underscore '_'",
                    55,
                )

        while True:
            try:
                while True:
                    print("\nCreate Password:")
                    self.password = super().get_hidden_input("> ")

                    if self.is_valid_password(self.password):
                        break
                    else:
                        print_long_message(
                            "WARNING",
                            "please choose a stronger password, it must contain: an uppercase, a lowercase, a number and, a special character and must be atleast 8 characters long",
                            55,
                        )

                print("\nConfirm Password:")
                self.password_confirm = super().get_hidden_input("> ")

                if not self.password == self.password_confirm:
                    raise PasswordDontMatchError

                break

            except PasswordDontMatchError:
                print_message("ERROR", "passwords don't mach")

        self.user = {self.username: {"password": self.password, "student id": 0}}

        self.user_dict.update(self.user)
        save_data(self.user_dict, CURRENT_PATH, "data/user_data.pickle")

    def is_valid_username(self, username):
        """
        Validating the username.

        Args:
            username (str): The username to validate.

        Returns:
            bool: True if the username is valid, else False.
        """
        # Define the regular expression pattern for a valid username
        pattern = r"^[a-zA-Z0-9_]{5,20}$"

        # Use re.match() to check if the username matches the pattern
        if re.match(pattern, username):
            return True
        else:
            return False


if __name__ == "__main__":
    print_header("LOGIN / CREATE ACCOUNT", "Red River College Polytech")
    print("Do you already have an account?")
    user_status = input("> ")

    if "yes" in user_status:
        user = Login()
    else:
        user = Register()

    print(f"Username: {user.get_username()}\nPassword: {user.get_password()}")
