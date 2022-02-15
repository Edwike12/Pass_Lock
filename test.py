import unittest # Importing the unittest module
from user import User  # Importing the user class


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
                self.new_user = User("Edwike","Nyash123") # create user object  

        def test_init(self):
                """
                test_init test case to test if the object is initialized properly
                """
                self.assertEqual(self.new_user.username,"Edwike")
                self.assertEqual(self.new_user.password,"Nyash123")



if __name__ == '__main__':
    unittest.main()                
    