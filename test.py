import unittest  # Importing the unittest module
from user import User  # Importing the user class
from credentials import Credentials



class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
            unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Edwike", "Nyash123")  # create user object

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.username, "Edwike")
        self.assertEqual(self.new_user.password, "Nyash123")

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.User_list), 1)


class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
            unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials(
            "Facebook", "Invioleta", "Invi@456")  # create user object

    def tearDown(self):
        '''
        Tear down method that does clean up after each test case has run
        '''
        Credentials.credentials_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.account, "Facebook")
        self.assertEqual(self.new_credential.username, "Invioleta")
        self.assertEqual(self.new_credential.password, "Invi@456")

    def test_save_credentials(self):
        '''
        Test to check if the object is saved into the credentials list
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_delete_credentials(self):
        '''
        These test is meant to see whether we can remove credentials from our credentials list.
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials("Facebook", "Invioleta", "Invie@456")
        test_credentials.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_display_credentials(self):
        '''
        These is a test that dislays all credentials that are present in the list
        '''
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)        


if __name__ == '__main__':
    unittest.main()
