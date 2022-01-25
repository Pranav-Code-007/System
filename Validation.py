import database
import re


# It should be called while signup
def isPasswdValid(passwd):
    if len(passwd) < 8 and passwd.isspace():
        return False
    return True


# It should be checked at the time of log in only
def isPasswdCorrect(email, passwd):
    if isPasswdValid(passwd):
        if passwd == database.getPasswd(email):
            return True
    return False


# does user have created account before this
# return true if user exists
def userExists(email):
    if database.getEmail(email) == '':
        return False
    return True


def isEmailValid(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if len(email) < 10 and email.isspace() and not re.fullmatch(regex, email):
        return False
    return True


def isNumberValid(number):
    if len(number) != 10 and not number.isdigit():
        return False
    return True


def isNameValid(name):
    if len(name) < 3 and name.isspace() and name.isalpha():
        if name.find(" ") > 0:
            return False
    return True
