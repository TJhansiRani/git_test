class Book:
    bookName = None
    bookNo = None
    price = None

    def __init__(self):
        pass

    def Set_bookName(self, bookName):
        self.bookName = bookName

    def Set_bookNo(self, bookNo):
        self.bookNo = bookNo

    def Set_price(self, price):
        self.price = price

    def get_bookName(self):
        return self.bookName

    def get_bookNo(self):
        return self.bookNo

    def get_price(self):
        return self.price


book1 = Book()
book1.Set_bookName("The Worrier")
book1.Set_bookNo(2)
book1.Set_price(5623)
print("Book Name:", book1.get_bookName())
print("Book No:", book1.get_bookNo())
print("Price:", book1.get_price())

book2 = Book()
book2.Set_bookName("Rohith")
book2.Set_bookNo(3)
book2.Set_price(564)
print("Book Name:", book2.get_bookName())
print("Book No:", book2.get_bookNo())
print("Price:", book2.get_price())


book3 = Book()
book3.Set_bookName("Vijayasri")
book3.Set_bookNo(4)
book3.Set_price(56465)
print("Book Name:", book3.get_bookName())
print("Book No:", book3.get_bookNo())
print("Price:", book3.get_price())
