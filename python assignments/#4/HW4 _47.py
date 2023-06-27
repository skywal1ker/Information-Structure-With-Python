"""
47. You are creating a new account and need to provide a password. The password has the
following requirements:
(a) 'The password must be at least 6 characters and at most 20 characters.
(b) It must contain at least one lowercase letter, one uppercase letter, and one number.
Write a program that prompts the user to input a password and checks if the password
is valid. If the password is valid, print a confirmation statement. If it is not, print a
statement that the password is not valid.
"""
def correct_password(password):
    if len(password) < 6 or len(password) > 20:
        return False
    has_lowercase = has_uppercase = has_number = False
    for character in password:
        if character.islower():
            has_lowercase = True
        if character.isupper():
            has_uppercase = True
        if character.isdigit():
            has_number = True
    if has_lowercase and has_uppercase and has_number:
        return True
    return False

def pass_set():
    password = input('type your password: ')
    if correct_password(password):
        print('Password is correct.')
    else:
        print('Password is not correct.')
pass_set()


