from random import randint

contacts = {
    'Kofi': str(randint(100000000, 999999999)),
    'Ama': str(randint(100000000, 999999999)),
    'Kojo': str(randint(100000000, 999999999))
}

def search_contact():
    search_name = input('Name to search: ').lower()
    found = False
    for name, info in contacts.items():
        if search_name in name.lower():
            print(f'Name: {name}\nDetails: {info}\n')
            found = True
    if not found:
        print('No matching contact found.')

def update_contact():
    name = input('Name to update: ')
    if name in contacts:
        new_number = input('New number: ')
        contacts[name] = new_number
        print(f'{name} updated.')
    else:
        print('Contact not found.')

def delete_contact():
    name = input('Name to delete: ')
    if name in contacts:
        del contacts[name]
        print(f'{name} deleted.')
    else:
        print('Contact not found.')

def add_contact():
    name = input('New contact name: ')
    if name in contacts:
        print('Contact already exists.')
    else:
        number = input('Phone number: ')
        contacts[name] = number
        print(f'{name} added.')

def view_contacts():
    if contacts:
        for name, number in contacts.items():
            print(f'{name}: {number}')
    else:
        print('No contacts available.')

def main():
    while True:
        print('Choose an action: Search, Update, Delete, Add, View')
        action = input(': ').lower()

        if action in ['search', 's']:
            search_contact()
        elif action in ['update', 'u']:
            update_contact()
        elif action in ['delete', 'd']:
            delete_contact()
        elif action in ['add', 'a']:
            add_contact()
        elif action in ['view', 'v']:
            view_contacts()
        elif action.lower in ['q','quit']:
            break
        else:
            print('Invalid action.')


main()