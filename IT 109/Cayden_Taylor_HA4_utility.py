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
# Any notes to grader: fully implemented
#-------------------------------------------------------------------------------
# Code starts below this line
#----------------------------------------------------------------------------

def build_dict(items):
   ''' Returns items_dict from items list. '''
   items_dict = {} #initialization

   for element in items:
      item_element = list(element.split(',')) #seperates the elements 
      items_dict[item_element[0]]=[item_element[1],item_element[2],item_element[3]]
      


   return items_dict

def checkout(cart):
    ''' Returns total price from cart dictionary'''
    print('Thanks for shopping')
    print('You purchased the following items:')
    print('Title-Author-Year-Price')

    total = 0
    
    for k,v in cart.items():#displays cart formatted
       print(k,'-','-'.join(v))
       total += float(v[2]) #convert to float so you can calculate it 

    print('The total amount is:$',total)
    return total
       


def display_all_items(items_dict):
   ''' Display a dictionary key and value'''
   print('\nTitle-Author-Year-Price')
   for k,v in items_dict.items(): #Displays all items formatted
      print(k,'-','-'.join(v))
   
   


def add_books_to_cart(title, cart, items_dict):
   '''Add an item to cart if title exists. Returns True if added
   otherwise returns False'''
   
   if title in items_dict.keys(): 
      print(title,'added to cart')
      cart.update({title:items_dict[title]})
      return True 
      
      
   else:
      print(title,'not found. Returning to main menu...')
      return False

   return cart

   

   
