"""
Assignment 6: Final Project

This file has the login and the register scripts.

@author: Gagandeep Singh
Date: December 2, 2023
"""
import re
import platform
import getpass
from functions import *

con = sqlite3.connect('database/student.db')
cur = con.cursor()

class LoginParent:
    """
    This is the parent class for the login and register scripts.
    """
    def get_username(self):
        """
        This function is used to get the username from the user.

        Returns:
            str: The username from the user.
        """
        return self.username

    def get_password(self):
        """
        This function is used to get the password from the user.

        Returns:
            str: The password from the user.
        """
        return self.password

    def is_valid_password(self, password):
        """
        This function is used to check if the password is valid.

        Args:
            password (str): The password to check.
        
        Returns:
            bool: True if the password is valid, False otherwise.
        """
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
            prompt (str, optional): The prompt to display to the user. Defaults 
            to "Enter your password: ".

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
    """
    This is the login script.
    """
    def __init__(self):
        print_header("LOGIN", "log into your RRC account")
        
        print("\nEnter your login credentials below.")

        while True:
            print("\nUsername:")
            self.username = input("> ").strip()

            print("\nPassword:")
            self.password = MD5(super().get_hidden_input("> "))

            try:
                self.user = cur.execute("SELECT * FROM student WHERE username = ?", (self.username,)).fetchone()
                if (not self.user) or (not self.user[6] == self.password):
                    raise WrongLoginCredentials
                break

            except WrongLoginCredentials:
                print_message("CAUTION", "username or password are incorrect")
                

class Register(LoginParent):
    def __init__(self):
        print_header("REGISTER", "create your new account with RRC")

        print("\nCreate your credentials below.")

        while True:
            try:
                print("\nUsername:")
                self.username = input("> ").strip()
                if value_exists('student', 'username', self.username):
                    raise UserAlreadyExistsError

                if not self.is_valid_username(self.username):
                    raise InvalidUsernameError
                break

            except UserAlreadyExistsError:
                print_message("CAUTION", "username already taken")

            except InvalidUsernameError:
                print_long_message(
                    "WARNING",
                    "invalid username, it must be 5 to 20 characters long and" 
                    "must not contain any special character except underscore '_'",
                    55,
                )
            
            return get_student_id(self.username, self.password)

        while True:
            try:
                while True:
                    print("\nCreate Password:")
                    self.password = super().get_hidden_input("> ")

                    if not self.is_valid_password(self.password):
                        print_long_message(
                            "WARNING",
                            "please choose a stronger password, it must contain:"
                            "an uppercase, a lowercase, a number and, a special"
                            "character and must be atleast 8 characters long",
                            55,
                        )
                    else:
                        break

                print("\nConfirm Password:")
                self.password_confirm = super().get_hidden_input("> ")

                if not self.password == self.password_confirm:
                    raise PasswordDontMatchError

                break

            except PasswordDontMatchError:
                print_message("ERROR", "passwords don't mach")

        insert_user(self.username, self.password)
    
    
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
    login = Login()
    # login.get_student_id()