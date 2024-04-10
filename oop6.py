class Book:
    bookName = None
    bookNo = None
    price = None

    def __init__(self):
        pass

    def Set_book_information(self, bookName, bookNo, price):
        self.bookName = bookName
        self.bookNo = bookNo
        self.price = price

    def get_bookName(self):
        return self.bookName

    def get_bookNo(self):
        return self.bookNo

    def get_price(self):
        return self.price


book1 = Book()
book1.Set_book_information("The Moments", 23, 568)
print("Book Name:", book1.get_bookName())
print("Book No:", book1.get_bookNo())
print("Price:", book1.get_price())

book2 = Book()
book2.Set_book_information("the Return", 56, 852)
print("Book Name:", book2.get_bookName())
print("Book No:", book2.get_bookNo())
print("Price:", book2.get_price())
