# Special methods - Allow us to use some built in operations in python such as length or the print function with our own user created object.


class Book():

  def __init__(self, title,author, pages):
    
    self.title = title
    self.author = author
    self.pages = pages

  def __str__(self):
    return f"{self.title} by {self.author}"
  

buku = Book('Journey to manhood', 'Nsuku', 240)

print(buku)