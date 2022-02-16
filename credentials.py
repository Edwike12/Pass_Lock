class Credentials():
    """
    Create credentials class to help create new objects of credentials
    """
    credentials_list = []

    def __init__(self, account, username, password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            account: new_user  account.
            username: new_user username.
            password: new_user password.
            
            '''
        self.account=account    
        self.username=username
        self.password=password

    def save_credentials(self):
            '''
            method to save new credentials
            '''
            Credentials.credentials_list.append(self)   

    def delete_credentials(self):
        '''
        Delete a credential from the list using this method.
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        """
        The credential array is returned by this function.
        """
        return cls.credentials_list


    @classmethod
    def locate_account(cls, account):
        '''
        A method that accepts a account name and returns the credentials for that site.
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials             