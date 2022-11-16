#-------------------------------------------------------------------------------
# ILA6.py
# Name: Cayden Taylor
# Python Version: 3.9.1
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Lab session
#-------------------------------------------------------------------------------
# Comments to grader: Fully Implemented
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------

from queue import LifoQueue, Queue

def readFile():
    f = open('LIFO.txt')
    lines = f.readlines()
    f.close()
    return lines[0].split()

#define your class here:

class MyLIFO(LifoQueue):

    def push(self, top):
        if top not in ['-' , '*' , '(' , '^' , '@', '$', '!', '&']:
            self.put(top, block = False)
            return True
        else:
            return False
        

    def pop(self):
        return self.get()
    

    def get_size(self):
        return self.qsize()
        

    def __str__(self):
        return ' '.join(self.queue)
        


class MyFIFO(Queue):

    def push(self, top):
          if top not in ['-' , '*' , '(' , '^' , '@', '$', '!', '&']:
            self.put(top, block = False)
            return True
          else:
              return False
      

    def pop(self):
        return self.get()
        

    def get_size(self):
        return self.qsize()
        

    def __str__(self):
        return ' '.join(self.queue)
    



def main():
    print(' Last in First Out')
    m = MyLIFO()
    lines = readFile()
    for word in lines:
        if m.push(word):
            print (word, " pushed to stack, current size: ", m.get_size())
        else:
            print (m.pop(), " popped from stack, current size: ", m.get_size())
    print()

    print(' First in First Out')
    n = MyFIFO()
    lines = readFile()
    for word in lines:
        if n.push(word):
            print (word, " pushed to stack, current size: ", n.get_size())
        else:
            print (n.pop(), " popped from stack, current size: ", n.get_size())
    print()

    print("Final stack size of LIFO: ", m.get_size())
    print(m)
    print ("Final stack size of FIFO: ", n.get_size())
    print(n)
        
    
main()






    
