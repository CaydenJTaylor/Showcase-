#-------------------------------------------------------------------------------
# Student Name: Taylor, Cayden 
# Version: Python 3.9.1
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Lab 8, lecture videos, supplemental source codes, textbook
#-------------------------------------------------------------------------------
# Any notes to grader: Fully implemented
#-------------------------------------------------------------------------------
# Code starts below this line
#----------------------------------------------------------------------------

import Cayden_Taylor_HA4_utility as u #import a file as u - change the file name


def main():
    
        items = ['Animal Farm, George Orwell, 1945, 19.99', 'The Great Gatsby, Scott Fitzgerald, 1934, 22.99',
                 'Jane Eyre, Charlotte Bronte, 1847, 27.99', 'Anna Karenina, Leo Tolstoy, 1877, 21.99 ',
                 'Sanctuary, William Faulkner, 1931, 30.99', 'Adventures of Huckleberry Finn, Mark Twain, 1884, 28.99']

        items_dict = u.build_dict(items)#calls a function from utility file
        cart = {} #cart initializaation
        
        print('Welcome to shopping at Amazing!')
        print('We sell books from American Novelists\nPlease choose from the following options to get information on available books')
        
        while True:
                print('\n1.Display all items')
                print('2.Add books to cart')
                print('3.Checkout')
                print('4.Quit')

                choice = input('\nEnter your option:')

                if choice == '1':
                        u.display_all_items(items_dict)
                        
                        

                elif choice == '2':
                        title = input('Enter the title of the book to add: ')
                        u.add_books_to_cart(title, cart, items_dict)
                        

                elif choice == '3':
                        u.checkout(cart)

                elif choice == '4':
                        print('The program is quitting')
                        break

                else:
                        print('Invalid option... choose 1-4')
                        
                #print menu
                #take user option
                #call appropriate function from utility file according to user input.
                

main()



