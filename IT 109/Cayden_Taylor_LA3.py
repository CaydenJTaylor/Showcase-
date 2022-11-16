#-------------------------------------------------------------------------------
# LA3.py
# Student Name: Cayden Taylor 
# Version: 
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that 
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: lecture, textbook, module resources, teacher 
#-------------------------------------------------------------------------------
# Any notes to grader: For example: fully implemented
#-------------------------------------------------------------------------------
# Code starts below this line 
#-------------------------------------------------------------------------------

count = int(input('Enter the total number of individuals: '))
#initialization
total_num = 0
#etotal is short for eligible
etotal = 0
i=0
print('\nPlease enter the answer to following questions to determine eligibility for current phase vaccination.') 


while i < count:
    print('\n**person',i+1,'**')
    i +=1
    
    Q1 = input('\nQ1: Are you a Fairfax healh district resident ages 65+?: ')
    Q2 = input('\nQ2: Are you a health care/child care worker, or a K-12 teacher or staff member who lives or works in the Fairfax Health District? (Y/N): ')
    Q3 = input('\nQ3: Are you a Fairfax Health District resident ages 16-64 with a high-risk medical condition or disability that increases your risk of severe illness from COVID-19? (Y/N): ')


    if Q1 == 'N' and Q2 == 'N' and Q3 == 'N':
        print('\n***Person',i, 'is not eligible***')
        
    else:
        print('\n***Person',i, 'is eligible***')
        etotal = etotal+1
        


total_num = i

eligible_num = (etotal/total_num)*100

print('\nOverall', eligible_num,'% of individuals are eligible to receive the COVID vaccine for this phase')

#so python module does not close before looking at results
input('\nPress Enter to close')
              







