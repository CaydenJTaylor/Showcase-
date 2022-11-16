#-------------------------------------------------------------------------------
# LA1.py
# Name: Cayden Taylor
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Textbook and course instructor
#-------------------------------------------------------------------------------
# Comments to grader:fully implemented 
#-------------------------------------------------------------------------------
# Code: Code starts here

height = float(input('Enter height in meters:'))

weight = float(input('Enter weight in kilograms:'))

BMI = weight/height**2


print('\nBody Type\tBMI Index')
print('Underweight\t<=18.5')
print('Normal Weight\t18.5-24.9')
print('Overweight\t25.0-29.9')
print('Obese\t\t>=30.0')
print('Your BMI is:',BMI)

input('\nPress Enter to close')







#-------------------------------------------------------------------------------

    

