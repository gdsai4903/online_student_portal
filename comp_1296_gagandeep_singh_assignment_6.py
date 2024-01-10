"""
Assignment 6: Final Project

This file will combine all the sections into one single section. 

@author: Gagandeep Singh
Date: December 2, 2023
"""
from functions import *


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
        clear_terminal()  # Clearing Terminal for better UI
        while True:
            # Printing heading uing a custom function defined in functions.py
            print_header("WELCOME TO RED RIVER COLLEGE POLYTECH", 
                            "Login / Register")

            # Asking if student already has an account
            print("Do you have an account already? (yes/no)")
            responce = input("> ").lower().strip()
            clear_terminal()

            if "yes" in responce:   # Login
                from login_page import Login
                user = Login()
                break

            elif "no" in responce:  # Register then login
                from login_page import Register, Login
                Register()
                clear_terminal()

                user = Login()
                break

            else:
                print_header("WELCOME TO RED RIVER COLLEGE POLYTECH", 
                                "Login / Register")
                
                print_message("ERROR", "invalid input")
                input("\n\nPress Enter to go back to menu.")

            clear_terminal()

        while True:
            clear_terminal()
            while True:
                print_header(
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

                    if not choice in [1, 2, 3, 4, 5, 6]:
                        raise ValueError

                    clear_terminal()
                    break

                except ValueError:
                    print_message("ERROR", "invalid input")
                    input("\n\nPress Enter to try again.")
                    clear_terminal()

            if choice == 1:
                if not user.get_student_id() == 0:
                    print_header(
                        "WELCOME TO ONLINE REGISTRATION PORTAL",
                        "Red River College polytech",
                    )
                    
                    print_message("CAUTION", 
                                  "you have already entered your details")
                else:
                    from students import Student

                    student = Student()
                    student.get_detials()
                    user.update_student_id(student.get_student_id())

                input("\n\nPress Enter to go back to menu.")
                clear_terminal()

            elif choice == 2:
                if user.get_student_id() == 0:
                    print_message("WARNING", 
                                  "you need to enter your details first")
                else:
                    student_id = user.get_student_id()
                    from documents import Documents

                    Documents(student_id)

                input("\n\nPress Enter to go back to menu.")
                clear_terminal()

            elif choice == 3:
                if user.get_student_id() == 0:
                    print_message("WARNING", "you need to enter your details first")
                else:
                    student_id = user.get_student_id()
                    from fee_payment import MakePayment

                    MakePayment(student_id)

                input("\n\nPress Enter to go back to menu.")
                clear_terminal()

            elif choice == 4:
                if user.get_student_id():
                    print_header(
                        "STUDENT DETAILS", f"Student ID: {str(user.get_student_id())}"
                    )
                    student_dict = read_data(CURRENT_PATH, "data/student_data.pickle")
                    print_student_details(student_dict[user.get_student_id()])
                else:
                    print_message("ERROR", "you havn't registered yet")

                input("\n\nPress Enter to go back to menu.")

            elif choice == 5:
                print("\n" * 5)
                print_message("LOGGED OUT")
                print("\n" * 5)
                input("\n\nPress Enter to go back to menu.")
                break

            elif choice == 6:
                clear_terminal()
                print("\n" * 5)
                print_header("THANK YOU", "have a nice day")
                print("\n" * 5)
                exit()


if __name__ == "__main__":
    main()
