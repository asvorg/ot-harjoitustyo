"""Main code of the program"""
import functions



while True:
    while True:
        print("Select option:\n")
        print("Create user: c")
        print("Quit: q")
        print("Generate a random password: gr")
        print("Add a password: ap")
        print("List passwords of a given user: l")
        selection = input("")

        if selection == "q":
            break

        if selection == "c":
            functions.create_user()

        if selection == "gr":
            print(functions.generate_password())
            print("\n")

        if selection == "ap":
            functions.add_password()

        if selection == "l":  # not working properly yet
            functions.list_passwords()

    if selection == "q":
        quit_sure = input("Are you sure? Y/N ")
        if quit_sure == "Y":
            print("Exiting...")
            break
        print("Continuing to selection\n")
