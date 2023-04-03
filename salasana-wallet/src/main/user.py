from main import master_password_dict

class User:

    def __init__(self,username,master_password):
        self.username = username
        self.master_password = master_password
        if self.username not in master_password_dict:
            master_password_dict[self.username] = self.master_password