#-------------------------------------------------------------------------------
# Student Name: Cayden Taylor
# Assignment: Final Project
# Python version: 3.9
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Textbook, Python Documentation, previous Hw's and labs
#-------------------------------------------------------------------------------
# Notes: had difficulties with add item and write function
#-------------------------------------------------------------------------------

from datetime import datetime, timedelta

def display_all_items(books, magazines):
    ''' display all items in the library
    Input: books, magazines dict
    Return: None
    '''
    print('Available books\n')
    for k,v in books.items():
        print(k,'-','-'.join(v))#formats line items

    print('Available magazines\n')

    for k,v in magazines.items():
        print(k,'-','-'.join(v))

    #your code here
    

def display_a_book_item(item_id, books):
    ''' display a book item 
    Input: item id, books dict
    Return: None
    '''
    for k,v in books.items():
        print(k,'-','-'.join(v))#formats line items
    #your code here


def display_a_magazine_item(item_id, magazines):
    '''display a magazine item
    Input: item id, magazines dict
    Return: None
    '''
    for k,v in magazines.items():
        print(k,'-','-'.join(v))#formats line items 
    #your code here


def search(name, d):
    '''
    search an item by title/name from a dict d
    Input: name of the item, dictionary to search from 
    Returns item id if found, otherwise returns False
    '''
    #your code here
    item_key =""
    item_value = ""
    for keys,values in d.items():#search function and lists related info 
        for value in values:
            if value == name:
                item_key = keys
                item_value = values
            break
        if item_key and item_value:
            print('Item ID:'+item_key)
            print('Title: ' + item_value[0])
            print('ISBN No. ' + item_value[2])
            print('Author: '+ item_value[3])
            print('No. of copies: '+ item_value[4])
            print('Stack '+ item_value[1])

            return True
        else:
            return False
        
    
   
    
    #check if the name exists in the dictionary d
    #return the key if does, otherwise return False
    
def add_item(cart, d, k):
    '''
    add an item by id k to cart if no of copies available is > 1
    otherwise prints an Item not found
    Input: cart, d (books/magazines), item id k
    Returns none
    '''
    print (k)
    print (d)
    if k in d.keys():# adds items to cart
        cart.update({k:d[k]})
    
    

    
    
    #your code here    
        
        
def remove_item(name, cart, d):
    '''
    remove an item by name from cart if found
    otherwise returns False
    Input: name cart, d (books/magazines)
    Returns True if item removed otherwise returns False
    '''
    valid = False
    for k in d.keys():
        cart.del[k]
        return True #removes items from cart
        
    #your code here
         
                
def display_cart(cart):
    '''
    Display current cart
    Returns none
    '''
    print('*************** Your Cart***************')
    for k,v in cart.items():
        print(k,'-','-'.join(v))
    
  
   
        
    #your code here

def return_date():
    current_date = datetime.now() #get the current date
    diff = timedelta(days=14) # count the difference
    due_date = current_date + diff # due date
    print(due_date.strftime('%m-%d-%Y')) #print the date
    
