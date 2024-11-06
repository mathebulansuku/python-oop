# Special methods - Allow us to use some built in operations in python such as length or the print function with our own user created object.


class Book():

  def __init__(self, title,author, pages):
    
    self.title = title
    self.author = author
    self.pages = pages

  def __str__(self): # Special method that gives the string representation of the class
    return f"{self.title} by {self.author}"
  
  def __len__(self): # allows you to declare the length of the class Book
    return self.pages
  
  def __del__(self):
    print(f"{self.title} has been deleted!")
  

buku = Book('Journey to manhood', 'Nsuku', 240)

print(buku)
str(buku)
len(buku)