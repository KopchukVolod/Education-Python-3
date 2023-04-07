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
    self.__numberOfStudents = newNumberOfStudents
      
  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"
    # return print("A {level} school named {name} with {numberOfStudents} students".format(level=self.level, name=self.name, numberOfStudents=self.numberOfStudents))

a1 = School("Kyiv", "middle", 30)
print(a1)
print(a1.get_name())
print(a1.get_level())
a1.set_numberOfStudents(100)
print(a1.get_numberOfStudents())

