#-------------------------------------------------------------------------------
# HA2
# Student Name: Cayden Taylor
# Python version: 3.9.1
# Submission Date: 6/25/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#---------------------------------------------------------------------------
# References: Hw 1 lab 4, lab 5, lab 6, sample codes
#-------------------------------------------------------------------------------
# Notes to grader: Fully implemented, one of my 48hr grace period late submissions
#-------------------------------------------------------------------------------
# Source code below
#-------------------------------------------------------------------------------

#define cart class - a subclass of list class
class Cartlist(list): #defining cart class which is a list. Similar to inheritance lecture
    def __getitem__(self, item):
        return super(Cartlist, self).__getitem__(item)

    def subtotal(self):#extending class to define subttotal, tax and total 
        total = 0.00
        for pie in self:
            total += pie.get_price()
        return total

    def tax(self):
        return self.subtotal() *.0325

    def total(self):
        return self.subtotal() + self.tax()

#define Pizza class
class pizza: #defining pizza class and calling list class
    Cartlist = Cartlist()

    def __init__(self, crust, sauce, size):
        self.crust = crust
        self.sauce = sauce
        self.size = size

    def __str__(self):
        return self.crust + ' ' + 'crust' + ' ' + self.sauce + ' ' + 'sauce' + ' ' + self.size
        
    


#define Cheese Pizza, Meat Pizza and Veggie Pizza class
class cheese(pizza):
    price = {'small':10.99, 'medium':12.99, 'large':14.99}

    def __init__(self, crust, sauce, size, option):
        super().__init__(crust, sauce, size) #use super class to save time can calls pizza __init__
        self.option = option

    def __str__(self):
        return super().__str__() + ' ' + 'with' + ' ' + self.option

    def get_price(self):
        return cheese.price[self.size]


class meat(pizza):
    price = {'small':12.99, 'medium':15.99, 'large':19.99}

    def __init__(self, crust, sauce, size, option):
        super().__init__(crust, sauce, size)
        self.option = option

    def __str__(self):
        return super().__str__() + ' ' + 'with' + ' ' + self.option

    def get_price(self):
        return meat.price[self.size]



class veggie(pizza):
    price = {'small':11.99, 'medium':13.99, 'large':15.99}

    def __init__(self, crust, sauce, size, option):
        super().__init__(crust, sauce, size)
        self.option = option

    def __str__(self):
        return super().__str__() + ' ' + 'with' + ' ' + self.option

    def get_price(self):
        return veggie.price[self.size]
    



#main function/global code
#take user input on pizza type, size, crust and sauce
#create object depending on type

def main():
    proceed = 'yes' #initalizing loop
    
    print("********Welcome to Mason Pizza********")
    while proceed == 'yes':#loop
        option = input("\nEnter type of pizza (cheese/meat/veggie): ")
        size = input("Enter size (small/medium/large): ")
        crust = input("Enter crust (thin/thick): ")
        sauce = input("Enter sauce (white/classic red): ")

        if option == 'cheese':
            cheese_option = input("Enter cheese type (mozzarella/ parm): ")
            cheese_pizza = cheese(crust, sauce, size, cheese_option)
            pizza.Cartlist.append(cheese_pizza) #add each object to list

        elif option == 'meat':
            meat_option = input("Enter meat type (chicken/beef/ham): ")
            meat_pizza = meat(crust, sauce, size, meat_option)
            pizza.Cartlist.append(meat_pizza)


        elif option == 'veggie':
            veggie_option = input("Enter veggie type (spinach/bell pepper): ")
            veggie_pizza = veggie(crust, sauce, size, veggie_option)
            pizza.Cartlist.append(veggie_pizza)


        proceed = input("Do you want to continue ordering? (yes/no): ")
        if proceed == 'yes': #loop
            continue
        else:
            pass
        
#Print receipt
#calculate subtotal, tax and total. 

        print("********Printing Receipt********")
        for pie in range(len(pizza.Cartlist)): #for loop to go through each pizza object
            print("\npizza", (pie+1))
            print(pizza.Cartlist[pie])

        
        print("\nSubtotal: ${:.2f}".format(pizza.Cartlist.subtotal()))#format each to only show 2 decimals 
        print("Tax: ${:.2f}".format(pizza.Cartlist.tax()))
        print("Total: ${:.2f}".format(pizza.Cartlist.total()))

        print("\n********Thank You!********")


main()
        

        
        



