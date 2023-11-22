import re

def get_calories(data):
  elves = data.split("\n\n")

  calories = []
  for elf in elves:
    calories.append(list(map(int, re.findall(r'\d+', elf))))

  calories.sort(reverse=True, key=sum)

  highest = 0
  for i in range(0, 3):
    highest += sum(calories[i])

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
assert get_calories(data) == 45000

with open("input.txt") as file:
  data = file.read()

print(get_calories(data))