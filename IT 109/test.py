def read_file():
    file = open("library.txt", "r")
    raw_list = list(file.readlines())#reads each line of .txt file

    file_list = []
    for element in raw_list:#for loop to remove '\n' in list
        file_list.append(element.strip())

    books = {}
    magazines = {}

    for item in file_list:
        ID,item_type,title,info,volume_ISBN,author_issue,num_copies = item.split(',')
        if item_type == 'book':
            books[ID]= title,info,volume_ISBN,author_issue,num_copies

        if item_type == 'magazine':
            magazines[ID]= title,info,volume_ISBN,author_issue,num_copies





    for k,v in books.items():
        print(k,'-','-'.join(v))

    for k,v in magazines.items():
        print(k,'-','-'.join(v))

    

read_file()

