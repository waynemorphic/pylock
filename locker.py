# The user class will contain the user details after they create an account in the password locker application
class User:
    '''
    Defines the user details. 
    '''

    user_list = []
    '''
    An empty list that stores user details
    '''

    def __init__(self, first_name, last_name, account_username, account_password):
        '''
        constructor takes in arguments that declare the user personal details
        and the password locker account credentials
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.account_username = account_username
        self.account_password = account_password
        '''
        instance variables unique to the new instance of the class
        '''

    def save_user_details(self):
        '''
        method to save user details
        '''
        User.user_list.append(self)

# The credentials class will contain the credentials (username and passwords) 
# of the user from various platforms. It will also generate new passwords automatically.
# Objective is to store generic username and password for existing platforms and create new credintials
# for new accounts using user passwords or automatically generated passwords

class Credentials:
    '''
    credentials class that stores user credentials from various platforms
    '''

    credentials_list = []
    '''
    empty list to store credentials
    '''

    def __init__(self, platform, username, password):
        '''
        constructor to generate new credentials per platform

        Takes in the name of the application, the username and password
        '''

        self.platform = platform
        self.username = username
        self.password = password
        '''
        new class variable instances
        '''

    def save_credentials(self):
        '''
        method to save the credentials
        '''

        Credentials.credentials_list.append(self)

    @classmethod
    def view_credentials(cls):
        '''
        method for displaying various credentials to the user
        '''

        return cls.credentials_list
    
    @classmethod
    def search_platform(cls, platform):
        '''
        method that takes in the name of an application and returns the credentials
        of the particular application if its credentials have been created by the user
        
        searches for existing platforms
        '''

        for application in cls.credentials_list:
            if application.platform == platform:
                return application
        # application is a variable in the credentials_list
        # returns the application that matches the name if the platform entered by the user
    