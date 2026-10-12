
class Library:
    def __init__(self):
        self.books = {
            "Python": True,
            "Maths": True,
            "Science": True
        }

    def show_books(self):
        for book, available in self.books.items():
            print(book, "-", "Available" if available else "Issued")

    def issue(self, book):
        if book in self.books and self.books[book]:
            self.books[book] = False
            print("Book issued successfully!")
        else:
            print("Book unavailable!")

    def return_book(self, book):
        if book in self.books and not self.books[book]:
            self.books[book] = True
            print("Book returned successfully!")
        else:
            print("Invalid return!")
