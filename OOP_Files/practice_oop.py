# This file contains my practice code with OOP in python

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # class method
    @ classmethod
    def from_string(cls, book_str):
        new_string = book_str.strip().capitalize()
        new_string.find(" ")
        return new_string

my_first_book = Book("Abroad in Japan", "Chris Broad")

print(my_first_book.from_string("mynameMCAALSiste is anboifw"))
