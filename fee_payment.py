"""
Assignment 6: Final Project

This file has the script for the fee payment

@author: Gagandeep Singh
Date: December 2, 2023
"""
from functions import *
from send_email import *


class MakePayment:
    def __init__(self, student_id):
        clear_terminal()
        # Printing the heading of the UI.
        print_header("FEE PAYMENT", "Red River College Polytech")

        student_dict = read_data(CURRENT_PATH, "data/student_data.pickle")

        current_student = student_dict[student_id]

        print_student_details(current_student)

        status = current_student["status"]

        # Checking if the student is already enrolled.
        if status == "Enrolled":
            print_message("ATTENTION", "you have aleady paid your fee")

        # Checking if the student is just a candidate.
        elif status == "Candidate":
            print_message("ATTENTION", "upload your documents first to pay your fee")

        elif status == "Approved":
            # Creating empty list to store courses taken.
            taken_courses = self.offer_courses()

            self.fee = self.calculate_fee(taken_courses)

            self.make_payment(student_id, current_student)

        # Saving the data for future reference
        save_data(student_dict, CURRENT_PATH, "data/student_data.pickle")

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
        taken_courses = []

        while True:
            # Asking student to select what course to take
            print("\nFrom the given list of courses, choose atleast 3:")

            # Printing the header for courses
            print("-" * 33)
            print("    COURSE NAME           FEE")
            print("-" * 33)

            for n, subject in enumerate(COURSES.keys()):
                print(
                    f"|{n+1}. {subject.title()}:"
                    f"{('$' + str(COURSES[subject][0])).rjust(COURSES[subject][1])}"
                )

            while True:
                try:
                    print(
                        "\nType the indexes of courses you want to take"
                        " separated by commas','."
                    )
                    response = input("> ")
                    courses_indexes = []
                    for x in response.split(","):
                        n = int(x.strip())
                        if n in [1, 2, 3, 4, 5]:
                            courses_indexes.append(n)
                        else:
                            raise ValueError

                    break
                except ValueError:
                    print_message("CAUTION", 'invalid input. sample input: "1, 2, 3"')

            if len(courses_indexes) >= 3:
                course_name = list(COURSES.keys())
                # printing the courses selected.
                print("\nYou have selected the following courses:")
                for n, c in enumerate(courses_indexes):
                    print(f"|{n+1}. {course_name[c-1]}")
                    taken_courses.append(course_name[c - 1])
            else:
                print_message("CAUTION", "you have to take atleast 3 courses.")
                print()
                input("\n\nPress Enter to go try again.")
                clear_terminal()

            input("\nPress Enter to continue? ")
            break
        return taken_courses

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
        for subject in COURSES.keys():
            if subject in taken_courses:
                print(
                    SPACING,
                    subject,
                    str("%.2f" % COURSES[subject][0]).rjust(7 + COURSES[subject][1]),
                    "+",
                )
                total += COURSES[subject][0]
        print()

        # Printing fee for Other expenses
        for expence in OTHER_CHARGES.keys():
            print(
                SPACING,
                expence,
                str("%.2f" % OTHER_CHARGES[expence][0]).rjust(
                    32 - OTHER_CHARGES[expence][1]
                ),
                "+",
            )
            total += OTHER_CHARGES[expence][0]

        print(SPACING, "-" * 33)
        print(SPACING, "Total", str("%.2f" % total).rjust(27))
        print(SPACING, "-" * 33)

        # Calculating the tax on the fee
        # GST
        gst = total * (GST / 100)
        print(SPACING, f"GST({GST}%):", str("%.2f" % gst).rjust(24), "+")

        # PST
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

    def make_payment(self, student_id, current_student):
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
                    valid_thru = input("Valid thru: ")
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

        if "pay" in payment_method:
            verify_email(
                current_student["email"],
                current_student["name"],
                purpose="payment",
                fee=self.fee,
            )

            # Printing the success message.
            print_message("CONGRATULATIONS", "you have paid your fee successfully")

            # Changing the student status to approved.
            current_student["status"] = "Enrolled"

            # Displaying the change of status
            print("\nYour status has now been changed to 'Enrolled'!")
            print("\nStudent status: ", current_student["status"])

            try:
                send_offer_letter(student_id, current_student)
            except Exception as e:
                print(e)

            print("\n" + "*an email has been sent to your registered email*".center(65))

        else:
            print_message("ERROR", "fee could not be paid")

            # Displaying the change of status
            print("\nYour status has not been changed to 'Enrolled'!")
            print("\nStudent status: ", current_student["status"])


if __name__ == "__main__":
    MakePayment(502156)
