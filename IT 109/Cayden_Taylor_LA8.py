#-------------------------------------------------------------------------------
# LA8.py
# Name: Cayden Taylor
# Python Version: 3.9.1
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Textbook, Lab 7, lecture videos, supplemental source codes
#-------------------------------------------------------------------------------
# Comments to grader: fully implemented 
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------

def read_file():
        '''reads input file
        returns a list of information'''
        file = open("studentProfile.txt", "r")
        raw_students = list(file.readlines())#reads each line of .txt file

        students = []
        for element in raw_students:#for loop to remove '\n' in list
                students.append(element.strip())

        return students


def create_dict(students):
        '''creates a student dict
        key = ID and value = [name, email, major]
        and returns student dict'''

       

        students_dict={}
        for element in students:
                student_element = list(element.split('|'))#prints each student and splits by "|"
                students_dict[student_element[0]]=[student_element[1],student_element[2],student_element[3]]
                #adds each value portion to the key value portion
                

        return students_dict
        

def display(students_dict):
    '''display student dictionary'''
    print('******Current Student Profile******')
    print('\nID - Full Name-Email Address-Major')
    for k,v in students_dict.items():
            print(k,'-','-'.join(v))#prints the key and values formatted 



def search(ID, students_dict):
        '''seach student dict by ID
        returns value if key found
        otherwise returns False'''

        for k,v in students_dict.items():
                if k == ID:
                        return v

        else:
                return False


        
 
def main():
        students = read_file() #read in information and returns list
        students_dict = create_dict(students) #create dict
        menu = '\n\n1. Search\n2. Display\n3. Exit'
        choice = '0'
        while choice!= '3':
                print(menu)
                choice = input('\nEnter your choice (1-3): ')
                                       
                if choice == '1':
                        ID = input('Enter student ID: ')
                        info = search(ID, students_dict)
                        if info == 0:
                            print('{} not found!'.format(ID))
                        else:
                            for i in info:
                                print(i, end = '-')
                
                elif choice == '2':
                        display(students_dict)
                        
                elif choice == '3':
                        print('Exiting application.')
                        
                else:
                        print('Invalid option. Return to main menu.')
                
        
        
main()

    






