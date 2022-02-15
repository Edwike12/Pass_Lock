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