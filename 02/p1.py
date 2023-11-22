def get_score(data):
  rounds = data.split("\n")

  score = 0
  for round in rounds:
    selection = round.split(" ")
    if selection[1] == 'X':
      score += 1
    elif selection[1] == 'Y':
      score += 2
    elif selection[1] == 'Z':
      score += 3
    opponent = ord(selection[0])
    i = ord(selection[1])
    difference = i - (opponent + (ord('X') - ord('A')))

    if difference == 0:
      score += 3
    elif difference == 1 or difference == -2:
      score += 6

  return score

data = """A Y
B X
C Z
A Z
C X
B Z"""
assert get_score(data) == 34

with open("input.txt") as file:
  data = file.read()

print(get_score(data))