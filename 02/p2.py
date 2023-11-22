def get_score(data):
  score = 0
  for round in data:
    selection = round.split(" ")
    if selection[1] == 'A':
      score += 1
    elif selection[1] == 'B':
      score += 2
    elif selection[1] == 'C':
      score += 3
    opponent = ord(selection[0])
    i = ord(selection[1])
    difference = i - opponent

    if difference == 0:
      score += 3
    elif difference == 1 or difference == -2:
      score += 6

  return score

def select_shape(opponent_choice):
  rounds = opponent_choice.split("\n")

  output = []
  for round in rounds:
    selection = round.split(" ")
    result = f'{selection[0]} '

    if selection[1] == 'X':
      if selection[0] == 'A':
        result += 'C'
      elif selection[0] == 'B':
        result += 'A'
      elif selection[0] == 'C':
        result += 'B'
    elif selection[1] == 'Y':
      result += f'{selection[0]}'
    elif selection[1] == 'Z':
      if selection[0] == 'A':
        result += 'B'
      elif selection[0] == 'B':
        result += 'C'
      elif selection[0] == 'C':
        result += 'A'

    output.append(result)

  return output


data = """A Y
B X
C Z"""
assert get_score(select_shape(data)) == 12

with open("input.txt") as file:
  data = file.read()

print(get_score(select_shape(data)))