# Inheritance - A way of forming new classes using classes that have already been defined
# Benefits - The ability to reuse code and reduce complexity of a program

class Animal():

  def __init__(self):
    print('ANIMAL CREATED')

  def who_am_i(self):
    print('I am an animal')

  def eat(self):
    print('I am eating')


class Dog(Animal):

  def __init__(self):
    Animal.__init__(self)
    print('Dog is created')


my_dog = Dog()

my_dog.