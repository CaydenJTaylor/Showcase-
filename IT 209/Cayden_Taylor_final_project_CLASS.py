#-------------------------------------------------------------------------------
# Final Project
# Student Name: Cayden Taylor
# Submission Date: 07/17/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Lecture vidoes, lab help, Homeworks
#-------------------------------------------------------------------------------
# Notes to grader: Fully Implemented
#-------------------------------------------------------------------------------
# Your source code below
#-------------------------------------------------------------------------------

class SmartCart(dict):
    '''dict subclass to maintain user cart'''
    def subtotal(self):
        '''Returns subtotal from a dictionary object'''
        total = 0
        for k,v in self.items():
            total += k.get_price() * v
        return total

class Item(object):
    '''Item class defines an item
    available in store. Item object saved in
    lists per category'''
    dairy_items=[] #list of all dairy items
    veg_fruit_items = [] #list of  veg and fruit items
    meat_items = [] #list of  meat and poultry items
    seafood_items = [] #list of seafood items
    
    def __init__(self, category, name, price, unit):#Initializing the start
        '''Initialization method'''
        self.__category = category.lower()
        self.__name = name.lower()
        self.__price = price.lower()
        self.__unit = unit.lower()
        #your code here
        #initialize name, price and unit as private method
        
        if self.__category == 'Dairy'.lower():#If dairy add to list
            Item.dairy_items.append(self)

        elif self.__category == 'Seafood'.lower():#if seafood add to list
            Item.seafood_items.append(self)

        elif self.__category == 'Meat'.lower():#if meat add to list
            Item.meat_items.append(self)

        elif self.__category == 'Vegatbles/Fruits'.lower():#if veg/fruit add to list
            Item.veg_fruit_items.append(self)

        #else:
            #print("Invalid Category")

        
            
            #your code here
            #append to dairy items list
        #your code here
        #elif <>:
            #append to other list as per category
            
    #your code here

    def get_category(self):#function to return category
        return self.__category
        

    def get_name(self):#function to return name
        return self.__name

    def get_price(self):#function to return price
        return self.__price

    def get_unit(self):#function to reutrn unit
        return self.__unit
    #define four get methods
    #to return four private attributes

    def __str__(self):
        line = '{}, {}, {}, {}'.format( self.get_category(), self.get_name(), \
                                        self.get_price(), self.get_unit())
        return line


#process file
with open('grocery_list.txt') as fin:
    for line in fin:
        name, category, price, unit = line.split('|') #split information
        Item(category, name, price, unit) #create Item object
        


'''Testing code to check object creationitems /category list
Comment out when done'''
def testing_code():
    for item in Item.dairy_items:
        print(item)
    print('++++++++++')

    for item in Item.veg_fruit_items:
        print(item)
    print('++++++++++')


    for item in Item.meat_items:
        print(item)
    print('++++++++++')


    for item in Item.seafood_items:
        print(item)
    print('++++++++++')

if __name__ == '__main__':
    testing_code()





          

