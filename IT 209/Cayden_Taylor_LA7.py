#-------------------------------------------------------------------------------
# LA7.py
# Name: Cayden Taylor 
# Python Version:  3.9.1
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

#define ValidString class - a subclass of str class
#your code here
class ValidString(str):
    def isvalid(self):
        for char in self:
            if char.isdigit():
                return False
        return True

    def __str__(self):
        if self.isvalid():
            return self
        else:
            return "Invalid String"



    
#sample object creation
s1 = ValidString('ABC') 
s2 = ValidString('AS123')
print('s1 valid? ', s1.isvalid())
print('s2 valid? ', s2.isvalid())
print(s1)
print(s2)
