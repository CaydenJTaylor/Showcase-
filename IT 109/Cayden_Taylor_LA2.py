#-------------------------------------------------------------------------------
# LA2.py
# Student Name: Cayden Taylor 
# Version: 3.9.1
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that 
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: module resources, instructor, textbook
#-------------------------------------------------------------------------------
# Any notes to grader:fully implemented
#-------------------------------------------------------------------------------
# Code starts below this line 
#----------------------------------------------------------------------------

choice = 0
total_sum = choice


while choice%2 != 1:
    choice = int(input("Enter an even number to continue. Enter an odd to close the application: "))
    if (choice%2) == 0:
        print('Adding even number',choice)
        total_sum += choice
        

    else:
        print(choice,'is an odd number. Exiting the program')



print('\n Total sum of even numbers is',total_sum)


#this is so the application will not close immediately and you can view the total sum
input('\n Press enter to close')
        
        
