def student_counter():
  for i in range(1,5001):
    try:
      yield i
    except GeneratorExit:
      print("More whan 100 students")

student_generator = student_counter()
for student_id in student_generator:
  print(student_id)
  if student_id >= 100:
    student_generator.clouse()
