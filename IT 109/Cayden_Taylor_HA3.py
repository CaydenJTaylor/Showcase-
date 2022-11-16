#-------------------------------------------------------------------------------
# HA3.py
# Student Name: Taylor, Cayden
# Version: Python 3.9.1
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Lab 4, Lecture videos, professor lectures, textbook, homework 2
#-------------------------------------------------------------------------------
# Any notes to grader: For example: Easy
#-------------------------------------------------------------------------------
# Code starts below this line
#----------------------------------------------------------------------------


def build_lists(items):
    
   title_list = []
   year_list = []
   writer_list = []
   price_list = []

   for item in items:#for loop to append values
      title,writer,year,price = item.split(",")
      title_list.append(title.strip())
      year_list.append(int(year.strip()))
      writer_list.append(writer.strip())
      price_list.append(float(price.strip()))
      
                     
      

   #find corresponding values and append to the four lists

   return title_list, year_list, writer_list, price_list


def checkout(cart, title_list, price_list):#checkout function
   print('Thanks for shopping')
   print('You purchased the following book(s):',cart)
   
   price = 0
   for item in cart:
      price += price_list[title_list.index(item)]
   print('The total amount is: $',price)
        



def main():
    
        items = ['Animal Farm, George Orwell, 1945, 19.99', 'The Great Gatsby, Scott Fitzgerald, 1934, 22.99',
                 'Jane Eyre, Charlotte Bronte, 1847, 27.99', 'Anna Karenina, Leo Tolstoy, 1877, 21.99 ',
                 'Sanctuary, William Faulkner, 1931, 30.99', 'Adventures of Huckleberry Finn, Mark Twain, 1884, 28.99']

        title_list, year_list, writer_list, price_list = build_lists(items)

        cart = []
        
        print('Welcome to shopping at Amazing!')
        print('We sell books from American Novelists\nPlease choose from the following options to get information on available books')

        while True:
            print('Press 1 to get title of available books as a list\n')
            print('Press 2 to get year of publication of available books as a list\n')
            print('Press 3 to get writer of available books as a list\n')
            print('Press 4 to get price range of available books\n')


            choice = input('Please input an option or input ''checkout'' to quit:')

            if choice == '1':
               print('Title list:',title_list)
               info_price = input('more info(m) or add books to cart?(a)')
               if info_price == 'm':
                  print(items)
               if info_price == 'a':
                  buying_number = int(input('how many books do you want to add?'))
                  for i in range(buying_number):#loop for number of books being bought
                     print(title_list)
                     book = input('enter the title of the book from list:').strip()
                     cart.append(book)
                  checkout(cart,title_list,price_list)#calls checkout function 
                  break

                     
            elif choice == '2':
               print('Book Year List:',year_list)
               info_price = input('more info(m) or add books to cart?(a)')
               if info_price == 'm':
                  print(items)
               if info_price == 'a':
                  buying_number = int(input('how many books do you want to add?'))
                  for i in range(buying_number):
                     print(year_list)
                     book = input('enter the year of the book from list:').strip()
                     cart.append(title_list[year_list.index(int(book))])
                  checkout(cart,title_list,price_list)
                  break

                     
            elif choice == '3':
               print('Writers List:',writer_list)
               info_price = input('more info(m) or add books to cart?(a)')
               if info_price == 'm':
                  print(items)
               if info_price == 'a':
                  buying_number = int(input('how many books do you want to add?'))
                  for i in range(buying_number):
                     print(writer_list)
                     book = input('enter the writer of the book from list:').strip()
                     cart.append(title_list[writer_list.index(book)])
                  checkout(cart,title_list,price_list)
                  break
                  
            
            elif choice == '4':
               print('Min Price:',min(price_list),'Max Price:', max(price_list))#min max range
               checkout(cart,title_list,price_list)
               break
               
               
                                                                     
            elif choice == 'checkout':
               checkout(cart,title_list,price_list)
               break

           
            # add your code here

main()

