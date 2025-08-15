from tkinter import PhotoImage

import customtkinter
from customtkinter import *

# ---
# Data Storage
# A dictionary to store contacts. The key is the contact's name,
# and the value is another dictionary with their number and email.
# ---
contacts = {}


# ---
# Helper functions for input validation. These are great for keeping the code clean!
# ---
def is_valid_phone(number):
    """Checks if a string is a 10-digit number."""
    return number.isdigit() and len(number) == 10


def is_valid_email(email):
    """Checks for a basic email format (contains '@' and '.')."""
    return '@' in email and '.' in email


# ---
# GUI Functions
# These functions will be called by the buttons on the GUI.
# They handle the logic and update the display.
# ---
def add_contact_gui():
    """Handles adding a new contact via the GUI."""
    name = name_entry.get().strip().title()
    number = number_entry.get().strip()
    email = email_entry.get().strip()

    # Clear the entry fields after getting the input
    name_entry.delete(0, END)
    number_entry.delete(0, END)
    email_entry.delete(0, END)

    if not name or not number or not email:
        result_label.configure(text='All fields must be filled.', text_color='red')
        return

    if name in contacts:
        result_label.configure(text=f"Sorry, '{name}' already exists.", text_color='red')
    elif not is_valid_phone(number):
        result_label.configure(text='Invalid phone number (must be 10 digits).', text_color='red')
    elif not is_valid_email(email):
        result_label.configure(text='Invalid email format.', text_color='red')
    else:
        contacts[name] = {'number': number, 'email': email}
        result_label.configure(text=f"Contact '{name}' added successfully! 🎉", text_color='green')


def view_contacts_gui():
    """Displays all contacts in the text box."""
    if not contacts:
        result_label.configure(text='No contacts available.', text_color='orange')
        contact_display.delete("0.0", "end")  # Clear the text box
        contact_display.insert("end", "No contacts to display.")
    else:
        contact_display.delete("0.0", "end")  # Clear the text box before showing new data
        for name, details in contacts.items():
            contact_display.insert("end", f'Name: {name}\n')
            contact_display.insert("end", f'Phone: {details["number"]}\n')
            contact_display.insert("end", f'Email: {details["email"]}\n')
            contact_display.insert("end", "---------------------\n")  # Separator

    result_label.configure(text="Displaying all contacts.")


def search_contact_gui():
    """Searches for a contact and displays the result."""
    search_name = name_entry.get().strip().title()
    name_entry.delete(0, END)  # Clear the entry field

    if not search_name:
        result_label.configure(text="Please enter a name to search.", text_color='red')
        return

    found = False
    contact_display.delete("0.0", "end")
    for name, details in contacts.items():
        if search_name in name:
            contact_display.insert("end", f'Name: {name}\n')
            contact_display.insert("end", f'Phone: {details["number"]}\n')
            contact_display.insert("end", f'Email: {details["email"]}\n')
            contact_display.insert("end", "---------------------\n")
            found = True

    if found:
        result_label.configure(text=f"Search for '{search_name}' complete.", text_color='green')
    else:
        result_label.configure(text=f"No contacts found matching '{search_name}'.", text_color='orange')


def update_contact_gui():
    """Updates an existing contact's details."""
    name = name_entry.get().strip().title()
    number = number_entry.get().strip()
    email = email_entry.get().strip()

    # Clear the entry fields
    name_entry.delete(0, END)
    number_entry.delete(0, END)
    email_entry.delete(0, END)

    if not name:
        result_label.configure(text="Please enter a name to update.", text_color='red')
        return

    if name not in contacts:
        result_label.configure(text=f"Contact '{name}' not found.", text_color='red')
        return

    if number and not is_valid_phone(number):
        result_label.configure(text='Invalid phone number (must be 10 digits).', text_color='red')
        return

    if email and not is_valid_email(email):
        result_label.configure(text='Invalid email format.', text_color='red')
        return

    # Update fields if provided
    if number:
        contacts[name]['number'] = number
    if email:
        contacts[name]['email'] = email

    result_label.configure(text=f"Contact '{name}' updated successfully! ✅", text_color='green')


def delete_contact_gui():
    """Deletes an existing contact from the dictionary."""
    name_to_delete = name_entry.get().strip().title()
    name_entry.delete(0, END)

    if name_to_delete in contacts:
        del contacts[name_to_delete]
        result_label.configure(text=f"Contact '{name_to_delete}' deleted. 👋", text_color='green')
    else:
        result_label.configure(text=f"Contact '{name_to_delete}' not found.", text_color='red')

    # Refresh the view in case the deleted contact was visible
    view_contacts_gui()


# ---
# GUI Setup
# Here, we create the main window and all the widgets (labels, buttons, entries).
# ---
customtkinter.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

root = CTk()
root.title("Contact Management System")
root.geometry("950x650")
root.iconbitmap('img.png')

# Main title label
title_label = CTkLabel(root, text="Contact Manager", font=("Arial", 24, "bold"))
title_label.pack(pady=10)

# Frame for the input fields to keep them organized
input_frame = CTkFrame(root)
input_frame.pack(pady=10, padx=10, fill='x')

# Name input
CTkLabel(input_frame, text="Name:").pack(padx=10, pady=5, anchor='w')
name_entry = CTkEntry(input_frame, placeholder_text="Enter contact name")
name_entry.pack(fill='x', padx=10, pady=5)

# Phone number input
CTkLabel(input_frame, text="Phone Number:").pack(padx=10, pady=5, anchor='w')
number_entry = CTkEntry(input_frame, placeholder_text="Enter phone number")
number_entry.pack(fill='x', padx=10, pady=5)

# Email input
CTkLabel(input_frame, text="Email:").pack(padx=10, pady=5, anchor='w')
email_entry = CTkEntry(input_frame, placeholder_text="Enter email")
email_entry.pack(fill='x', padx=10, pady=5)

# Frame for the action buttons
button_frame = CTkFrame(root)
button_frame.pack(pady=10, padx=10, fill='x')

# The buttons that call our functions
add_button = CTkButton(button_frame, text="Add Contact", command=add_contact_gui)
add_button.pack(side="left", padx=5, pady=5, expand=True)

view_button = CTkButton(button_frame, text="View All", command=view_contacts_gui)
view_button.pack(side="left", padx=5, pady=5, expand=True)

search_button = CTkButton(button_frame, text="Search", command=search_contact_gui)
search_button.pack(side="left", padx=5, pady=5, expand=True)

update_button = CTkButton(button_frame, text="Update", command=update_contact_gui)
update_button.pack(side="left", padx=5,pady=5, expand=True)

delete_button = CTkButton(button_frame, text="Delete", command=delete_contact_gui)
delete_button.pack(side="left", padx=5, pady=5, expand=True)

# A label to show messages to the user (e.g., success or error messages)
result_label = CTkLabel(root, text="", font=("Arial", 14))
result_label.pack(pady=5)

# A Textbox widget to display all contacts or search results
contact_display = CTkTextbox(root, width=400, height=150)
contact_display.pack(pady=10)

# A button to quit the application
quit_button = CTkButton(root, text="Quit", command=root.quit, fg_color="red")
quit_button.pack(pady=10)

root.mainloop()
