#-------------------------------------------------------------------------------
# LA5.py
# Name: Cayden Taylor
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: textbook, professor, lab 4, lecture videos
#-------------------------------------------------------------------------------
# Any notes to grader: fully implemented
#-------------------------------------------------------------------------------
# Code: Code starts here


#initializing 
answer = 'y'
names_list = []
cgpa_list = []
total = 0


while answer == 'y':#while loop
   
    names,cgpa = input('Enter first & last name and gpa(seperate by comma):').split(",")
    
    cgpa = [float(x) for x in cgpa.split()]#converts input to a float
    names = [str(x) for x in names.split(",")]

    names_list.append(*names)#adds names/gpa to respective list
    cgpa_list.append(*cgpa)

    answer = input('Do you want to continue(y/n)?')


print(names_list)
print(cgpa_list)

for x in range(0, len(cgpa_list)):#for loop to find total of cgpa and average 
    total = total + cgpa_list[x]

average = total/len(cgpa_list)


max_value = max(cgpa_list)#finding out what is the index value
max_index = cgpa_list.index(max_value)

print("Student name:",names_list[max_index],"has the highest cgpa of",max(cgpa_list))
print("The average cgpa of the class is:",average)
















#-------------------------------------------------------------------------------
