import re


def validate_email(email):
    if not (isinstance(email, str)):
        raise Exception("Email must be a String")


def validate_password(password):
    if not (isinstance(password, str)):
        raise Exception("Password must be a String")
    elif not (re.search("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]).{8,32}$", password)):
        raise Exception("Password must contain one number,capital_alphabet, small_alphabet,and a special character")
