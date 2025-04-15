from abc import ABC, abstractmethod

class User:
    def useTool(tool):
        pass

class GuestUser(User):
    def signUp():
        pass
    def logIn():
        pass

class AccountUser(User):
    def logOut():
        pass

class FreeUser(AccountUser):
    def upgrade():
        pass

class PremiumUser(AccountUser):
    pass

class AdminUser(AccountUser):
    def toggleTool(tool):
        pass
    
    def installTool(tool):
        pass

    def uninstallTool(tool):
        pass
    
    def togglePremium(tool):
        pass


class ToolManager:
    def addTool(tool):
        pass

    def removeTool(tool):
        pass

    def executeTool(tool):
        pass

class ToolComponent:
    @abstractmethod
    def run():
        pass

    @abstractmethod
    def changeLevel(level):
        pass

class Tool(ToolComponent):
    def run():
        pass

    def changeLevel(level):
        pass