#-------------------------------------------------------------------------------
# HA2
# Student Name: Cayden Taylor
# Submission Date: 03/14/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Textbook, Homework 1, Lab 4, lectures, teacher 
#-------------------------------------------------------------------------------
# Notes to grader: Meets all requirements
#-------------------------------------------------------------------------------
#master apps list - should not be modified
apps = ['Weather channel:1.99', 'Bubble Shooter:0.99', \
           'Gallery Pro:1.09', 'Scanner Pro:2.99', \
        'Voice Recorder:3.99', 'Peak Finder:4.99' ]



 

#write your while loop, print menu option
#perform display, add, delete, checkout and exit

#Main menu
main_menu = ('\n1:Display apps\n2:Add apps\n3:Delete an app from cart\n4:Checkout\n5:Exit')



total = 0 #initalizing the total
cart = [] #append purchased items 


choice = [1, 2, 3, 4, 5]#initalizing the choices



print('**********Welcome to mini app store**********')

while choice:
        print('\nAvailable options:')
        print(main_menu)
        choice = int(input('\n\nEnter your choice:'))

        if choice == 1:#listing the apps 
                print('\n****** List of apps******')
                print('\nName--Price')
                print('--------------------')
                for x in apps:
                        print(x)

        if choice == 2:#adding apps to cart
                add_item = input('Enter app name to add to cart:')
                if add_item.lower() == 'weather channel':
                        total += 1.99
                        cart.append(apps[0])
                        print('************ Your Cart************')
                        print('\nName--Price')
                        print(*cart, sep = "\n")
                        print('*********************')
                elif add_item.lower() == 'bubble shooter':
                        total += 0.99
                        cart.append(apps[1])
                        print('************ Your Cart************')
                        print('\nName--Price')
                        print(*cart, sep = "\n")
                        print('*********************')
                elif add_item.lower() == 'gallery pro':
                        total += 1.09
                        cart.append(apps[2])
                        print('************ Your Cart************')
                        print('\nName--Price')
                        print(*cart, sep = "\n")
                        print('*********************')
                elif add_item.lower() == 'scanner pro':
                        total += 2.99
                        cart.append(apps[3])
                        print('************ Your Cart************')
                        print('\nName--Price')
                        print(*cart, sep = "\n")
                        print('*********************')
                elif add_item.lower() == 'voice recorder':
                        total += 3.99
                        cart.append(apps[4])
                        print('************ Your Cart************')
                        print('\nName--Price')
                        print(*cart, sep = "\n")
                        print('*********************')
                elif add_item.lower() == 'peak finder':
                        total += 4.99
                        cart.append(apps[5])
                        print('************ Your Cart************')
                        print('\nName--Price')
                        print(*cart, sep = "\n")
                        print('*********************')
                        
                

        if choice == 3:#removing apps from cart
                remove_item = input('Enter app name to delete from cart:')
                if remove_item.lower() == 'weather channel':
                        total -= 1.99
                        cart.remove(apps[0])
                        print('Weather Channel deleted from cart')
                        print('\n************ Your Cart************')
                        print('\nName--Price')
                        print(*cart, sep = "\n")
                        print('*********************')
                elif remove_item.lower() == 'bubble shooter':
                        total -= 0.99
                        cart.remove(apps[1])
                        print('Bubble Shooter deleted from cart')
                        print('\n************ Your Cart************')
                        print('\nName--Price')
                        print(*cart, sep = "\n")
                        print('*********************')
                elif remove_item.lower() == 'gallery pro':
                        total -= 1.09
                        cart.remove(apps[2])
                        print('Gallery Pro deleted from cart')
                        print('\n************ Your Cart************')
                        print('\nName--Price')
                        print(*cart, sep = "\n")
                        print('*********************')
                elif remove_item.lower() == 'scanner pro':
                        total -= 2.99
                        cart.remove(apps[3])
                        print('Scanner Pro deleted from cart')
                        print('\n************ Your Cart************')
                        print('\nName--Price')
                        print(*cart, sep = "\n")
                        print('*********************')
                elif remove_item.lower() == 'voice recorder':
                        total -= 3.99
                        cart.remove(apps[4])
                        print('Voice Recorder deleted from cart')
                        print('\n************ Your Cart************')
                        print('\nName--Price')
                        print(*cart, sep = "\n")
                        print('*********************')
                elif remove_item.lower() == 'peak finder':
                        total -= 4.99
                        cart.remove(apps[5])
                        print('Peak finder deleted from cart')
                        print('\n************ Your Cart************')
                        print('\nName--Price')
                        print(*cart, sep = "\n")
                        print('*********************')

        if choice == 4:#checkout
                formatted_total = "{:.2f}".format(total)
                print('\nYour cart:')
                print(*cart, sep = "\n")
                print('Your toal:', formatted_total)

        if choice == 5:#break the loop
                print('*********** Thanks for shopping with us***********')
                break

        

input('press enter to close')#This is so the module won't automatically close



                
                        
                
                        
                        
                        
                
                



                
                
                
        



