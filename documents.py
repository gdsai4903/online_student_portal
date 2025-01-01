import os
import platform
import sqlite3
import time

from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget

import utils


class Documents:
    def __init__(self, username):
        utils.print_header("UPLOAD DOCUMENTS", "Red River College Polytech")

        student_id = utils.get_student_id(username)
        status = utils.get_status(username)
        utils.print_student_details(username)

        # Checking if the student is already approved or enrolled.
        if status == "A":
            utils.print_header("UPLOAD DOCUMENTS", "Red River College Polytech")
            print("\n" + "ATTENTION".center(utils.WIDTH))
            print(("-" * 40).center(utils.WIDTH))
            print("*you have already" " uploaded your documents*".center(utils.WIDTH))

        elif status == "E":
            utils.print_header("UPLOAD DOCUMENTS", "Red River College Polytech")
            print("\n" + "ATTENTION".center(utils.WIDTH))
            print(("-" * 40).center(utils.WIDTH))
            print("*you are already enrolled, no need to submit*".center(utils.WIDTH))

        elif status == "C":
            # Asking the user to upload the documents.
            documents_upload = (
                input("\nType 'upload' to upload your documents: ").lower().strip()
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
                        self.save_docs(doc, student_id, username)

                        utils.print_message(
                            "CONGRATULATIONS",
                            "you have successfully" " uploaded your documents",
                        )

                        # Changing the student status to approved.
                        utils.set_status(username, "A")

                        # Displaying the change of status
                        print("\nYour status has now been changed to 'Approved'!")
                        print("\nStudent status: ", utils.get_status(username))
                        break

                    elif "no" in choice:
                        continue

                    elif "exit" in choice:
                        utils.print_message("ERROR", "couldn't upload documents")

                        # Displaying the change of status
                        print("\nYour status has not been changed!")
                        print("\nStudent status: ", utils.get_status(username))
                        break

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

    def save_docs(self, file_path, student_id, username):
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
            student_directory = "./documents"
            os.makedirs(student_directory, exist_ok=True)

            file_name = file_path.split("/")[-1]  # Extract the file name from the path
            new_file_name = (
                str(int(time.time()))
                + "_"
                + username
                + "_"
                + file_name.replace(" ", "_")
            )
            new_path = f"./documents/{new_file_name}"

            with open(file_path, "rb") as source, open(new_path, "wb") as destination:
                destination.write(source.read())

            con = sqlite3.connect("database/student.db")
            cur = con.cursor()

            query = """INSERT INTO document (student_id, doc_name)
                       VALUES (?,?)"""

            cur.execute(query, (student_id, new_file_name))

            con.commit()
            con.close()


class DocumentUploadApp(QWidget):
    def __init__(self):
        super().__init__()

    def show_dialog(self):
        options = QFileDialog.Options()
        options = QFileDialog.DontUseNativeDialog
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
    doc = Documents("gsingh456")
