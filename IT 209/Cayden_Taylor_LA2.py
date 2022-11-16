#-------------------------------------------------------------------------------
# LA2.py
# Name: Cayden Taylor
# Python Version:  3.9.1
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Lab session
#-------------------------------------------------------------------------------
# Comments to grader: Fully implemented
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------

    
#define User class and methods: __init__, __str__ and login

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        username_str = 'username: {}'.format(self.username)
        hidden_password = 'password: ' + len(self.password)*'*'
        return username_str + '\n' + hidden_password

    def login(self, given_username, given_password):
        if self.username == given_username and self.password == given_password:
            return True
        else:
            return False
        
        

#define object u1 and u2
u1 = User('john', '1234567')
u2 = User('peter', 'abcde')


#print object u1 and u2
print('Object Created')
print(u1)
print(u2)

#call login method using u1 and pass 'john' and  '1234' as given_username and given_password
if (u1.login('john', '1234')):
    print('Welcome {}'.format(u1.username))
else:
    print('Invalid login')


#call login method using u2 and pass 'peter' and  'abcde' as given_username and given_password
if (u2.login('peter', 'abcde')):
    print('Welcome {}'.format(u2.username))
else:
    print('Invalid login')






