# Online Student Portal

This is a terminal-based online student portal project written in Python. The portal allows students to register, log in, and manage their details, documents, and course fees. The application uses SQLite to store data and includes a status tracking system to monitor the student's progress through the registration process.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Database Structure](#database-structure)
- [Status Tracking](#status-tracking)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **User Authentication**: Students can register and log in. ![login](./images/login_screenshot.png)
- **Main Menu**: Main menu to choose the action to be performed. ![Menu](./images/main_menu_screenshot.png)
- **Enter Details**: Students can enter their personal details such as name, address, and contact info.
- **Upload Documents**: Students can upload their documents. ![Upload Documents](./images/documents_screenshot.png)
- **Pay Fee**: Students can choose their courses and pay the associated fees. ![Pay Fee](./images/fee_payment_screenshot.png)
- **View Details**: Students can view all their entered details. ![View Details](./images/view_details_screenshot.png)
- **Status Tracking**: The system tracks the student's progress through different statuses: Unknown (U), Candidate (C), Approved (A), Enrolled (E).
- **Email Notification**: Once the fee is paid, a letter of offer is sent to the student's registered email. ![Email](./images/email_screenshot.png)
- **Logout and Exit**: Students can log out or exit the application.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/online-student-portal.git
   cd online-student-portal
