# Fill in the line class methods to accept coordinates as a pair of tuples and return the slope and distance of t


class Line:

  def __init__(self,coor1,coor2):

    self.coor1 =(coor1, coor2)

  def distance(self):
      return ((self.coor1 - self.coor2) ** 2 + (self.coor1 - self.coor2) ** 2) ** 0.5

  def slope(self):
    pass