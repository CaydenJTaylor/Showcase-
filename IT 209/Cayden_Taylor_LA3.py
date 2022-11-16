#-------------------------------------------------------------------------------
# I=LA3.py
# Name: Cayden Taylor
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Lab instructor
#-------------------------------------------------------------------------------
# Comments to grader: Fully implemented 
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------

# Define class rectangle

class Rectangle():
    #defining init function for rectangle
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return "length = {} \n width = {}".format(self.length,self.width)


    def area(self):
        return self.length * self.width #computing area

    def increase_size(self, l, w):
        self.length += l
        self.width += w


# define class cuboid
class Cuboid(Rectangle):
    def __init__(self, length, width, depth):
        super(Cuboid, self).__init__(length,width)
        self.depth = depth

    def __str__(self):
        return super().__str__() + '\n' + "depth ={}".format(self.depth)

    def volume(self):
        return super().area()*self.depth

    def increase_size(self, l, w, d):
        super().increase_size(l, w)
        self.depth += d



# Create object Rectangle
r1 = Rectangle(1, 2)

# Print dimensions
print(r1)
# Print area
print("Initial area of r1 is")
# increase dimensions
r1.increase_size(1,1)
# Print dimensions
print(r1)
# print area
print("New area of r1 is", r1.area())

# Create object Cuboid
c1 = Cuboid(1,2,3)
# Print dimensions
print(c1)
# Print volume
print("Initial volume of c1 is", c1.volume())

# increase dimensions
c1.increase_size(1,1,1)
# Print dimensions
print(c1)
# print area
print("New voulme of c1 is",c1.volume())



      
