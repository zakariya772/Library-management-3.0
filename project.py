class Book:
    borrowed_count = 0
    def __init__(self,title,author):
        self.__title = title
        self.__author = author
        self.__available = True

    def borrow(self):
        if self.__available:
            self.__available = False
            Book.borrowed_count+=1
            print(f"{self.__title} has been borrowed successfully.")
            return True
        print(f"{self.__title} has been borrowed")
        return False

    @classmethod
    def borrowed_books(cls):
        return cls.borrowed_count

    def return_book(self):
        if not self.__available:
            self.__available = True
            print(f"{self.__title} returned successfully.")
            Book.borrowed_count-=1
            return True
        print(f"{self.__title} has already been returned")
        return False

    def new_title(self,new_title):
        print(f"{self.__title} changed successfully.")
        self.__title = new_title

    def new_author(self,new_author):
        print(f"{self.__author} changed successfully.")
        self.__author = new_author
    @property
    def title(self):
        return self.__title
    @property
    def author(self):
        return self.__author

    @property
    def available(self):
        return self.__available

class Member:
    def __init__(self,name,member_id,age,course):
        self.__name = name
        self.__member_id = member_id
        self.__age = age
        self.__course = course
        self.__borrowed_books = []
        self.__favourite_book = None
    def introduce(self):
        print(f"My name is {self.__name}")
    def add_borrowed_books(self,book):
        if book in self.__borrowed_books:
            return False
        self.__borrowed_books.append(book)
        return True

    def remove_borrowed_books(self,book):
        if book not in self.__borrowed_books:
            return False
        self.__borrowed_books.remove(book)
        return True

    def view_borrowed_books(self):
        if len(self.__borrowed_books) == 0:
            print ("borrowed books list empty!")
            return
        for book in self.__borrowed_books:
            print(f"Title: {book.title}\n")
            print(f"Author: {book.author}\n")
            print(f"Available: {book.available}")

    def get_borrowed_books(self):
        return self.__borrowed_books

    def set_favourite_book(self,book):
        self.__favourite_book = book

    def view_favourite_book(self):
        book = self.__favourite_book
        if not book:
            print("No favourite book.")
            return 
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
    @property
    def name(self):
        return self.__name

class Library:
    def __init__(self):
        self.__books = []
        self.__members = []
    def empty_books(self):
        if len(self.__books) == 0:
            print(f"books list is empty.")
            return True
        return False

    def add_book(self):
        title = input("title name: ").strip()
        author = input("author name: ").strip()
        book = Book(title,author)
        self.__books.append(book)
        print("Book added successfully.")

    def add_member(self):
        name = input("Member name: ").strip()
        member_id = input("Member id: ").strip()
        age = input("Member age: ").strip()
        course = input("Member course: ").strip()
        member = Member(name,member_id,age,course)
        self.__members.append(member)
        print("Member added successfully.")

    def view_books(self):
        if self.empty_books():
            return
        for book in self.__books:
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Available: {book.available}")

    def delete_book(self):
        if self.empty_books():
            return
        question = input("which book do you want to delete ?").strip().lower()
        for index,book in enumerate(self.__books):
            if question == book.title.lower():
                if not book.available:
                    print(f"{book.title} has been borrowed.")
                    return
                deleted_book = self.__books.pop(index)
                print(f'{deleted_book.title} deleted successfully.')
                return
        print("book not found!")
        return

    def search_book(self):
        if self.empty_books():
            return
        search = input("Seach book: ").lower().strip()
        for book in self.__books:
            if book.title.lower() == search:
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Available: {book.available}")
                return
        print("book not found!")
        return

    def statistics(self):
        if self.empty_books():
            return
        total_books = 0
        available_books = 0
        unavailable_books = 0
        for book in self.__books:
            total_books+=1
            if book.available:
                available_books+=1
            else:
                unavailable_books+=1
        if total_books == 1:
            print(f"Total book: {total_books}")
        else:
            print(f"Total books: {total_books}")
        if available_books == 1:
            print(f"available book: {available_books}")
        else:
            print(f"available books: {available_books}")
        if unavailable_books == 1:
            print(f"borrowed book: {unavailable_books}")
        else:
            print(f"borrowed books: {unavailable_books}")
    
    def borrow_book(self):
        member_name = input("Member name: ").strip().lower()
        found_member = False
        for member in self.__members:
            if member.name.lower() == member_name:
                found_member = True
                book_title = input("Book title: ").strip().lower()
                for book  in self.__books:
                    if book_title == book.title.lower():
                        if book.borrow():
                            member.add_borrowed_books(book)
                            print(f"{book.title} has been added to borrowed book list successfully")
                            return
        if not found_member:
            print("member not found")
            return 
        print("Book not found")
        return
        
    def return_book(self):
        member_name = input("Member name: ").strip().lower()
        found_member = False
        for member in self.__members:
            if member.name.lower() == member_name :
                found_member = True
                book_title = input("Book title: ").strip().lower()
                for book  in self.__books:
                    if book_title == book.title.lower() and book in member.get_borrowed_books():
                        if book.return_book():
                            member.remove_borrowed_books(book)
                            print(f"{book.title} has been removed from the borrowed book list successfully.")
                            return 
        if not found_member:
            print("member not found")
            return
        print("Book not found")
        return
        
    def set_member_favourite_book(self):
        member_name = input("Member name: ").strip().lower()
        found_member = False
        for member in self.__members:
            if member_name == member.name.lower():
                found_member = True
                book_title = input("Enter book name: ").strip().lower()
                for book in self.__books:
                    if book_title == book.title.lower():
                        member.set_favourite_book(book)
                        return
        if not found_member:
            print("member not found!")
            return
        print("Book not found")

    def view_member_borrowed_books(self):
        member_name = input("Member name: ").strip().lower()
        for member in self.__members:
            if member_name == member.name.lower():
                member.view_borrowed_books()
                return
        print("Member not found!")

    def view_member_favourite_book(self):
        member_name = input("Member name: ").strip().lower()
        for member in self.__members:
            if member_name == member.name.lower():
                member.view_favourite_book()
                return
        print("favourite book not found!")   

def operations():
    library = Library()
    while True:
        choice = input("choice: ")
        if choice.isdigit():
            if choice == "1":
                library.add_book()
            elif choice == "2":
                library.add_member()          
            elif choice == "3":
                library.view_books()
            elif choice == "4":
                library.delete_book()
            elif choice == "5":
                library.search_book()
            elif choice == "6":
                library.statistics()
            elif choice == "7":
                library.borrow_book()
            elif choice == "8":
                library.return_book()
            elif choice == "9":
                library.set_member_favourite_book()
            elif choice == "10":
                library.view_member_borrowed_books()
            elif choice == "11":
                library.view_member_favourite_book()
            elif choice == "12":
                break
        else:
            print("your choice value must be a digit.")
            continue
operations()

        
