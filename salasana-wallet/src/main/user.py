master_password_dict = {}  # persistence needed


class User:

    def __init__(self, username, master_password):
        self.username = username
        self.master_password = master_password
    
    def create_user(username, master_password):
        if username not in master_password_dict:
            master_password_dict[username] = master_password