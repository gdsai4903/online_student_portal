# Online Student Portal

#### Video Demo: []

#### Description:

The **Online Student Portal** is a Python-based terminal application designed to simulate a comprehensive student management system. The project utilizes `sqlite3` for data storage and organizes functionality across various simulated "pages" to enhance user experience.

## Features

### Login and Registration

- **Login Page:** Secure login functionality for students using their credentials.
- **Registration Page:** Allows new users to create an account and store their details in the database.

### Student Management

- **Student Page:** Provides students with an interface to view and manage their personal details and academic information.

### Fee Payment

- **Fee Payment Page:** Enables students to view their pending fees and make payments directly through the portal.

### Document Management

- **Document Page:** Allows students to upload, view, or download necessary documents such as ID cards, transcripts, or certificates.

### Terminal Page Simulation

- Each module clears the terminal and presents a new interface, simulating navigation between pages.

## Project Structure

The project is organized into multiple Python files for modularity and readability:

1. **`db_build.py`**

   - Handles the creation and initialization of the SQLite3 database.
   - Includes necessary table structures for storing user details, documents, and fee information.

2. **`index.py`**

   - The main entry point of the application.
   - Routes users to login, registration, and other modules.

3. **`login_page.py`**

   - Manages user authentication, including password validation.

4. **`students.py`**

   - Provides functionality for viewing and managing student data.

5. **`documents.py`**

   - Handles the uploading and management of documents for students.

6. **`fee_payment.py`**

   - Manages fee payment records and transactions.

7. **`mailing.py`**

   - Implements email notifications for important actions (e.g., registration confirmation, fee payment).

8. **`utils.py`**
   - Includes utility functions shared across different modules, such as input validation and formatting.

## Technical Details

- **Programming Language:** Python 3
- **Database:** SQLite3
- **Libraries Used:**
  - `sqlite3`: For database management.
  - `os`: To clear the terminal and simulate page navigation.
  - `smtplib`: For sending email notifications.
  - Other built-in Python libraries for file handling and input/output operations.

## Design Choices

- **Terminal Simulation:** The use of terminal-clearing commands (`os.system('clear')` or `os.system('cls')`) provides a simple yet effective way to simulate navigation between pages in a terminal-based environment.
- **SQLite3:** Chosen for its lightweight nature and ease of integration with Python.
- **Modularity:** The project is divided into multiple files to ensure maintainability and scalability.

## How to Run the Project

1. Clone the repository to your local machine.

   ```bash
   git clone [https://github.com/gdsai4903/online_student_portal]
   ```

2. Navigate to the project directory.

   ```bash
   cd Online-Student-Portal
   ```

3. Run the `db_build.py` script to initialize the database.

   ```bash
   python db_build.py
   ```

4. Start the application by running the `index.py` file.

   ```bash
   python index.py
   ```

5. Follow the on-screen instructions to navigate through the portal.

## Future Enhancements

- **GUI Integration:** Implement a graphical user interface for a more user-friendly experience.
- **Enhanced Security:** Add encryption for storing sensitive data like passwords.
- **Admin Panel:** Include an admin panel for managing student records and fee structures.
- **Multi-language Support:** Support for multiple languages to cater to a broader audience.

## Conclusion

The **Online Student Portal** project demonstrates the application of Python for creating a practical and modular student management system. It highlights the importance of database integration, terminal-based navigation, and modular design in software development.
