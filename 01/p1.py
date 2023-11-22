import re

def get_calories(data):
  elves = data.split("\n\n")

  calories = []
  for elf in elves:
    calories.append(list(map(int, re.findall(r'\d+', elf))))

  highest = 0
  for calory in calories:
    if sum(calory) > highest:
      highest = sum(calory)

  return highest

data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
assert get_calories(data) == 24000

with open("input.txt") as file:
  data = file.read()

print(get_calories(data))