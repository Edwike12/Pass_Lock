#!/usr/bin/env python3
from credentials import Credentials
from user import User
import random
import string

# credential methods


def create_credential(account, username, password):
    '''
    Function to create a new user credentials
    '''
    new_credentials = Credentials(account, username, password)
    return new_credentials


def save_credentials(credentials):
    '''
    Funtion to save the credential
    '''
    credentials.save_credentials()


def delete_credentials(credentials):
    '''
    Function to delete a credential
    '''
    credentials.delete_credentials()


def find_credentials(account):
    '''
    Function to find a credential
    '''
    return Credentials.locate_account(account)


def check_existing_credentials(account):
    '''
    Function to check whether a credential exists
    '''
    return Credentials.locate_account(account)


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

# Users method


def create_user(username, password):
    '''
   To generate a new user credential, use this function.
    '''
    new_user = User(username, password)
    return new_user


def save_user(user):
    '''
    The user credential is saved using this function.
    '''
    user.save_user()

def main():

    print("HELLO, WELCOME TO PASSWORD LOCKER.")
    username = input("Please enter your username:")

    while True:
        print(
            f"Hello {username}, Kindly use these short codes to either sign up or login to your account.")
        print("sn - sign up to new users")
        print("lg - log into your account")
        short_code = input("Enter short code:").upper()

        if short_code == 'SN':
            print("Enter  username: ")
            username = input()

            print("Enter password")
            fpin = input()
            print('*' * 60)

            print("You are successfully registered.")
            print("Kindly, proceed to log in to your account",)
            print('\n')

        elif short_code == 'LG':
            print("Enter your username")
            username = input()

            print("Enter your password")
            pin = input()
            if f"{username } = {pin}":
                print('*' * 60)

                print(f"{username}, you've succesfully logged into your account")
                print('\n')

                pass
                while True:
                    print("Use these short codes: \n sc - Save credentials \n, cc - Create new credentials \n, dc - display credentials \n, lc - locate saved credential \n, del - delete credentials \n, ex - exit the account")

                    short_code = input()

                    if short_code == 'cc':
                        print(" Create New Credentials")
                        print("-"*40)

                        print(" Input Account: ")
                        account = input()

                        print(" Input username: ")
                        username = input()

                        print(
                            "Generate password?, respond by  YES or NO")
                        password = input().upper()
                        if password == 'YES':
                            print("What length do you want your password to be?")
                            password_length = int(input())
                            chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
                            gen_password = "".join(random.choice(
                                chars) for i in range(password_length))

                        elif password == 'NO':
                            print("Enter the password.")
                            gen_password = input()

                        else:
                            print("Wrong input, enter yes or no",)

                        # save_credentials(create_credential(account, username, gen_password))
                        # print('\n')
                        # print('-'*50)
                        # print(f"{username}, your new password has successfully  been created")
                        # print(f" Your generated password is: {gen_password}")
                        # print('-'*50)
                        # print('\n')

                    elif short_code == 'sc':
                        print("Save Existing credentials")
                        print("-"*50)

                        print(" Input account: ")
                        account = input()

                        print(" Input username: ")
                        username = input()

                        print("Input Password: ")
                        password = input()

                        save_credentials(create_credential(account, username, password))
                        print('\n')
                        print(f"{account:} credentials successfully saved")
                        print('\n')

                    elif short_code == 'dc':
                        if display_credentials():
                            print("The following is a list of all of your credentials.")
                            print('\n')

                            for credentials in display_credentials():
                                print(f"{credentials.account} {credentials.username} {credentials.password}")
                                print('\n')

                        else:
                            print('\n')
                            print("You don't seem to have any stored credentials.")
                            print('\n')

                    elif short_code == 'lc':
                        print("Please type the name of the account you're looking for below.\n")
                        search_account = input("account: ")
                        if check_existing_credentials(search_account):
                            search_account = find_credentials(search_account)
                            print(f"{search_account.username} {search_account.password}")
                            print("-"*50)

                            # print(f"Password: {search_account.password}")

                        else:
                            print("These credentials aren't available.")
                            print('\n')

                    elif short_code == 'del':
                        print(
                            "Please type the name of the account you wish to remove below.\n")
                        delete_credentials = input()
                        if check_existing_credentials(delete_credentials):
                            delete_credentials = find_credentials(delete_credentials)
                            delete_credentials(delete_credentials)

                            print("Credentials were successfully removed.")

                        else:
                            print("There are no credentials.")

                        print('-'*50)
                    elif short_code == "ex":
                        print("-"*50)

                        print("THANK YOU FOR USING PASSWORD LOCKER!!",)
                        print('\n')
                        break    



if __name__ == '__main__':
    main()