def main():
    phonebook = {}

    while True:
        print('\nPhonebook menu')
        print('1. Add a contact')
        print('2. View all contacts')
        print('3. Search for a contact')
        print('4. Exit')

        choice = input('Choose an option: ')  # Ask for user input to choose an option

        if choice == '1':  # Add a contact
            name = input('Enter the contact\'s name: ')
            phone_number = input('Enter the contact\'s phone number: ')
            phonebook[name] = phone_number
            print(f'Contact {name} added successfully.')

        elif choice == '2':  # View all contacts
            if phonebook:
                print('\nAll Contacts:')
                for name, phone_number in phonebook.items():
                    print(f'{name}: {phone_number}')
            else:
                print('No contacts available.')

        elif choice == '3':  # Search for a contact
            search_name = input('Enter the contact\'s name to search: ')
            if search_name in phonebook:
                print(f'{search_name}: {phonebook[search_name]}')
            else:
                print(f'Contact with the name {search_name} not found.')

        elif choice == '4':  # Exit
            print('Exiting the phonebook. Goodbye!')
            break  # Exit the while loop and end the program

        else:
            print('Invalid choice. Please select a valid option.')

# Ensure the script runs the main function if it's executed directly
if __name__ == '__main__':
    main()
