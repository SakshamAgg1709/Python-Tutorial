#Library Managaement System

class Library:
    def __init__(self , list_book , lname):
        self.list_of_book = list_book
        self.library_name = lname
        self.lendDict = {}

    def display_book(self):
        print(f"We have following books in Our Library : {self.library_name}")
        for items in self.list_of_book:
            print(items)

    def lend_book(self , lender ,book_name):
        if book_name.title() in self.list_of_book:

            if book_name not in self.lendDict.keys():
                self.lendDict.update({book_name:lender})
                print("Lender-Book database updated, You can take the book now. :)")
            else:
                print(f"Book is already being used by {self.lendDict[book_name]}")
        else:
            print("The entered book is not in the Library")

    def add_book(self , book_names):
        book_names2 = book_names.split(",")
        for book in book_names2:
            self.list_of_book.append(book)


    def return_book(self ,lender ,  book_name):
        self.lendDict.pop(lender)
        self.lendDict.pop(book_name)
        self.list_of_book.append(book_name)




if __name__ == '__main__':
    Saksham_Library = Library([ "Gita" ] , "Saksham Library")

    while(True):
        print(f"Welcome to the {Saksham_Library.library_name}. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend Book - You can lend only one book at the time")
        print("3. Add a Book - You can add as many as you want")
        print("4. Return a  Book - You can return only 1 book at a time")
        user_choice = int(input())

        if user_choice == 1:
            Saksham_Library.display_book()

        elif user_choice == 2:
            book = input("Enter the book you want to Lend : ")
            user = input("Enter your name:")
            Saksham_Library.lend_book(user , book)

        elif user_choice == 3:
            book = input("Enter the book you want to add (Separate two or more book with a ',') : ")
            Saksham_Library.add_book(book)
            print("Entered Books are added successfully")


        elif user_choice == 4:
            user = input("Enter your name:")
            book = input("Enter the book you want to return : ")
            Saksham_Library.return_book(user ,book)

        else:
            print("Not a valid option")

        print("Press q for quitting ,c for continue")
        user_choice2 = input()

        if user_choice2  == "q":
            quit()
        elif user_choice2 == "c":
            continue
        else:
            print("Enter correct letter")