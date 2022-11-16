#-------------------------------------------------------------------------------
# LA5.py
# Name: Cayden Taylor
# Python Version: 3.9.1
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Lab session
#-------------------------------------------------------------------------------
# Comments to grader: Fully Implemented
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------

#helper functions
def has_digit(password):
    '''
    Checks if a password string has at least one digit.
    Returns True if at least one digit is present, False otherwise
    '''
    return any([char.isdigit() for char in password])

def has_letter(password):
    '''
    Checks if a password string has at least one letter.
    Returns True if at least one letter is present, False otherwise
    '''
    return any([(ord(c)>= 97 and ord(c) <=122) \
                or (ord(c)>= 65 and ord(c) <=90) for c in password])

class InvalidPassword(Exception):
    pass

class InsufficentLength(InvalidPassword):
    def __str__(self):
        return "Length of password must be between 6 to 12 characters."


class NoDigit(InvalidPassword):
    def __str__(self):
        return "Password must contain at least one digit (0-9)."


class NoLetter(InvalidPassword):
    def __str__(self):
        return "Password must contain at least one letter."


while True:
    try:
        password = input("Enter your password: ")

        if len(password) <6 or len(password) >12:
            raise InsufficentLength
        elif has_digit(password) == False:
            raise NoDigit
        elif has_letter(password) == False:
            raise NoLetter
        else:
            break
    except InsufficentLength as i:
        print(i)
    except NoDigit as i:
        print(i)
    except NoLetter as i:
        print(i)


print('Valid password: {}'.format(password))
            
        





