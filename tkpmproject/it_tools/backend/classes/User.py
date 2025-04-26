from data_service.services.user_services import *
from data_service.services.user_role_services import *

class User:
    pass

class GuestUser(User):
    def sign_in(self, username, password):
        pass
    
    def sign_up(self, email, username, password):
        # Get a list of all users
        users = get_all_users()

        # Check if the email already exists
        if users.filter(email=email).exists():
            return False, "Email already exists"
        
        # Check if the username already exists
        if users.filter(username=username).exists():
            return False, "Username already exists"
    
        # Create the user with the corresponding role
        new_user = None
        if email == 'ntminh22@clc.fitus.edu.vn':    
            user_role = get_user_role_by_name('admin')
            user = create_user(username, email, password, user_role)
            new_user = AdminUser(user.id, user.email, user.username, user.password_hash)
        else:
            user_role = get_user_role_by_name('regular')
            user = create_user(username, email, password, user_role)  
            new_user = FreeUser(user.id, user.email, user.username, user.password_hash)

        return True, "User created successfully", new_user
        

class AccountUser(User):
    def __init__(self, id, email, username, password):
        self.id = id
        self.email = email
        self.username = username
        self.password = password

    def log_out(self):
        pass

class FreeUser(AccountUser):
    def __init__(self, id, email, username, password):
        super().__init__(id, email, username, password)

    def upgrade(self):
        pass

class PremiumUser(AccountUser):
    def __init__(self, id, email, username, password):
        super().__init__(id, email, username, password)

    def cancel_upgrade(self):
        pass

class AdminUser(AccountUser):
    def __init__(self, id, email, username, password):
        super().__init__(id, email, username, password)
        
    def toggle_tool(self, tool):
        pass

    def install_tool(self, tool):
        pass

    def uninstall_tool(self, tool):
        pass

    def toggle_premium(self, tool):
        pass