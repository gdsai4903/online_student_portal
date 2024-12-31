import getpass
import platform
import re
import sqlite3

import utils

con = sqlite3.connect("database/student.db")
cur = con.cursor()


class LoginParent:
    def is_valid_password(self, password):
        """
        This function is used to check if the password is valid.

        Args:
            password (str): The password to check.

        Returns:
            bool: True if the password is valid, False otherwise.
        """
        # Check if the password has at least 8 characters
        if len(password) < 5:
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
        utils.print_header("LOGIN", "log into your RRC account")

        print("\nEnter your login credentials below.")

        while True:
            print("\nUsername:")
            self.username = input("> ").strip()

            print("\nPassword:")
            self.password = utils.MD5(super().get_hidden_input("> "))

            try:
                self.user = cur.execute(
                    "SELECT password FROM people WHERE username = ?", (self.username,)
                ).fetchone()
                if (not self.user) or (not self.user[0] == self.password):
                    raise utils.WrongLoginCredentials
                break

            except utils.WrongLoginCredentials:
                utils.print_message("CAUTION", "username or password are incorrect")


class Register(LoginParent):
    def __init__(self):
        utils.print_header("REGISTER", "create your new account with RRC")

        print("\nCreate your credentials below.")

        while True:
            try:
                print("\nUsername:")
                self.username = input("> ").strip()
                if utils.value_exists("people", "username", self.username):
                    raise utils.UserAlreadyExistsError

                if not self.is_valid_username(self.username):
                    raise utils.InvalidUsernameError
                break

            except utils.UserAlreadyExistsError:
                utils.print_message("CAUTION", "username already taken")

            except utils.InvalidUsernameError:
                utils.print_long_message(
                    "WARNING",
                    "invalid username, it must be 5 to 20 characters long and"
                    "must not contain any special character except underscore '_'",
                    55,
                )

        while True:
            try:
                while True:  # loop for valid password
                    print("\nCreate Password:")
                    self.password = super().get_hidden_input("> ")

                    if not self.is_valid_password(self.password):
                        utils.print_long_message(
                            "WARNING",
                            "please choose a stronger password, it must contain:"
                            "an uppercase, a lowercase, a number and, a special"
                            "character and must be atleast 5 characters long",
                            55,
                        )
                    else:
                        break

                print("\nConfirm Password:")
                password_confirm = super().get_hidden_input("> ")

                if not self.password == password_confirm:
                    raise utils.PasswordDontMatchError

                break

            except utils.PasswordDontMatchError:
                utils.print_message("ERROR", "passwords don't mach")

        utils.insert_user(self.username, self.password)

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
    print(login)
    # login.get_student_id()
