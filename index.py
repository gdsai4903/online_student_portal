import utils


def main():
    """
    This is main funcion that is called at the end of the program. This function
    has all the code that will be executed for running the program.

    Arguments:
        None

    Returns:
        None
    """

    while True:
        utils.clear_terminal()  # Clear Terminal for better UI
        while True:
            # Printing heading uing a custom function defined in functions.py
            utils.print_header(
                "WELCOME TO RED RIVER COLLEGE POLYTECH", "Login / Register"
            )

            # Asking if student already has an account
            print("Do you have an account already? (yes/no)")
            responce = input("> ").lower().strip()
            utils.clear_terminal()

            if "yes" in responce:  # Login
                from login_page import Login

                user = Login()
                break

            elif "no" in responce:  # Register then login
                from login_page import Login, Register

                Register()

                utils.clear_terminal()

                user = Login()
                break

            else:
                utils.print_header(
                    "WELCOME TO RED RIVER COLLEGE POLYTECH", "Login / Register"
                )

                utils.print_message("ERROR", "invalid input")
                input("\n\nPress Enter to go back to menu.")

            utils.clear_terminal()
        username = user.username
        while True:
            utils.clear_terminal()
            while True:
                utils.print_header(
                    "WELCOME TO ONLINE REGISTRATION PORTAL",
                    "Red River College Polytech",
                )
                print("\nWhat task would you like to perform?")
                print("| 1. Enter details")
                print("| 2. Upload Documents")
                print("| 3. Pay Fee")
                print("| 4. My Details")
                print("| 5. Logout")
                print("| 6. Exit")

                try:
                    print("\nEnter the index of the task you want to perform.")
                    choice = int(input("> "))

                    if choice not in [1, 2, 3, 4, 5, 6]:
                        raise ValueError

                    utils.clear_terminal()
                    break

                except ValueError:
                    utils.print_message("ERROR", "invalid input")
                    input("\n\nPress Enter to try again.")
                    utils.clear_terminal()

            if choice == 1:
                if not utils.get_status(username) == "U":
                    utils.print_header(
                        "WELCOME TO ONLINE REGISTRATION PORTAL",
                        "Red River College polytech",
                    )

                    utils.print_message(
                        "CAUTION", "you have already entered your details"
                    )
                else:
                    from students import Student

                    student = Student(username)
                    student.get_detials()

                input("\n\nPress Enter to go back to menu.")
                utils.clear_terminal()

            elif choice == 2:
                if utils.get_status(username) == "U":
                    utils.print_message(
                        "WARNING", "you need to enter your details first"
                    )
                elif utils.get_status(username) == "C":
                    from documents import Documents

                    Documents(username)

                input("\n\nPress Enter to go back to menu.")
                utils.clear_terminal()

            elif choice == 3:
                if utils.get_status(username) == "C":
                    utils.print_message(
                        "WARNING", "you need to enter your details first"
                    )
                else:
                    from fee_payment import MakePayment

                    MakePayment(username)

                input("\n\nPress Enter to go back to menu.")
                utils.clear_terminal()

            elif choice == 4:
                if not utils.get_status(username) == "U":
                    utils.print_header(
                        "STUDENT DETAILS",
                        f"Student ID: {utils.get_student_id(username)}",
                    )
                    utils.print_student_details(username)
                else:
                    utils.print_message("ERROR", "you havn't registered yet")

                input("\n\nPress Enter to go back to menu.")

            elif choice == 5:
                print("\n" * 5)
                utils.print_message("LOGGED OUT", "Thank You")
                print("\n" * 5)
                input("\n\nPress Enter to go back to menu.")
                break

            elif choice == 6:
                utils.clear_terminal()
                print("\n" * 5)
                utils.print_header("THANK YOU", "have a nice day")
                print("\n" * 5)
                exit()


if __name__ == "__main__":
    main()
