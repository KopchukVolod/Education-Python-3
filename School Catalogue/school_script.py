#School Catalogue
class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents
    
  def set_numberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents
      
  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"
    # return print("A {level} school named {name} with {numberOfStudents} students".format(level=self.level, name=self.name, numberOfStudents=self.numberOfStudents))
class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy
  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + " The pickup policy is {pickupPolicy}".format(pickupPolicy=self.pickupPolicy)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "high", numberOfStudents)
    self.sportsTeams = sportsTeams
  def get_sportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    parentRepr1 = super().__repr__()
    return parentRepr1 + " have team with {sportsTeams}".format(sportsTeams=self.sportsTeams[1])

a1 = School("Kyiv", "middle", 158)
print(a1)
a2 = PrimarySchool("MySchool", 159, "free")  
#print(a2.get_pickupPolicy())
print(a2)
a3 = HighSchool("'Best school of Volodymyr Kopchuk'", 100, ["Tennis", "Basketball"])
print(a3)
a4 =  HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(a4)
