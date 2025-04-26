class Book:
    total_books = 0  # class variable

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"Total books now: {cls.total_books}")

# Example usage:
book1 = Book()
Book.increment_book_count() 

book2 = Book()
Book.increment_book_count() 

book3 = Book()
Book.increment_book_count() 