# Group 16 - Contact Management System
# This program allows users to manage contacts with options to add, update, delete, search.

# A dictionary to store contacts. The key will be the contact's name,
# and the value will be another dictionary containing their number and email.
contacts = {

}

# ---
# Helper function to validate phone numbers
# ---
def is_valid_phone(number):
    """Checks if a string is a 10-digit number."""
    return number.isdigit() and len(number) == 10

# ---
#function to validate email addresses
# ---
def is_valid_email(email):
    """Checks for a basic email format (contains '@' and '.')."""
    return '@' in email and '.' in email

# ---
# Main functions for managing contacts
# ---

def add_contact():
    """Adds a new contact with checked name, phone, and email."""
    print("\n--- Add New Contact ---")
    name = input('Enter new contact name: ').strip().title()

    # Check if the contact already exists
    if name in contacts:
        print(f"Sorry, a contact named '{name}' already exists.")
        return

    # Loop until a valid 10-digit phone number is entered
    while True:
        number = input('Enter phone number (10 digits): ').strip()
        if is_valid_phone(number):
            break
        print('Invalid phone number. It must be 10 digits.')

    # Loop until a valid email format is entered
    while True:
        email = input('Enter email: ').strip()
        if is_valid_email(email):
            break
        print('Invalid email format. Please include an "@" and a ".".')

    # Store the new contact in the dictionary
    contacts[name] = {'number': number, 'email': email}
    print(f"Contact '{name}' added successfully! 🎉")

def view_contacts():
    """Displays all existing contacts."""
    print("\n--- All Contacts ---")
    if not contacts:
        print('No contacts available. Add some to get started!')
    else:
        for name, details in contacts.items():
            print(f'Name: {name}, Phone: {details["number"]}, Email: {details["email"]}')

def search_contact():
    """Searches for a contact by name and displays their details."""
    print("\n--- Search Contacts ---")
    search_name = input('Enter a name to search: ').strip().title()
    found_contacts = []

    # Find all contacts that contain the search name (case-insensitive)
    for name, details in contacts.items():
        if search_name in name:
            found_contacts.append((name, details))

    if not found_contacts:
        print(f"No contacts found matching '{search_name}'.")
    else:
        print("Found the following contacts:")
        for name, details in found_contacts:
            print(f'Name: {name}, Phone: {details["number"]}, Email: {details["email"]}')

def update_contact():
    """Updates the phone and email of an existing contact."""
    print("\n--- Update Contact ---")
    update_name = input('Enter the name of the contact to update: ').strip().title()

    if update_name in contacts:
        print(f"Updating details for '{update_name}'.")

        # Get and validate the new phone number
        while True:
            new_number = input('Enter new phone number (10 digits): ').strip()
            if is_valid_phone(new_number):
                contacts[update_name]['number'] = new_number
                break
            print('Invalid phone number. It must be 10 digits.')

        # Get and validate the new email
        while True:
            new_email = input('Enter new email: ').strip()
            if is_valid_email(new_email):
                contacts[update_name]['email'] = new_email
                break
            print('Invalid email format. Please include an "@" and a ".".')

        print(f"Contact '{update_name}' updated successfully! ✅")
    else:
        print(f"Contact '{update_name}' not found.")

def delete_contact():
    """Deletes an existing contact."""
    print("\n--- Delete Contact ---")
    name_to_delete = input('Enter the name of the contact to delete: ').strip().title()

    if name_to_delete in contacts:
        del contacts[name_to_delete]
        print(f"Contact '{name_to_delete}' deleted successfully. 👋")
    else:
        print(f"Contact '{name_to_delete}' not found.")


def main():
    """Main loop to run the contact management system."""
    print("Welcome to the Contact Management System! 📖")
    while True:
        print("\nWhat would you like to do?")
        print("  [A]dd a new contact")
        print("  [V]iew all contacts")
        print("  [S]earch for a contact")
        print("  [U]pdate an existing contact")
        print("  [D]elete a contact")
        print("  [Q]uit the program")

        action = input('Your choice: ').strip().lower()

        if action in ['add', 'a']:
            add_contact()
        elif action in ['view', 'v']:
            view_contacts()
        elif action in ['search', 's']:
            search_contact()
        elif action in ['update', 'u']:
            update_contact()
        elif action in ['delete', 'd']:
            delete_contact()
        elif action in ['quit', 'q']:
            print("Thanks for using the Contact Management System. Goodbye! 👋")
            break
        else:
            print('Invalid action. Please choose from the options above.')

# This line ensures the main function runs when the script is executed.
if __name__ == "__main__":
    main()