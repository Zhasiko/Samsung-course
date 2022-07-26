class Book:
    def __init__(self, name, code, pages):
        self.name = name
        self.code = code
        self.pages = pages
        
    def getBookData(self):
        return self.name, self.pages
    
class ScientificBook(Book):
    def __init__(self, name, code, pages, price, publicsher):
        super().__init__(name,code,pages)
        self.price = price
        self.publicsher = publicsher
    
    def getBookData(self):
        return super().getBookData(), self.price, self.publicsher
    
class LiteratureBook(Book):
    def __init__(self, name, code, pages,author,year):
        super().__init__(name,code,pages)
        self.author = author
        self.year = year
        
    def getBookData(self):
        return super().getBookData(), self.author, self.year
    
class Library:
    def __init__(self, name, city, country, books):
        self.name = name
        self.city = city
        self.country = country
        self.books = books
    def addBook(self):
        self.books.append(Book.getBookData())
        
    def LibraryData(self):
        return self.name, self.country, self.books
    
book1 = ScientificBook('Alchimic',25,400,1500,"Koelo")
book2 = LiteratureBook('Anna Karenina', 46,485,"Tolstoy",1922)

library = Library("Zhambyl","Almaty", "KZ", [book1])

print(Library.LibraryData())

