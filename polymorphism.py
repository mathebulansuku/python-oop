# Polymorphism - A way in which different object classes can share the same method name. Those methods can be called from the same place even though a variety of different objects might be passed in

class Dog():

  def __init__(self, name):
    self.name = name 

  def speak(self):
    return self.name + "says woof!"
  

class Cat():

  def __init__(self, name):
    self.name = name 

  def speak(self):
    return self.name + "says meow!"