letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#print(len(letters))
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
#print(len(points))
zip_dic = zip(letters, points)
letter_to_points = {key:value for key, value in zip_dic}

letter_to_points[" "] = 0
print(letter_to_points)
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total
brownie_points = score_word("BROWNIE")
print(brownie_points)
player_to_words = {"player1":	["wordNerd",	"Lexi Con",	"Prof Reader"], "BLUE":	["EARTH",	"ERASER",	"ZAP"], "TENNIS":	["EYES",	"BELLY",	"COMA"], "EXIT":	["MACHINE",	"HUSKY",	"PERIOD"]}
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
    player_to_points[player] = player_points
print(player_to_points)

# play_word("player1", "CODE") 
# print(player_to_words)
# print(player_to_points)


