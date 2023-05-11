"""Main code of the program"""
from utils import functions


while True:
    functions.art()
    print("Select option:\n")
    print("Create user: c")
    print("Change the password of a specified user: cp")
    print("Quit: q")
    print("Generate a random password: gr")
    print("Add a password: ap")
    print("List passwords of a given user: l")
    print("Delete user: d")
    selection = input("")

    if selection == "q":
        quit_sure = input("Are you sure? Y/N ")
        if quit_sure == "Y":
            print("Exiting...")
            break
        print("Continuing to selection\n")

    if selection == "c":  # persistence still needed
        functions.create_user()

    if selection == "gr":
        print(functions.generate_password())
        print("\n")

    if selection == "ap":
        functions.add_password()

    if selection == "l":
        functions.list_passwords()
    
    if selection == "d":
        functions.delete_user()

