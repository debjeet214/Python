class Library:
  def __init__(self):
    no_of_books = 0
    self.books = []

  def addbooks(self, book,author,price):
    self.books.append(book)
    self.author=author
    self.price=price
    self.no_of_books = len(self.books)

  def showinfo(self):
    print(f"There are totally {self.no_of_books} books. The books are:")
    for books in self.books:
      print(f"Name : {self.books}\nAuthor : {self.author}")

b1 = Library()
b1.addbooks("The Workholic", "Alexandra Slammi", 2000)
b1.addbooks("The Oath", "Dragon Instance", 999)
b1.addbooks("The Workholic", "Alexandra Slammi", 2000)
b1.showinfo()
