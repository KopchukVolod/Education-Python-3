
class Circle:
  pi = 3.14
  def area(self, radius):
      return self.pi * radius ** 2 
circle = Circle()

pizza_area = circle.area(6)
print(pizza_area)

teaching_table_area = circle.area(18)
print(teaching_table_area)

round_room_area = circle.area(11460 / 2 )
print(round_room_area)
