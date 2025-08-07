# Group_16
This is a basic contact management system built with Python. It allows users to perform common CRUD (Create, Read, Update, Delete) operations on a dictionary-based contact list. The application runs in the console, providing a simple and interactive way to manage contacts.

# Contact Manager

A simple command-line contact management application built with Python. This project allows users to manage a contact list through basic console commands.

## Features

- **Add Contact:** Add a new contact with a name and phone number.
- **View Contacts:** Display all contacts currently stored in the system.
- **Search Contact:** Search for a contact by name.
- **Update Contact:** Change the phone number for an existing contact.
- **Delete Contact:** Remove a contact from the list.

## How to Run

1.  Make sure you have **Python 3** installed on your machine.
2.  Save the code from `main.py` into a file named `contact_manager.py`.
3.  Open your terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the application using the following command:
    ```bash
    python contact_manager.py
    ```

## Usage

Once the application is running, you will be prompted to choose an action. Simply type the name of the action or its corresponding shortcode to perform the task.

| Action  | Shortcode | Description                     |
|---------|-----------|---------------------------------|
| `Search`  | `s`       | Find a contact by name          |
| `Update`  | `u`       | Update an existing contact's number |
| `Delete`  | `d`       | Delete a contact                |
| `Add`     | `a`       | Add a new contact               |
| `View`    | `v`       | View all contacts               |
| `Quit`    | `q`       | Exit the application            |

## Project Structure

The project consists of a single Python file with several functions:

-   `contacts`: A dictionary to store the contact data.
-   `Contacts()`: Searches for a contact.
-   `update_contact()`: Updates a contact's phone number.
-   `delete_contact()`: Deletes a contact.
-   `add_contact()`: Adds a new contact.
-   `view_contacts()`: Displays all contacts.
-   `main()`: The main loop that runs the application and handles user input.

Feel free to explore the code and see how these functions work together!

---
