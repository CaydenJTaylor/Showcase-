#-------------------------------------------------------------------------------
# LA8.py
# Name: Cayden Taylor 
# Python Version:  3.9.1
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
#Basic iterator for list of US presidents 
class Presidents:
    def __init__(self, presList):
        self.presList = presList
        self.index = -1


    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.presList) -1:
            raise StopIteration
        self.index += 1
        return self.presList[self.index]
    
    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.presList[self.index]

    def first(self):
        if len(self.presList) == 0:
            raise StopIteration
        self.index = -1
        return self.presList[0]


    def last(self):
        if len(self.presList) == 0:
            raise StopIteration
        self.index = len(self.presList)
        return self.presList[len(self.presList)-1]


emptyList = []
emptyIterator = iter(Presidents(emptyList))

try:
    print('First name in the list is {}'.format(emptyIterator.first()))
except StopIteration:
    print('Empty List')
    # if StopIteration is raised, break from loop

try:
    print('Last name in the list is {}'.format(emptyIterator.last()))
except StopIteration:
    print('Empty List')
    # if StopIteration is raised, break from loop

names = ['Wilson', 'Harding', 'Coolidge', 'Hoover', 'Roosevelt', 'Truman', 'Eisenhower']
prez = iter(Presidents(names))

# infinite loop
while True:
    try:
        # get the next item
        # do something with element'
        print(prez.__next__(), end= ',')
    except StopIteration:
        print('\nEnd of list reached')
        # if StopIteration is raised, break from loop
        break

try:
    print('First name in the list is {}'.format(prez.first()))
except StopIteration:
    print('Empty List')
    # if StopIteration is raised, break from loop

try:
    print('Last name in the list is {}'.format(prez.last()))
except StopIteration:
    print('Empty List')
    # if StopIteration is raised, break from loop

# Reverse Order
while True:
    try:
        print(prez.prev(), end= ',')
        # get the next item
        # do something with element
    except StopIteration:
        print('\nEnd of reverse list reached')
        # if StopIteration is raised, break from loop
        break


