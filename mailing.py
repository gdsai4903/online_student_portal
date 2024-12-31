"""
Assignment 6: Final Project

This file contains the script to send the mails for otp and offer letters.

@author: Gagandeep Singh
Date: December 2, 2023
"""

import datetime
import random
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils import get_details, print_message

RRC_image = "images/RRC-Polytech-Horizontal.png"
date = datetime.date.today().strftime("%B %d, %Y")

SENDER_EMAIL = "gdsai4903@gmail.com"


def send_offer_letter(username):
    """
    To send the offer letter to the registered email.

    Args:
        student_id (int): the student id of the student
        student (dict): the student's data dictionary
    """
    # Email configuration
    details = get_details(username)
    student_id = details[0]
    name = details[1] + " " + details[2]
    dob = details[3]
    receiver_email = details[4]
    phone = details[7]
    address = details[8]

    subject = "OFFER LETTER"

    # Offer letter in HTML
    body = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>file_1701197481442</title>
    <meta name="author" content="{name}" />
    <style type="text/css">
      * {{
          margin: 0;
          padding: 0;
          text-indent: 0;
        }}
      h1 {{
          color: black;
          font-family: Calibri, sans-serif;
          font-style: normal;
          font-weight: bold;
          text-decoration: none;
          font-size: 9pt;
        }}
      .s1 {{
          color: black;
          font-family: Calibri, sans-serif;
          font-style: normal;
          font-weight: normal;
          text-decoration: none;
          font-size: 9pt;
        }}
      .s2 {{
          color: black;
          font-family: "Calibri Light", sans-serif;
          font-style: normal;
          font-weight: normal;
          text-decoration: none;
          font-size: 18pt;
        }}
      .s3 {{
          color: #2e5395;
          font-family: "Calibri Light", sans-serif;
          font-style: normal;
          font-weight: normal;
          text-decoration: none;
          font-size: 14pt;
        }}
      .s4 {{
          color: black;
          font-family: Calibri, sans-serif;
          font-style: normal;
          font-weight: bold;
          text-decoration: none;
          font-size: 11pt;
        }}
      .s5 {{
          color: black;
          font-family: Calibri, sans-serif;
          font-style: normal;
          font-weight: normal;
          text-decoration: none;
          font-size: 11pt;
        }}
      .s6 {{
          color: #0462c1;
          font-family: Calibri, sans-serif;
          font-style: normal;
          font-weight: normal;
          text-decoration: underline;
          font-size: 11pt;
        }}
      .s7 {{
          color: black;
          font-family: Calibri, sans-serif;
          font-style: normal;
          font-weight: normal;
          text-decoration: none;
          font-size: 11pt;
        }}
      p {{
          color: black;
          font-family: Calibri, sans-serif;
          font-style: normal;
          font-weight: normal;
          text-decoration: none;
          font-size: 11pt;
          margin: 0pt;
        }}
      .a,
      a {{
          color: black;
          font-family: Calibri, sans-serif;
          font-style: normal;
          font-weight: normal;
          text-decoration: none;
          font-size: 11pt;
        }}
      table,
      tbody {{
          vertical-align: top;
          overflow: visible;
        }}
    </style>
  </head>
  <body>
    <p style="padding-left: 5pt; text-indent: 0pt; text-align: left">
      <span
        ><table border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td><img width="316" height="46" src="cid:image1" /></td>
          </tr></table
      ></span>
    </p>
    <p style="text-indent: 0pt; text-align: left"><br /></p>
    <h1 style="padding-top: 3pt; text-indent: 0pt; text-align: left">
      Date<span class="s1">: {date}</span>
    </h1>
    <p style="text-indent: 0pt; text-align: left"><br /></p>
    <p class="s2" style="padding-left: 0pt; text-indent: 0pt; text-align: left">
      OFFER OF ADMISSION (LETTER OF ACCEPTANCE)
    </p>
    <p
      class="s3"
      style="
        padding-top: 12pt;
        padding-left: 5pt;
        text-indent: 0pt;
        text-align: left;
      "
    >
      PERSONAL INFORMATION
    </p>
    <p style="text-indent: 0pt; text-align: left"><br /></p>
    <table
      style="border-collapse: collapse; margin-left: 5.25pt"
      cellspacing="0"
    >
      <tr style="height: 27pt">
        <td
          style="
            width: 275pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Name
          </p>
          <p
            class="s5"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 12pt;
              text-align: left;
            "
          >
            {name.title()}
          </p>
        </td>
        <td
          style="
            width: 274pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Date of Birth
          </p>
          <p
            class="s5"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 12pt;
              text-align: left;
            "
          >
            {dob}
          </p>
        </td>
      </tr>
      <tr style="height: 27pt">
        <td
          style="
            width: 275pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Student Id
          </p>
          <p
            class="s5"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            {student_id}
          </p>
        </td>
        <td
          style="
            width: 274pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Phone
          </p>
          <p
            class="s5"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            {phone}
          </p>
        </td>
      </tr>
      <tr style="height: 27pt">
        <td
          style="
            width: 275pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Email
          </p>
          <p
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 12pt;
              text-align: left;
            "
          >
            <a href="mailto:gdsai4903@gmail.com" class="s6"
              >{receiver_email}</a
            >
          </p>
        </td>
        <td
          style="
            width: 274pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Address
          </p>
          <p
            class="s5"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 12pt;
              text-align: left;
            "
          >
            {address.title()}
          </p>
        </td>
      </tr>
    </table>
    <p style="text-indent: 0pt; text-align: left"><br /></p>
    <p class="s3" style="padding-left: 5pt; text-indent: 0pt; text-align: left">
      INSTITUTION INFORMATION
    </p>
    <p style="text-indent: 0pt; text-align: left"><br /></p>
    <table
      style="border-collapse: collapse; margin-left: 5.25pt"
      cellspacing="0"
    >
      <tr style="height: 41pt">
        <td
          style="
            width: 275pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Full Name of Institution
          </p>
          <p
            class="s5"
            style="padding-left: 5pt; text-indent: 0pt; text-align: left"
          >
            Red River College Polytechnic
          </p>
        </td>
        <td
          style="
            width: 276pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Address of Institution
          </p>
          <p
            class="s5"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            D105 - 2055 Notre Dame Avenue
          </p>
          <p
            class="s5"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 12pt;
              text-align: left;
            "
          >
            Winnipeg, Manitoba, Canada R3H 0J9
          </p>
        </td>
      </tr>
      <tr style="height: 33pt">
        <td
          style="
            width: 275pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Type of School/Institution
          </p>
          <p
            class="s5"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Public Post – Secondary
          </p>
        </td>
        <td
          style="
            width: 276pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Website
          </p>
          <p
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            <a href="http://www.rrc.ca/" class="s7">www.rrc.ca</a>
          </p>
        </td>
      </tr>
      <tr style="height: 32pt">
        <td
          style="
            width: 275pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Email
          </p>
          <p style="padding-left: 5pt; text-indent: 0pt; text-align: left">
            <a href="mailto:international@rrc.ca" class="s7"
              >international@rrc.ca</a
            >
          </p>
        </td>
        <td
          style="
            width: 276pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Telephone
          </p>
          <p
            class="s5"
            style="padding-left: 5pt; text-indent: 0pt; text-align: left"
          >
            204-632-2327
          </p>
        </td>
      </tr>
    </table>
    <p style="text-indent: 0pt; text-align: left"><br /></p>
    <p class="s3" style="padding-left: 5pt; text-indent: 0pt; text-align: left">
      PROGRAM INFORMATION
    </p>
    <p style="text-indent: 0pt; text-align: left"><br /></p>
    <table
      style="border-collapse: collapse; margin-left: 5.25pt"
      cellspacing="0"
    >
      <tr style="height: 32pt">
        <td
          style="
            width: 138pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Academic Status
          </p>
          <p
            class="s5"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Full Time
          </p>
        </td>
        <td
          style="
            width: 139pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Hours of instructions/week
          </p>
          <p
            class="s5"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            25 - 30
          </p>
        </td>
        <td
          style="
            width: 277pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Field/Program of Study
          </p>
          <p
            class="s5"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Data Science and Machine Learning Diploma
          </p>
        </td>
      </tr>
      <tr style="height: 33pt">
        <td
          style="
            width: 277pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
          colspan="2"
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Credential and Year of Study
          </p>
          <p
            class="s5"
            style="padding-left: 5pt; text-indent: 0pt; text-align: left"
          >
            Year 1
          </p>
        </td>
        <td
          style="
            width: 277pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Type of Training Program
          </p>
          <p
            class="s5"
            style="padding-left: 5pt; text-indent: 0pt; text-align: left"
          >
            College level studies
          </p>
        </td>
      </tr>
      <tr style="height: 54pt">
        <td
          style="
            width: 277pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
          colspan="2"
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Exchange Program
          </p>
          <p
            class="s5"
            style="padding-left: 5pt; text-indent: 0pt; text-align: left"
          >
            NO
          </p>
        </td>
        <td
          style="
            width: 277pt;
            border-top-style: solid;
            border-top-width: 1pt;
            border-left-style: solid;
            border-left-width: 1pt;
            border-bottom-style: solid;
            border-bottom-width: 1pt;
            border-right-style: solid;
            border-right-width: 1pt;
          "
        >
          <p
            class="s4"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 13pt;
              text-align: left;
            "
          >
            Estimated Tuition Fee for Two Semesters
          </p>
          <p
            class="s5"
            style="padding-left: 5pt; text-indent: 0pt; text-align: left"
          >
            Program Fees: $20,660.00
          </p>
          <p
            class="s5"
            style="padding-left: 5pt; text-indent: 0pt; text-align: left"
          >
            Books and supplies purchased separately. The estimated
          </p>
          <p
            class="s5"
            style="
              padding-left: 5pt;
              text-indent: 0pt;
              line-height: 12pt;
              text-align: left;
            "
          >
            cost for the first year is $2,000.00.
          </p>
        </td>
      </tr>
    </table>
    <p style="text-indent: 0pt; text-align: left"><br /></p>
    <p
      style="
        padding-top: 2pt;
        padding-left: 0pt;
        text-indent: 0pt;
        text-align: center;
      "
    >
      D105 – 2055 Notre Dame Avenue, Winnipeg, Manitoba, Canada R3H 0J9
    </p>
    <p style="padding-left: 0pt; text-indent: 0pt; text-align: center">
      <a href="mailto:international@rrc.ca" class="a" target="_blank"
        >Telephone: 204-632-2327 | Fax: 204-697-0584| Email: </a
      ><a href="http://www.rrc.ca/international" class="a" target="_blank"
        >international@rrc.ca | </a
      ><a href="http://www.rrc.ca/international" target="_blank"
        >www.rrc.ca/international</a
      >
    </p>
  </body>
</html>

"""

    send_mail(receiver_email, subject, body)


def send_otp(username, otp, purpose, fee=None, **kwargs):
    """
    Send email for otp

    Args:
      username(str): username of the sutdent
      otp (int): otp
      purpose (str): purpose of otp
      fee (float): fee of otp
    """

    # OTP email in HTML
    if purpose == "register":
        # Email configuration
        receiver_email = kwargs["email"]
        student_name = kwargs["first_name"] + " " + kwargs["last_name"]

        subject = "Email Verification OTP."
        body = f"""<html>
                <body>
                    <p><img src="cid:image1"></p>
                    <p>Dear {student_name},</p>
                    <p>Thank you for registering with Red River College Polytechnic.</p>
                    <p>Your verification code is: {otp}.</p>
                    <p>Do NOT share this with anyone.</p>
                    <p>If you did not initiate this request, please ignore this email.</p>
                </body>
            </html>"""

    elif purpose == "payment":
        details = get_details(username, ("email", "first_name", "last_name"))[0]
        receiver_email = details[0]
        student_name = details[1] + " " + details[2]

        subject = "Payment Verification OTP."
        body = f"""<html>
                <body>
                    <p><img src="cid:image1"></p>
                    <p>Dear {student_name},</p>
                    <p>This is an email to verify the transaction on your account of ${"%.2f"%fee}.</p>
                    <p></p>
                    <p>Your verification code is: {otp}.</p>
                    <p>Do NOT share this with anyone.</p>
                    <p>If you did not initiate this request, please ignore this email.</p>
                </body>
            </html>"""

    send_mail(receiver_email, subject, body)


def verify_email(username, purpose="register", fee=None, **kwargs):
    """
    Verify email

    Args:
    student_email (str): student email
    purpose (str): purpose
    fee (float): total amount of fee due
    """
    # creating otp
    otp = random.randint(100000, 999999)

    # Sending otp via email
    send_otp(username, otp, purpose, fee, **kwargs)
    email = get_details(username, ("email",))[0]
    while True:
        try:
            recieved = int(input(f"\nEnter OTP sent to your email ({email}): "))

            # verifying otp
            if not recieved == otp:
                raise ValueError

            print_message("SUCCESS", "email verified successfully")
            break

        except ValueError:
            print_message("WARNING", "OTP doesn't match")

    # Printing blank line for clean UI
    print()


def send_mail(receiver, subject, body):
    """
    Send email

    Args:
      SENDER_EMAIL (str): sender email
      receiver (str): receiver email
      subject (str): subject
      body (str): body
    """
    # Create the MIME object
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = receiver
    message["Subject"] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, "html1"))

    # Open the image file and attach it to the email
    with open(RRC_image, "rb") as image_file:
        image = MIMEImage(image_file.read())
        image.add_header("Content-ID", "<image1>")
        message.attach(image)

    message.attach(MIMEText(body, "html"))

    # SMTP server setup for Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Start the SMTP session
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Login to your Gmail account using the app-specific password
    with open("./key.txt", "r") as f:
        app_password = f.readline()

    server.login(SENDER_EMAIL, app_password)

    # Send the email
    server.sendmail(SENDER_EMAIL, receiver, str(message))

    # Quit the SMTP server
    server.quit()


if __name__ == "__main__":
    # send_otp('gdsai4903@gmail.com', 1234)
    # verify_email('gsingh456')
    print(get_details("gsingh123", ("email", "first_name", "last_name"))[0])
