#-------------------------------------------------------------------------------
# ILA10.py
# Name: Cayden Taylor
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: video lectures, textbook 
#-------------------------------------------------------------------------------
# Any notes to grader: fully implemented
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------


def summation(sequence):
        """
        Input: sequence: python list 
        Return: summation of the numeric elements: int or float
        """
        total_sum = 0
        for s in sequence:
                try:
                        total_sum += float(s)#completes equation if int or float 
                except:
                        print('Not a number, continue to next element')#if not prints message
        return total_sum	

def reciprocal(n):
        """
        Input: n: int or float
        Returns: reciprocal of n if n is int or float otherwise
        returns error message
        """
        try:
                return 1/float(n)#Tries to return if it is a float or int
        except:
                print(n,':Zero and string not allowed') #if not prints message
        
	
def getList(filename):
        """
        Input: filename: string
        Returns: list: content of the file in list
        if file can be opened otherwise returns False
        """
        f = open(filename)
        temp = f.readline()
        return [t.split('\n')[0] for t in temp.split(',') ] #returns the sequence
        

def main():
        sequence = getList('ILA9.txt')
        if sequence == False:
                print ("File I/O error")
        else:
                print('The sequence is: ', sequence)
                
                print ("**** Calculating Summation  ****")
                print (summation(sequence))

                print (" **** Calculating Reciprocal  ****")
                for s in sequence:
                        print ('{} : {}'.format(s , reciprocal(s)))

	

main()
