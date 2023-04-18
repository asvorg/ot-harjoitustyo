#import user
import hashlib as hl
import functions
import persistent


while True:
    while True:
        print("Select option:\n")
        print("Create user: c")
        print("Quit: q")
        print("Generate a random password: gr")
        print("Add a password: ap")
        selection = input("")

        if selection == "q":
            break

        if selection == "c":
            create_user_selection_username = input("Input username ")
            create_user_selection_master_password = input(
                "Input master password ")

            if create_user_selection_username in persistent.users_dict:
                print("Already in use")
                break
            persistent.users_dict[create_user_selection_username] = hl.sha256(
                create_user_selection_master_password.encode())
            # print(persistent.users_dict)

        if selection == "gr":
            length = input("Desired password length: \n")
            print(functions.generate_password(int(length)))
            print("\n")

        if selection == "ap":  # broken
            functions.add_password()

    if selection == "q":
        quit_sure = input("Are you sure? Y/N ")
        if quit_sure == "Y":
            print("Exiting...")
            break
        print("Continuing to selection\n")
