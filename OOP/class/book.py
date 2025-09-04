
class Book:
    all_books = []

    def __init__(self, title, price, year=0, publisher="", genre="", author=""):
        self.title = title
        self.price = price
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        Book.all_books.append(self)

    @classmethod
    def add_book(cls):
        title = input('Title: ')
        price = float(input('Price: '))
        more = input('Do you want to add more details? (y/n): ').lower()

        if more == 'y':
            year = int(input('Year: '))
            publisher = input('Publisher: ')
            genre = input('Genre: ')
            author = input('Author: ')
            cls(title, price, year, publisher, genre, author)
        else:
            cls(title, price)

    @classmethod
    def show_books(cls):
        if not cls.all_books:
            print('No books available')
            return
        for book in cls.all_books:
            print(f'Here is the books available: ')
            if book.publisher:
                print(f'{book.title} by {book.publisher}')
            else:
                print(f'{book.title}')

    @classmethod
    def search_book(cls):
        book_find = input('Enter the title of the book that you want to search: ')
        for book in cls.all_books:
            if book.title.lower() == book_find.lower():
                print(f'Yes, {book.title} is in the store!')
                return
        print('Not avaliable')


if __name__ == "__main__":
    print('Menu:')
    print('1 - add book')
    print('2 - show all books available')
    print('3 - search book')
    print('0 - exit')

    while True:
        choice = int(input('Enter your choice(0-3): '))
        if choice == 1:
            Book.add_book()
        elif choice == 2:
            Book.show_books()
        elif choice == 3:
            Book.search_book()
        elif choice == 0:
            break

















