#  ________  ________  ________        ___  _______   ________ _________        ________
# |\   __  \|\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\     |\_____  \
# \ \  \|\  \ \  \|\  \ \  \|\  \     \ \  \ \   __/|\ \  \___\|___ \  \_|     \|____|\ /_
#  \ \   ____\ \   _  _\ \  \\\  \  __ \ \  \ \  \_|/_\ \  \       \ \  \            \|\  \
#   \ \  \___|\ \  \\  \\ \  \\\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \          __\_\  \
#    \ \__\    \ \__\\ _\\ \_______\ \________\ \_______\ \_______\  \ \__\        |\_______\
#     \|__|     \|__|\|__|\|_______|\|________|\|_______|\|_______|   \|__|        \|_______|

# Author: Nate Harris
# CIST2110-001-Project-3 Library Management System (LMS)
# Project 3 will implement a library management system (LMS) that will allow users to manage books, users, and a library to manage collection of books and users.
# The LMS will be menu driven and will allow users to add, delete, and update books and users.
# Users will also be able to borrow and return books.
# The LMS will also allow users to search for books and users.

# ENABLE WORD WRAP TO MAKE THINGS EASIER TO READ:
# VIEW (at the top) -> WORD WRAP

# Import statements:

# Project outline and requirements:

# OUTLINE - The LMS will consist of the following classes and methods:

# 1. Create a Book class that has the following attributes (create a __init__ method)):
#    a. ISBN (int)
#    b. Title (string)
#    c. Author (string)
#    d. borrowed (boolean) - this should not be passed in as a parameter, it should be set to False by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES

# Methods:
#    a. __str__ (returns a string representation of the book using the following format: ISBN: <ISBN>, Title: <Title>, Author: <Author>, Borrowed: <Borrowed>)
#    b. checkout - sets borrowed to True and returns a message that the book has been checked out
#    c. checkin - sets borrowed to False and returns a message that the book has been checked in
#    d. isBorrowed - returns True if the book is borrowed and False if the book is not borrowed

class Book:
    """
    Book class
    
    Attributes:
        title (str): title of book
        author (str): author of book
        isbn (int): isbn of book
        borrowed (bool): whether book is borrowed or not
        
        Methods:
            checkout: sets borrowed to True and returns a message that the book has been checked out
            checkin: sets borrowed to False and returns a message that the book has been checked in
            isBorrowed: returns True if the book is borrowed and False if the book is not borrowed
    """
    
    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False

    def __str__(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Borrowed: {self.borrowed}"

    def checkout(self):
        self.borrowed = True
        return f"{self.title} has been checked out"

    def returned(self):
        self.borrowed = False
        return f"{self.title} has been checked in"

    def isBorrowed(self):
        return self.borrowed


# 2. Create a User class that has the following attributes (create a __init__ method)):
#    a. Name (string)
#    c. ID (int)
#    d. borrowedBooks (list of books) - this should not be passed in as a parameter, it should be set to an empty list by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES

# Methods:
#    a. __str__ (returns a string representation of the user using the following format: Name: <Name>, ID: <ID>, Borrowed Books: <Borrowed Books>)
#    b. borrow_book - adds the book to the borrowedBooks list, updates the isBorrowed attribute of the book to True, and returns a message that the book has been checked out (should take a book as a parameter)
#    c. return_book - removes the book from the borrowedBooks list, updates the isBorrowed attribute of the book to False, and returns a message that the book has been checked in (should take a book as a parameter)
    
class User:
    """
    User class
    
    Attributes:
        name (str): name of user
        member_id (int): id of user
        borrowed_books (list): list of books borrowed by user
        
        Methods:
            borrow_book: adds the book to the borrowedBooks list, updates the isBorrowed attribute of the book to True, and returns a message that the book has been checked out
            return_book: removes the book from the borrowedBooks list, updates the isBorrowed attribute of the book to False, and returns a message that the book has been checked in
    """

    def __init__(self, name: str, member_id: int):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Name: {self.name}, ID: {self.member_id}, Borrowed Books: {self.borrowed_books}"

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        book.checkout()
        return f"{book.title} has been checked out"

    def return_book(self, book):
        self.borrowed_books.remove(book)
        book.returned()
        return f"{book.title} has been checked in"

# 3. Create a Library class that has the following attributes (create a __init__ method)):
#    a. books (list of books)
#    b. users (list of users)
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES

# Methods:
#    a. __str__ (returns a string representation of the library using the following format: Books: <Books>, Users: <Users>)
#    b. add_book - adds a book to the books list (should take a book as a parameter)
#    c. add_user - adds a user to the users list (should take a user as a parameter)
#    d. find_book - returns the book with the given ISBN (should take an ISBN as a parameter)
#    e. find_user - returns the user with the given ID (should take an ID as a parameter)
#    f. export_books_to_csv - exports the books list to a csv file (should take a filename as a parameter)
#       The csv file should have the following format: ISBN,Title,Author,Borrowed
#       The csv.DictWriter class is very useful for this: https://docs.python.org/3/library/csv.html#csv.DictWriter
#    g. export_users_to_csv - exports the users list to a csv file (should take a filename as a parameter)
#       This will be similar to the export_books_to_csv method but there is a slight difference with the borrowedBooks attribute if you get stuck this code might help:
#       borrowed_books_titles = [book.title for book in user.borrowed_books]
#       Use that and pythons .join method to create a string of the borrowed books titles

class Library:
    """ 
    Library class
    
    Attributes:
        books (list): list of books in library
        users (list): list of users in library
        
        Methods:
            add_book: adds a book to the books list
            add_user: adds a user to the users list
            find_book: returns the book with the given ISBN
            find_user: returns the user with the given ID
            export_books_to_csv: exports the books list to a csv file
            export_users_to_csv: exports the users list to a csv file
    """

    def __init__(self):
        self.books = []
        self.users = []

    def __str__(self):
        return f"Books: {self.books}, Users: {self.users}"

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book

    def find_user(self, id):
        for user in self.users:
            if user.id == id:
                return user

    def export_books_to_csv(self, filename):
        import csv
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['ISBN', 'Title', 'Author', 'Borrowed']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for book in self.books:
                writer.writerow({'ISBN': book.isbn, 'Title': book.title, 'Author': book.author, 'Borrowed': book.borrowed})

    def export_users_to_csv(self, filename):
        import csv
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'ID', 'Borrowed Books']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for user in self.users:
                borrowed_books_titles = [book.title for book in user.borrowed_books]
                writer.writerow({'Name': user.name, 'ID': user.member_id, 'Borrowed Books': borrowed_books_titles})

# 4. Create a menu that will allow users to:
#    a. Add books
#    b. Add users
#    c. Delete books
#    d. Delete users
#    g. Borrow books
#    h. Return books
#    i. Search books
#    j. Check if book is available
#    k. Search users
#    l. Export books to csv
#    m. Export users to csv
#    z. Exit
                
# 5. Create a main method that will create a library object and use the menu to call the appropriate methods
# RQUIREMENTS:
# 1. You should be doing error checking on all user input (make sure the user enters a valid ISBN, ID, etc.) and handle any errors appropriately (i.e. if the user enters an invalid ISBN, ask them to enter a valid ISBN)
# 2. You should be using try except blocks to handle any errors
# 3. You should be using the classes and methods outlined above with the exact names and parameters
# 4. You should be using the menu to call the appropriate methods
# 5. There is a Project3Tests.py file that will help you test your code. You should be able to run that file and pass all the tests.
#    Remember to run pytest use the following command in the terminal: pytest Project3Tests.py
# 6. The Project3Tests.py file is missing 2 tests. test_user_return and test_library_find_user. You will need to implement those tests and ensure they pass.
# 7. In your main method you should create a library object first to use for the rest of the program. You should not be creating a new library object every time you call a method. (Similar to the Store object in Lab 11)
# 8. In your main method you should be using a while loop to keep the program running until the user chooses to exit.

# IMPORTANT: You will only have 1 submission for this project so make sure you test your code thoroughly before submitting.
# You will be graded on the following:
# 1. Did you follow the project outline and requirements?
# 2. Does your code run without errors?
# 3. Did you use try except blocks to handle errors?
# 4. Did you use the classes and methods outlined above with the exact names and parameters?
# 5. Did you use the menu to call the appropriate methods?
# 6. Did you include docstrings for all classes and methods?
# 7. Did you include type hints for all methods?
# 8. Did your pytests for the test_user_return and test_library_find_user work?


def main():
    library = Library()
    while True:
        try:
            print("a. Add book")
            print("b. Add user")
            print("c. Delete book")
            print("d. Delete user")
            print("g. Borrow book")
            print("h. Return book")
            print("i. Search books")
            print("j. Check if book is available")
            print("k. Search users")
            print("l. Export books to csv")
            print("m. Export users to csv")
            print("z. Exit")
            choice = str(input("Enter choice: "))
            if choice == 'a':
                title = str(input("Enter title: "))
                if title == "":
                    print("Title cannot be empty")
                    title = str(input("Enter title: "))
                author = str(input("Enter author: "))
                if author == "":
                    print("Author cannot be empty")
                    author = str(input("Enter author: "))
                isbn = input("Enter ISBN: ")
                if isbn == "":
                    print("ISBN cannot be empty")
                    isbn = input("Enter ISBN: ")
                book = Book(title, author, isbn)
                library.add_book(book)
            elif choice == 'b':
                name = input("Enter name: ")
                id = input("Enter ID: ")
                user = User(name, id)
                library.add_user(user)
            elif choice == 'c':
                isbn = input("Enter ISBN: ")
                book = library.find_book(isbn)
                library.books.remove(book)
            elif choice == 'd':
                id = input("Enter ID: ")
                user = library.find_user(id)
                library.users.remove(user)
            elif choice == 'g':
                isbn = input("Enter ISBN: ")
                book = library.find_book(isbn)
                id = input("Enter ID: ")
                user = library.find_user(id)
                user.borrow_book(book)
            elif choice == 'h':
                isbn = input("Enter ISBN: ")
                book = library.find_book(isbn)
                id = input("Enter ID: ")
                user = library.find_user(id)
                user.return_book(book)
            elif choice == 'i':
                isbn = input("Enter ISBN: ")
                book = library.find_book(isbn)
                print(book)
            elif choice == 'j':
                isbn = input("Enter ISBN: ")
                book = library.find_book(isbn)
                print(book.isBorrowed())
            elif choice == 'k':
                id = input("Enter ID: ")
                user = library.find_user(id)
                print(user)
            elif choice == 'l':
                filename = input("Enter filename: ")
                library.export_books_to_csv(filename)
            elif choice == 'm':
                filename = input("Enter filename: ")
                library.export_users_to_csv(filename)
            elif choice == 'z':
                print("Exiting the program, goodbye!")
                break
            else:
                print("Invalid option, please choose a, b, c, d, g, h, i, j, k, l, m, or z")
        except ValueError as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
