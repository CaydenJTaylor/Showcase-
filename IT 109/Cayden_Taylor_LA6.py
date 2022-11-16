#-------------------------------------------------------------------------------
# LA6.py
# Student Name: Cayden Taylor
# Version: 3.9.1
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that 
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Textbook, proffesor lecture, video lectures, Lab 5
#-------------------------------------------------------------------------------
# Any notes to grader: fully implemented
#-------------------------------------------------------------------------------
# Code starts below this line 
#----------------------------------------------------------------------------
def main():
    answer = 'y'
    while answer == 'y':
        extract_letters_and_digits()
        answer = input('\n\nDo you want to continue (y/n):')
        if answer == 'n':
            break

        
def extract_letters_and_digits():
    """asks for input from user,extracts letters and digits and
    places them in there corresonding list and prints it"""
    
    user_input = input("Enter a word to start with: ")
    
    numbers = ''.join(filter(lambda i: i.isdigit(),user_input))
    letters = ''.join(filter(lambda i: i.isalpha(),user_input))

    number_list = list(numbers)
    letter_list = list(letters)

    print("\nThe letters in the string are:")

    for x in letter_list:
        print(x, end = ",")

    print("\n\nThe digits in the string are:")

    for x in number_list:
        print(x, end = ",")

main()



    

    

    

   

    


