"""
Assignment 6: Final Project

This file has the script for the fee payment

@author: Gagandeep Singh
Date: December 2, 2023
"""
import sqlite3
from functions import *
from send_email import *


class MakePayment:
    def __init__(self, username):
        clear_terminal()
        # Printing the heading of the UI.
        print_header("FEE PAYMENT", "Red River College Polytech")

        print_student_details(username)

        status = get_status(username)

        # Checking if the student is already enrolled.
        if status == "E":
            print_message("ATTENTION", "you have aleady paid your fee")

        # Checking if the student is just a candidate.
        elif status == "C":
            print_message("ATTENTION", "upload your documents first to pay your fee")

        elif status == "A":
            # Creating empty list to store courses taken.
            taken_courses = self.offer_courses()

            self.fee = self.calculate_fee(taken_courses)

            self.make_payment(username)

        # Printing the Thankyou message
        print_thankyou()

    def offer_courses(self):
        """
        Offers the courses to students

        Raises:
            ValueError: when invalid input is provided

        Returns:
            list: list of chosen courses
        """
        self.taken_courses = []

        while True:
            # Asking student to select what course to take
            print("\nFrom the given list of courses, choose atleast 3:")

            # Printing the header for courses
            print("-" * 35)
            print("  C_ID   COURSE NAME           FEE")
            print("-" * 35)

            course_ids = []
            for course in self.fetch_courses():
                course_ids.append(course[0])
                print(
                    f" |{course[0]}.  {course[1]}:"
                    f"{('$' + str(course[2])).rjust(25-len(course[1]))}"
                )

            while True:
                try:
                    print(
                        "\nType the c_id of courses you want to take"
                        " separated by commas','."
                    )
                    response = input("> ")
                    for choices in response.split(","):
                        c_id = int(choices.strip())
                        if c_id in course_ids:
                            self.taken_courses.append(c_id)
                        else:
                            raise ValueError

                    break
                except ValueError:
                    print_message("CAUTION", 'invalid input. sample input: "1001, 1002, 1003"')

            if len(self.taken_courses) >= 3:
                course_names = self.fetch_courses(self.taken_courses)

                # printing the courses selected.
                print("\nYou have selected the following courses:")
                for course in course_names:
                    print(f" |{course[0]} - {course[1]}")
            else:
                print_message("CAUTION", "you have to take atleast 3 courses.")
                print()
                input("\n\nPress Enter to go try again.")
                clear_terminal()

            input("\nPress Enter to continue? ")
            break
        return self.taken_courses

    def calculate_fee(self, taken_courses):
        """
        To calculate the fee of the student's selected courses.

        Args:
            taken_courses (list): the taken courses to calculate

        Returns:
            float: the calculated fee of the student's selected courses.
        """

        # Calculating and printing the fee reciept
        print("\nYour fee will be calculated as following: ")

        # Creating float variable to store total fee.
        total = 0.0

        courses = self.fetch_courses(taken_courses)
        amanities = self.fetch_amanities()

        # Printing the receipt header.
        print("\n" + SPACING, "-" * 33)
        print(SPACING, "RRC POLYTECH".center(33))
        print(SPACING, "Fee Receipt".center(33))
        print(SPACING, str(datetime.date.today()).center(33))
        print(SPACING, str(datetime.datetime.now().strftime("%H:%M:%S")).center(33))
        print(SPACING, "-" * 33)
        print(SPACING, "Description", "Amount".rjust(21))
        print(SPACING, "-" * 33)

        # Printing fee for chosen courses
        for course in courses:
            if course[0] in taken_courses:
                print(
                    SPACING,
                    course[1],
                    str("%.2f" % course[2]).rjust(32- len(course[1])),
                    "+",
                )
                total += course[2]
        print()

        # Printing fee for Other expenses
        for expence in amanities:
            print(
                SPACING,
                expence[0],
                str("%.2f" % expence[1]).rjust(
                    32 - len(expence[0])
                ),
                "+",
            )
            total += expence[1]

        print(SPACING, "-" * 33)
        print(SPACING, "Total", str("%.2f" % total).rjust(27))
        print(SPACING, "-" * 33)

        # Calculating the tax on the fee
        # GST
        GST = get_tax('GST')
        gst = total * (GST / 100)
        print(SPACING, f"GST({GST}%):", str("%.2f" % gst).rjust(24), "+")

        # PST
        PST = get_tax('PST')
        pst = total * (PST / 100)
        print(SPACING, f"PST({PST}%):", str("%.2f" % pst).rjust(24), "+")

        # Calculating Printing the sub total
        sub_total = total + gst + pst
        print(SPACING, "-" * 33)
        print(SPACING, "Sub Total:", str("%.2f" % sub_total).rjust(22))
        print(SPACING, "-" * 33)

        grand_total = sub_total

        # Calculating the DISCOUNT
        if len(taken_courses) == 5:
            # Calculating and printing the discount applied
            discount = sub_total * (DISCOUNT / 100)
            print(
                SPACING,
                f"Discount({DISCOUNT}%):",
                str("%.2f" % discount).rjust(19),
                "-",
            )
            grand_total = sub_total - discount
        else:
            print(SPACING, "Discount(0%):", "00.00".rjust(19), "-")

        # Calculating Printing the grand total
        print(SPACING, "=" * 33)
        print(SPACING, "Grand Total:", str("%.2f" % grand_total).rjust(20))
        print(SPACING, "=" * 33)

        return grand_total

    def make_payment(self, username):
        """
        To make a payment, and send the offer letter to the registered email.

        Args:
            student_id (int): the student id of the student
            current_student (dict): the student's data dictionary
        """

        while True:
            print("\nEnter your card details below:")
            card_num = input("Credit/Debit card number: ")

            if not len(card_num) == 16:
                print_message("ERROR", "Please enter a valid card number")
                continue

            while True:
                try:
                    valid_thru = input("Valid thru MM/YY: ")
                    valid_thru = datetime.datetime.strptime(valid_thru, "%m/%y")
                    break

                except ValueError:
                    print_message("ERROR", "Please enter a valid date")
                    continue
            while True:
                cvv = input("3 digit security code: ")
                if not len(cvv) == 3:
                    print_message("ERROR", "Enter Valid CVV")
                    continue
                break

            response = (
                input("Do you confirm the details abonve (yes/no): ").lower().strip()
            )
            if "yes" in response:
                break

        # Asking the student for payment method
        payment_method = input("\nType 'pay' and press Enter to pay: ").lower().strip()

        # details = get_details(username, ('student_id', 'email', 'first_name'))

        if "pay" in payment_method:
            verify_email(
                username,
                purpose="payment",
                fee=self.fee,
            )

            # Printing the success message.
            print_message("CONGRATULATIONS", "you have paid your fee successfully")

            try:
                # inserting course records
                register_courses(username, self.taken_courses)
                # Changing the student status to approved.
                set_status(username, 'E')
                try:
                    send_offer_letter(username)
                    print("\n" + "*an email has been sent to your registered email*".center(WIDTH))
                except Exception as e:
                    print(e)

            except Exception as e:
                print_message("Warning!", f"There was an error registering for courses.{e} Your status was not changed. ")

                # Displaying the change of status
                print("\nYour status has now been changed to 'Enrolled'!")
                print("\nStudent status: ", get_status(username))

            


        else:
            print_message("ERROR", "fee could not be paid")

            # Displaying the change of status
            print("\nYour status has not been changed to 'Enrolled'!")
            print("\nStudent status: ", get_status(username))


    def fetch_courses(self, taken_courses = None):
        con = sqlite3.connect('database/student.db')
        cur = con.cursor()

        if taken_courses:
            placeholder = ','.join('?' for _ in taken_courses)
            query = f"SELECT course_id, course_name, course_fee FROM course WHERE course_id IN ({placeholder})"
            cur.execute(query, taken_courses)

        else:
            query = "SELECT course_id, course_name, course_fee FROM course WHERE active=1"
            cur.execute(query)

        courses = cur.fetchall()

        con.close()

        return courses

    def fetch_amanities(self):
        con = sqlite3.connect('database/student.db')
        cur = con.cursor()

        query = "SELECT amenity_name, amenity_fee FROM amenity WHERE active=1"

        cur.execute(query)

        amanities = cur.fetchall()

        con.close()

        return amanities

if __name__ == "__main__":
    MakePayment('gsingh456')
    # get_details('gsingh123', ('email', 'first_name'))
