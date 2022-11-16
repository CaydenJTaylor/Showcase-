#-------------------------------------------------------------------------------
# HA1
# Student Name: Cayden Taylor
# Submission Date: 2/26/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Lecture, notes, textbook, teacher
#-------------------------------------------------------------------------------
# Notes to grader: meets all requirements
#-------------------------------------------------------------------------------

menu=('1.Order Burger\n2.Fries\n3.Drinks\n4.Chedckout\n5.Quit')
burger_menu = ('Burger Menu\n1.Cheese-$5.99\n2.Veggie-$6.99\n3.Meat-$7.49')
fries_menu = ('Fires menu\n1.Regular fries-$1.99\n2.Large fries-$2.99')
drink_menu = ('Drinks menu\n1.Soda-$1.50\n2.Water bottle-$1.00')
choice = [1, 2, 3, 4, 5]
total = 0


print('***********Welcome to Mason Burger***********')
while choice:
    print(menu)
    choice = int(input('\nEnter your option[1-5]: '))

    if choice == 1:
        print(burger_menu)
        burger_choice = int(input('\nEnter your burger selection (1-3): '))

        if burger_choice == 1:
            print('One Cheese burger added to your cart.')
            total += 5.99

        elif burger_choice == 2:
            print('One Veggie burger added to your cart.')
            total += 6.99

        elif burger_choice == 3:
            print('One Meat burger added to your cart.')
            total += 7.49

        else:
            print('invalid option. Returning to Main menu.')

            


    elif choice == 2:
        print(fries_menu)
        fries_choice = int(input('\nEnter your fries selection (1-2): '))

        if fries_choice == 1:
                print('One regular fries added to your cart.')
                total += 1.99

        elif fries_choice == 2:
                print('One large fires added to your cart.')
                total += 2.99

        else:
            print('invalid option. Returning to Main menu.')


    elif choice == 3:
        print(drink_menu)
        drink_choice = int(input('\nEnter your drink selection (1-2): '))

        if drink_choice == 1:
                print('One Soda added to you cart.')
                total += 1.50

        elif drink_choice == 2:
                print('One water bottle added to your cart.')
                total += 1.00

        else:
            print('invalid option. Returning to Main menu.')



    elif choice == 4:
        total_tax = total*0.043
        after_tax = total+total_tax
        print('\nChecking out...')
        print('Your total before tax:',total)
        print('Toatl tax(4.3%):',total_tax)
        print('Your total after tax:',after_tax)
        print('***********Thanks***********')

    elif choice == 5:
        print('Exiting the program')
        break


    else:
        print('invalid option. Returning to Main menu.')







        
