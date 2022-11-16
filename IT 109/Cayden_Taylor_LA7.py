#-------------------------------------------------------------------------------
# LA7.py
# Name: Cayden Taylor
# Python Version: 3.9.1
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Lecture videos, lab 5, textbook
#-------------------------------------------------------------------------------
# Any notes to grader: fully implemented
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------

#define max_spending function here
def max_spending(month_spend_dict):
        keys = []
        values = []

        for k in month_spend_dict.keys():#for loop to put keys and values in seperate lsit
                keys.append(k)
                

        for v in month_spend_dict.values():
                values.append(v)
                

        max_value = max(values)
        max_index = values.index(max_value)#finding index of highest number 

        print('Max spending of $',max_value,'in month of',keys[max_index])


#define monthly_spending function here
def monthly_spending(spend_dict):
        
        #adding all fees for each month together
        jan_total = sum(spend_dict['Jan'])

        feb_total = sum(spend_dict['Feb'])

        mar_total = sum(spend_dict['Mar'])

        month_spend_dict = dict(January=jan_total, Febuary=feb_total, March=mar_total)
        

        return month_spend_dict
        

def main():
        #grocery, automobile, utilities
        spend_dict = {'Jan': [90,60, 50], 'Feb': [56, 30, 65],\
                   'Mar': [100, 85, 78]}

        month_spend_dict = monthly_spending(spend_dict)

        
        #call monthly_spending function
        monthly_spending(spend_dict)

        #call max_spending function
        max_spending(month_spend_dict)
        
        #print the outcome from max_spending()
        


        
main()

