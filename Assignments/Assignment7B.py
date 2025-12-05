class Book:
    def __init__(self, title):
        # Attributes
        self.title = title
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f'Error: "{self.title}" is already borrowed.')
        else:
            self.is_borrowed = True
            print(f'You borrowed "{self.title}".')

    def return_book(self):
        if not self.is_borrowed:
            print(f'Error: "{self.title}" was not borrowed.')
        else:
            self.is_borrowed = False
            print(f'You returned "{self.title}".')

    def display_info(self, index):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"{index} - {self.title} ({status})")

class Library:
    def __init__(self):
        self.books = [
            Book("Python Basics"),
            Book("Intro to AI")
        ]

    def show_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("Books in Library:")
        for index, book in enumerate(self.books):
            book.display_info(index)

    def borrow_book(self):
        if not self.books:
            print("No books in the library.")
            return
        available_indices = [i for i, b in enumerate(self.books) if not b.is_borrowed]
        if not available_indices:
            print("No available books to borrow.")
            return

        print("Books in Library:")
        for index, book in enumerate(self.books):
            if not book.is_borrowed:
                book.display_info(index)
        try:
            selection = int(input("Select a book to borrow: "))
            book = self.books[selection]
            book.borrow()
        except ValueError:
            print("Error: Please enter a valid number.")
        except IndexError:
            print("Error: Invalid book index.")

    def return_book(self):
        if not self.books:
            print("No books in the library.")
            return

        print("Books in Library:")
        for index, book in enumerate(self.books):
            book.display_info(index)

        try:
            selection = int(input("Select a book to return: "))
            book = self.books[selection]
            book.return_book()
        except ValueError:
            print("Error: Please enter a valid number.")
        except IndexError:
            print("Error: Invalid book index.")

    def add_book(self):
        title = input("Enter the title of the new book: ").strip()
        if title == "":
            print("Error: Title cannot be empty.")
            return

        new_book = Book(title)
        self.books.append(new_book)
        print(f'"{title}" has been added to the library!')

def main():
    library = Library()
    running = True

    while running:
        print("[Owl Library]")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Add Book")
        print("5. Exit")
        choice = input("> ")

        match choice:
            case "1":
                print()
                library.show_books()
                print()
            case "2":
                print()
                library.borrow_book()
                print()
            case "3":
                print()
                library.return_book()
                print()
            case "4":
                print()
                library.add_book()
                print()
            case "5":
                print("Exiting program... Goodbye!")
                running = False
            case _:
                print("Error: Invalid menu option.\n")

main()
