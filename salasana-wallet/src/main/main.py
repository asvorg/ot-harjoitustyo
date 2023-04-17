import user


while True:
    while True:
        print("Select option:\n")
        print("Create user: c")
        print("Quit: q")
        selection = input("")

        if selection == "q":
            break

        if selection == "c":
            create_user_selection_username = input("Input username ")
            if create_user_selection_username in user.master_password_dict:
                break
            create_user_selection_master_password = input("Input password ")
            creation = user.User.create_user(create_user_selection_username,create_user_selection_username)
            print("Added " + create_user_selection_username)

    if selection == "q":
        quit_sure =  input("Are you sure? Y/N ")
        if quit_sure  == "Y":
            print("Exiting...")
            break
        else:
            print("Continuing to selection\n")