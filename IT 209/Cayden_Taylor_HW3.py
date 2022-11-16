#-------------------------------------------------------------------------------
# HA3
# Student Name: Cayden Taylor
# Python version: 3.9.1
# Submission Date: 7/9/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: HW 2 Lab 6 Lab 7 Lab 8 sample codes
#-------------------------------------------------------------------------------
# Notes to grader: 2nd 2 day late pass, had trouble with try excpet block
#-------------------------------------------------------------------------------
# Source code below
#-------------------------------------------------------------------------------

#define InvalidBook Exception class
class InvalidBook(Exception):
    try:
        Book_List()
    except:
        print("invlaid Book")
    #your code here

#defing InvalidOption Exception class
class InvalidOption(Exception):
    try:
        choice == 1 or 2
    except:
        print("Choice not vlaid")
        


#define a BookList class
class Book_List(list): #list class 
    def search(self, name):
        for book in self:
            if book.get_name() == name:
                return book
            return None


#define a Book class
class Book: #defining super class for book
    def __init__(self, genre, name, author, stackno):
        self.genre = genre
        self.name = name
        self.author = author
        self.stackno = stackno

        def get_genre(self):
            return self.genre

        def get_name(self):
            return self.name

        def get_author(self):
            return self.author

        def get_stack_no(self):
            return self.stackno


#define a Novel, Scifi class
class Novel(Book): #creating subclass for Novel section
    def __init__(self, genre, name, author, stackno, sub_genre):
        super().__init__(genre, name, author, stackno)
        self.subgenre = sub_genre
    def get_sub_genre(self):
        return self.sub_genre
    def __str__(self):
        return "Title: " + self.get_name() + "\nGenre: " + self.get_genre() + "\nSub Genre: " + self.get_sub_genre() + "\nAuthor: " + self.get_author() + "\nStack: " + self.get_stackno()



class Scifi(Book):#Creating subclass for scifi section
    def __init__(self, genre, name, author, stackno, date, location):
        super().__init__(genre, name, author, stackno)
        self.date = date
        self.location = location
    def get_date(self):
        return self.date
    def get_location(self):
        return self.location
        return self.sub_genre
    def __str__(self):
        return "Title: " + self.get_name() + "\nGenre: " + self.get_genre() + "\nAuthor: " + self.get_author() + "\nStack: " + self.get_stackno() + "\nMovie Date: " + self.get_date() + " Location : " + self.get_loaction()
                      

#Note: Scifi class you need to check if there is no movie night you can set
#date and location to 'No information'. See sample I/O


#define a main function
def main(): #creating main and opening file 
    book_location = Book_List()
    file = open("library.txt", "r")
    for line in file:
        sections = line.strip().split(",")
        if sections[0] == "Novel":
            book_location.append(Novel(sections[0], sections[1], sections[2], sections[3], sections[4])) #breaking the file down into the parts needed 
        elif sections[0] == "scifi":
            if len(sections) == 6:
                book_location.append(Scifi(sections[0], sections[1], sections[2], sections[3], sections[4], sections[5]))
            else:
                book_location.append(Scifi(sections[0], sections[1], sections[2], sections[3], sections[4], sections[5]))

    file.close()
    print("-------------------------------")
    print("Welcome to libary database main menu")
    print("---------------------------------")

    while True:
        print("\n1. Search")
        print("2. Exit")
        choice = int(input("Emter your option (1/2): "))
        if choice == 1:
            search_for_book = input("Enter title of the book: " ).strip()
            book_here = book_location.search(search_for_book)
            if not(book_here):
                raise InvalidBook()#Raise errro when book is not found

        elif choice == 2:
            print("leaving the database")
            break

        if choice != 1 or 2:
            raise InvalidOption() #raise erroe when option is not 1 or 2

main()
#read the file information
#create object per genre as in HA2

#once object creation is done
#setup a user menu using try-except block
#if book not found raise and InvalidBook exception
#if choice not 1 or 2, then raise InvalidOption
