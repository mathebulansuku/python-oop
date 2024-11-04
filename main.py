class Dog():

  # Class Object Attribute - Same for every instance of the class
  species = "mammal"

  def __init__(self,breed, name, spots):
    self.breed = breed 
    self.name = name

    #Spots is a boolean
    self.spots = spots
  # Attributes breed, name , spots
  #We take in an argument breed, name , spots
  #Assign it using self.attribute_name/argument


  # Methods - Operations or actions of the class
  def bark(self):
    print("Woof! Woof! my name is {}".format(self.name))

my_dog = Dog(breed='Lab', name="Chopper",spots=False)

my_dog.bark()


print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)