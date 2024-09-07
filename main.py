
import os

def open_file():
    if not os.path.exists("contacts.txt"):
        f = open("contacts.txt", "x")

def add_contact():
    # Prompt the user to enter contact details
    name = input("\t\t\tEnter the name of the contact: ")
    phone = input("\t\t\tEnter the phone number: ")
    email = input("\t\t\tEnter the email address: ")
    home_address = input("\t\t\tEnter the home address: ")

    # Ask the user for confirmation to save the contact
    option = input("\n\t\t\tAre you sure you want to save this contact (y/n): ").lower()

    if option == 'y' or option == 'yes':
        # Open the file in append mode and write the new contact details
        f = open("contacts.txt", "a")
        f.write(f"{name}\t{phone}\t{email}\t{home_address}\n")
        f.close()
        print("\t\t\tContact added successfully!")
    else:
        # Notify the user if the input is not 'y' or 'yes'
        print("Invalid Input! Try again.")


def view_all_contact():
    # Open the file containing contacts in read mode
    f = open("contacts.txt")

    i = 0
    # Print header for the contact list
    print("\n\n\nALL CONTACTS:")
    print("*===========*\n")
    print(f"{'S.No.'.ljust(35)} {'NAME'.ljust(35)}{'PHONE'.ljust(35)}{'EMAIL'.ljust(35)}{'HOME ADDRESS'.ljust(35)}")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    # Iterate over each line in the file
    for line in f:
        i += 1
        # Split the line into fields based on tab characters
        info = line.split("\t")
        # Insert the serial number at the beginning of the list
        info.insert(0, str(i))
        # Print each field, left-justified to a width of 35 characters
        for data in info:
            print(f"{data.ljust(35)}", end="")
        # Print a separator line after each contact
        print("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    # Close the file after reading
    f.close()


def search_contact():
    pass

def update_contact():
    pass

def delete_contact():
    # Prompt the user to enter the phone number they want to delete
    phone_number = input("\t\t\tEnter the phone number you want to delete:")

    # Open the file containing contacts in read mode
    file = open("contacts.txt", "r")

    is_matched = False

    # Check if the phone number exists in the file
    for record in file:
        fields  = record.split("\t")
        for field in fields:
            if field == phone_number:
                is_matched = True
                break
            if is_matched:
                break

    # If the phone number is not found, notify the user and exit the function
    if not is_matched:
        print("\t\t\tThis phone number not found!")
        return

    # List to store records that do not match the phone number
    unmatched_records = []
    file.seek(0)

    # Collect all records except the one with the phone number to be deleted
    for record in file:
        is_matched = False
        fields  = record.split("\t")
        for field in fields:
            if field == phone_number:
                is_matched = True
                break
        if is_matched:
            continue
        else:
            unmatched_records.append(record)

    # Close the file after reading
    file.close()

    # Open the file in write mode to clear its contents
    file = open("contacts.txt", "w")
    file.write("")

    # Reopen the file in append mode to write back the unmatched records
    file = open("contacts.txt", "a")
    for record in unmatched_records:
        file.write(record)

    # Close the file after writing
    file.close()

    # Notify the user that the phone number has been deleted successfully
    print("\t\t\tThis phone number has been deleted successfully.")

def main_menu():
    while True:
        print("\n\n\t\t\t========================================")
        print("\t\t\t= WELCOME TO THE PHONEBOOK APPLICATION =")
        print("\t\t\t========================================")
        print()
        print("\t\t\t[1] Add Contact")
        print("\t\t\t[2] Search Contact")
        print("\t\t\t[3] View All Contact")
        print("\t\t\t[4] Update Contact")
        print("\t\t\t[5] Delete Contact")
        print("\t\t\t[6] Exit")

        option = int(input("\n\t\t\tPlease select an option (1-6): "))

        match option:
            case 1:
                add_contact()
                continue

            case 2:
                search_contact()
                continue

            case 3:
                view_all_contact()
                continue

            case 4:
                continue

            case 5:
                delete_contact()
                continue

            case 6:
                exit()

open_file()
main_menu()

