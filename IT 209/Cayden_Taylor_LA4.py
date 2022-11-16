#-------------------------------------------------------------------------------
# LA4
# Student Name: Cayden Taylor
# Submission Date: 6/16/2021 
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Lab session
#-------------------------------------------------------------------------------
# Notes to grader: fully implemented
#-------------------------------------------------------------------------------

import math

class Polygon(object): #an ABC class
    '''
    This class is the base class of Polygon.
    By default it will consider the Polygon as square.
    '''
    def __init__(self, side_of_interest='', shapename=''):
        self.side_of_interest = side_of_interest #initialize side of interest
        self.shapename = shapename
        print('Enter sides of {}'.format(self.shapename))
        self.sides = [] #holds all the sides
        for i in range(self.side_of_interest): #user input
            self.sides.append(float(input("Enter side " + str(i + 1) + ": ")))

    def perimeter(self): #abstract base method
        raise NotImplementedError('Subclass must implement it')

    def area(self):  #abstract base method
        raise NotImplementedError('Subclass must implement it')


class Square(Polygon):
    side_of_interest =   1 # class variable

    def __init__(self):
         super().__init__(Square.side_of_interest, 'Square')


    def perimeter(self):
        perimeter_full = 4*self.sides[0]
        return perimeter_full

    def area(self):
        return (self.sides[0])**2
            

    #define __init__, perimeter and area methods

class Triangle(Polygon):
     side_of_interest =   3 # class variable

     def __init__(self):
         super().__init__(Triangle.side_of_interest, 'Triangle')

     def perimeter(self):
         side_A, side_B, side_C = self.sides
         perimeter_full = side_A + side_B + side_C
         return perimeter_full

     def area(self):
         side_A, side_B, side_C = self.sides
         perimeter_half = (side_A + side_B + side_C)/2
         area_value = math.sqrt(perimeter_half*(perimeter_half - side_A)*
                                   (perimeter_half - side_B)*
                                   (perimeter_half - side_C)
                                   )
         return area_value
            
            



#create Triangle and Square object

print('Creating child 1')
t = Triangle()
print('Perimeter: {:.2f}'.format(t.perimeter()))
print('Area: {:.2f}'.format(t.area()))

print('\nCreating child 2')

s = Square()
print('Perimeter: {:.2f}'.format(s.perimeter()))
print('Area: {:.2f}'.format(s.area()))














