#-------------------------------------------------------------------------------
# Cayden_Taylor_LA4.py
# Student Name: Cayden Taylor
# Assignment: LA4
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: lecture, texbook, and powerpoints 
#-------------------------------------------------------------------------------
# Note to grader: fully completed and meets all requirements 
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------
# Source Code: Write your code below


books=['\nGirl With No Name:$14.88', 'Despicable Me:$12.99', \
           'Journey To The Moon:$10.99', 'The Calculating Stars:$20.0']
checkout_list = []
print('*********** Welcome to mini book store  ***********') 
total_count = int(input('How many books to checkout? '))
i=0
price=0


while i in range(total_count):
    print('\n*******List of Books*******')
    i = i+1
    for x in books:
        print(x)
        

    
    cart_item = input('\nEnter book title to add to your cart: ')
    

    if cart_item.lower() == 'girl with no name':
        print(books[0],'added to your cart')
        checkout_list.append(books[0])
        price += 14.88
 
    elif cart_item.lower() == 'despicable me':
        print(books[1],'added to your cart')
        checkout_list.append(books[1])
        price += 12.99

    elif cart_item.lower() == 'journey to the moon':
        print(books[2],'added to your cart')
        checkout_list.append(books[2])
        price += 10.99

    elif cart_item.lower() == 'the calculating stars':
        print(books[3],'added to your cart')
        checkout_list.append(books[3])
        price += 20.0

    else:
        print('invalid choice')

print('\nYour Cart:')
print(*checkout_list, sep = "\n")
print('---------------------------')
print('Your toatl $',price)

#so python module does not close before reading price
input('\npress enter to close')



