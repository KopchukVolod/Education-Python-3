def summa():
    yield 'Summa Cum Laude'
def magna():
    yield 'Magna Cum Laude' 
def cum_laude():
    yield 'Cum Laude'
def graduation_countdown(days):
  while days >= 0:
    days_left = yield days
    if days_left != None:
      days = days_left
    else:
      days -= 1
days = 25
countdown_generator = (day for day in range(days, -1, -1))
grad_days = graduation_countdown(days)
for i in grad_days:
  if i == 15:
    grad_days.send(10)
  elif i == 3:
    grad_days.close()
  print("Days Left: " + str(i))
def honors_generator(gpas):
  for i in gpas:
    if i > 3.9:
      yield from summa()
    elif i > 3.7:
      yield from magna()
    elif i > 3.5:
      yield from cum_laude()

gpas = [3.2, 4.0, 3.6, 2.9]
honors = honors_generator(gpas)
for honor_label in honors:
  print(honor_label)
