"""Main code of the program"""
# pylint: disable=E0401
from utils import functions

functions.spawn_mongo()
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

    if functions.validate_input(selection) is False:
        break

    if selection == "q":
        quit_sure = input("Are you sure? Y/N ")
        if quit_sure == "Y":
            print("Exiting...")
            break
        print("Continuing to selection\n")

    if selection == "c":
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

    if selection == "cp":
        functions.change_master_password()
