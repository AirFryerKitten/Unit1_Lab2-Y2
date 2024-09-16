class Rat:

  def __init__(self, sex, weight):
    self.sex = sex
    self.weight = weight
    self.litters = 0

  def __str__(self):
    return str(self.weight)

  def __repr__(self):
    return f"Sex:{self.sex} {self.weight}"

  def getWeight(self):
    return self.weight

  def getSex(self):
    return self.sex

  def canBreed(self):
    return self.litters <= 5

  def __lt__(self,other):
    return self.weight < other.weight

  def __gt__(self,other):
    return self.weight > other.weight

  def __le__(self,other):
    return self.weight <= other.weight

  def __ge__(self,other):
    return self.weight >= other.weight

  def __eq__(self,other):
    return self.weight == other.weight 


