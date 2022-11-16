#-------------------------------------------------------------------------------
# Student Name: Cayden Taylor
# Assignment: Final Project
# Python version: 3.9
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Textbook, Python Documentation, previous HW's and labs
#-------------------------------------------------------------------------------
# Notes: had difficulties with the add item and write function 
#-------------------------------------------------------------------------------

import Cayden_Taylor_final_project_utility as u #change the name of the file

import Cayden_Taylor_final_project_utility as u

def build_dict():
    '''
    Returns item type dictionary created from input file
    where key is an item id and
    value is a list of rest of the information
    '''
    file = open("library.txt", "r")
    raw_list = list(file.readlines())#reads each line of .txt file

    file_list = []
    for element in raw_list:#for loop to remove '\n' in list
        file_list.append(element.strip())

    books = {}
    magazines = {}

    for item in file_list:
        ID,item_type,title,info,volume_ISBN,author_issue,num_copies = item.split(',')#formats list of books and magazines
        if item_type == 'book':
            books[ID]= title,info,volume_ISBN,author_issue,num_copies

        if item_type == 'magazine':
            magazines[ID]= title,info,volume_ISBN,author_issue,num_copies
       #your code here
    return books, magazines


def write_to_file(books, magazines):
    '''
    Writes the updated user information toinput file
    '''
    
    

    print('Updating library information....')
    
    #your code here
    
def main():
    print('\n\n********** Welcome to 209-Library *************')
    books, magazines= build_dict()
    cart={} #user cart
    option = 0
    
    while option!=5:
        #display main menu
        print('1.Display all items\n2.Search\n3.Remove an item from cart\n4.Checkout\n5.Exit Application')
        option = int(input('Enter option (1-5): '))
        if option == 1:
            u.display_all_items(books, magazines)#call diaply funcntion
        
        elif option == 2:
            print('Choose Items')
            print('1. Book')
            print('2. Magazine')
            print('3. Returning to main menu')
            choice = int(input('Enter option (1-3):'))
            if choice == 1:
                d = books
                name = input('\nEnter the title of the book to search:')
                if u.search(name, d) is True:
                    answer = input("\nWould you like to add this item to your cart(y/n)?")
                    if answer == 'y':
                        print("Item:",name,"added to cart\n")
                        k = dict(books)
                        u.add_item(cart, d, k)#adds item 
                        u.display_cart(cart)
                        
                        
                elif u.search(name, d) is False:
                        print(name, 'not found')
   

            if choice == 2:
                d = magazines
                name = input('Enter the title of the magazine to search:')
                if u.search(name, d) is True:
                    answer = input('Would you like to add this item to your cart(y/n)?')
                    if answer == 'y':
                        print("Item:",name,"added to cart")
                elif u.search(name, d) is False:
                    print(name,'not found')
                    
            if choice == 3:
                print("returning to main menu")
                continue

        elif option == 3:
            remove_item(name, cart, d) #removes item

        elif option == 4:
            u.display_cart(cart)#displays cart items and tells return date 
            print('Please return the items by the following due dates:')
            u.return_date()

        elif option == 5:
            write_to_file(books, magazines)
                
                    

            
                
            
                    
            

            #your code here
    
if __name__== '__main__':
    main()
