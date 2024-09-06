
import os

def openFile():
    if not os.path.exists("contacts.txt"):
        f = open("contacts.txt", "x")

def add_contact():
    name = input("\t\t\tEnter the name of the contact: ")
    phone = input("\t\t\tEnter the phone number: ")
    email = input("\t\t\tEnter the email address: ")
    home_address = input("\t\t\tEnter the home address: ")

    option = input("\n\t\t\tAre you sure want to save this contact (y/n): ").lower()

    if option == 'y' or option == 'yes':
        f = open("contacts.txt", "a")
        f.write(f"{name}\t{phone}\t{email}\t{home_address}  \n")
        f.close()
        print("\t\t\tContact added successfully!")
    else:
        print("Invalid Input! Try again.")

def view_all_contact():
        f = open("contacts.txt")
        i = 0
        print("\n\n\nALL CONTACTS:")
        print("*===========*\n")
        print(f"{"S.No.".ljust(35)} {"NAME".ljust(35)}{"PHONE".ljust(35)}{"EMAIL".ljust(35)}{"HOME ADDRESS".ljust(35)}")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for line in f:
            i += 1
            info = line.split("\t")
            info.insert(0, str(i))
            for data in info:
                print(f"{data.ljust(35)}", end="")
            print("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def viewAllContact():
        pass

def updateContact():
        pass

def deleteContact():
        pass

def main_menu():
    while True:
        print("\n\n\t\t\t========================================")
        print("\t\t\t= WELCOME TO THE PHONEBOOK APPLICATION =")
        print("\t\t\t========================================")
        print()
        print("\t\t\t[1] Add Contact")
        print("\t\t\t[2] View Contact")
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
                continue

            case 3:
                view_all_contact()
                continue

            case 4:
                continue

            case 5:
                continue

            case 6:
                exit()

openFile()
main_menu()

