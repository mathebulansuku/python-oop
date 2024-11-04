# Special methods - Allow us to use some built in operations in python such as length or the print function with our own user created object.


class Book():

  def __init__(self, title,author, pages):
    
    self.title = title
    self.author = author
    self.pages = pages