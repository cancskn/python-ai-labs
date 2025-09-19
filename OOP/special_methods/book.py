class Book:
    def __init__(self, name, pages):
        self.name =name
        self.pages =pages

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.pages == other.pages

book1 = Book("Dorian Gray", 140)
book2 = Book("Cats and Dogs", 140)
book3 = Book("History of Something", 1000)

print(book1.__eq__(book2))
print(book1.__eq__(book3))

