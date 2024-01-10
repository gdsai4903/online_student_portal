"""
Assignment 6: Final Project

This file contains the script for the upload documents section. 

@author: Gagandeep Singh
Date: December 2, 2023
"""
import platform
from functions import *
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget


class Documents:
    def __init__(self, student_id):
        print_header("UPLOAD DOCUMENTS", "Red River College Polytech")
        student_dict = read_data(CURRENT_PATH, "data/student_data.pickle")
        current_student = student_dict[student_id]
        name = student_dict[student_id]["name"]
        status = current_student["status"]

        print_student_details(current_student)

        # Checking if the student is already approved or enrolled.
        if status == "Approved":
            print("\n" + "ATTENTION".center(65))
            print(("-" * 40).center(65))
            print("*you have already" " uploaded your documents*".center(65))

        elif status == "Enrolled":
            print("\n" + "ATTENTION".center(65))
            print(("-" * 40).center(65))
            print("*you are already enrolled, no need to submit*".center(65))

        elif status == "Candidate":
            # Asking the user to upload the documents.
            documents_upload = (
                input("\nType 'upload' to " + "upload your documents: ").lower().strip()
            )

            # Confirming upload.
            if "upload" in documents_upload:
                while True:
                    doc = self.get_docs()
                    print("\nSelected file:", doc)
                    print("\nDo you want to upload this file?")
                    print("| 'no':   to select another file")
                    print("| 'yes':  to upload this file")
                    print("| 'exit': to cancel")
                    choice = input("> ").strip().lower()

                    if "yes" in choice:
                        self.save_docs(doc, student_id, name)

                        print_message(
                            "CONGRATULATIONS",
                            "you have successfully" " uploaded your documents",
                        )

                        # Changing the student status to approved.
                        current_student["status"] = "Approved"

                        # Displaying the change of status
                        print("\nYour status has now been changed to 'Approved'!")
                        print("\nStudent status: ", current_student["status"])
                        break

                    elif "no" in choice:
                        continue

                    elif "exit" in choice:
                        print_message("ERROR", "couldn't upload documents")

                        # Displaying the change of status
                        print("\nYour status has not been changed!")
                        print("\nStudent status: ", current_student["status"])
                        break

            student = {student_id: current_student}

            student_dict.update(student)

            save_data(student_dict, CURRENT_PATH, "data/student_data.pickle")

    def get_docs(self):
        """
        This function is to open the file explorer to select the documents that
        they wanna use.
        """
        if platform.system() == "Windows":
            import tkinter as tk
            from tkinter import filedialog
            root = tk.Tk()
            root.attributes("-topmost", True)
            root.withdraw()  # Hide the main window

            file_path = filedialog.askopenfilename(title="Select a file")

            if file_path:
                print(f"\nSelected file: {file_path}")
                return file_path
            else:
                print("No file selected.")
                return None
        else:
            app = QApplication([])
            win = DocumentUploadApp()
            path = win.show_dialog()
            win.show()
            return path

    def save_docs(self, file_path, student_id, name):
        """
        This function is to save the selected documents and save them to the
        student's dedicated folder.

        Args:
            file_path (str): path of the file to save
            student_id (int): student id of the student
            name (str): name of the student
        """
        if file_path:
            # Create a directory for the student
            student_directory = f"./documents/{student_id}_{name.replace(' ', '_')}"
            os.makedirs(student_directory, exist_ok=True)

            file_name = file_path.split("/")[-1]  # Extract the file name from the path
            new_path = f"./documents/{student_id}_{name.replace(' ', '_')}/" + file_name

            with open(file_path, "rb") as source, open(new_path, "wb") as destination:
                destination.write(source.read())


class DocumentUploadApp(QWidget):
    def __init__(self):
        super().__init__()

    def show_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        selected_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Documents",
            "",
            "All Files (*);;Documents (*.docx *.pdf *.txt)",
            options=options,
        )

        if selected_path:
            # self.label.setText(f"Selected Path: {selected_path}")
            return selected_path


if __name__ == "__main__":
    doc = Documents(763351)
