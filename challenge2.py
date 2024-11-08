class Cylinder:

  def __init__(self, height=1, radius=1):
    self.height = height
    self.radius = radius

  def volume(self):
    return 3.14 * (self.radius)**2 * self.height

  def surface_area(self):
    return 2 * 3.14 * self.radius * (self.radius + self.height)
  

mycylinder = Cylinder()

print(mycylinder.volume())
print(mycylinder.surface_area())
  