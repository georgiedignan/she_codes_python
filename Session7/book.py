class Book:
    #attributes - size, pages, colour, thickness
    #methods - turning a page, closing, opening

    def __init__(self, title, author, pages, current_page):
        #assignment to object attributes
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.bookmark = 1  #assign by default
    
    def bookmark_page(self):
        self.bookmark = self.current_page
    
    def turn_page(self):
        self.current_page += 1

    #string representation
    def __str__(self):
        return f"Title:{self.title}, Author:{self.author}, Pages:{self.pages}"
    
    def __len__(self):
        return self.pages

    #create a method turn back the page
    def turn_back(self):
        self.current_page -= 1

    def goto_page(self,page_number):
        self.current_page = page_number
    

my_book = Book("A great book", "me", 198, 1)
# print(my_book.__str__())
# print(my_book)
# print(my_book.bookmark) #attr
# my_book.turn_page() #method
# my_book.bookmark_page()
# print(my_book.bookmark)

my_book.goto_page(101)
print(my_book.current_page)