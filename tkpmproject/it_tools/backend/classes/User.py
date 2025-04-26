class User:
    pass

class GuestUser(User):
    def sign_in(self, username, password):
        pass
    
    def sign_up(self, email, username, password):
        pass

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