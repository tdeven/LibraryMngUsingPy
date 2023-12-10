class Myclass:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, books):
        self.books.append(books)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The library has:{self.noBooks} books.The books are:-")

        for book in self.books:
            print(book)


    
lst = Myclass()
lst.addBook("Some books")
lst.addBook("Some books")
lst.showInfo()