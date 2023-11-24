import string

def get_summed_priority(data):
  rucksacks = data.split("\n")

  summed_priorities = 0
  for rucksack in rucksacks:
    half = int(len(rucksack) / 2)
    compartments = [rucksack[:half], rucksack[half:]]
    
    found_in_both = ''
    priority = 0
    for i in range(0, len(compartments[0])):
      for j in range(0, len(compartments[1])):
        if compartments[1][j] == compartments[0][i]:
          found_in_both = compartments[1][j]
          if found_in_both.islower():
            priority = string.ascii_lowercase.index(found_in_both)
          else:
            priority = string.ascii_uppercase.index(found_in_both) + 26
      
    priority += 1
    summed_priorities += priority  

  return summed_priorities

data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

assert get_summed_priority(data) == 157

with open("input.txt") as file:
  data = file.read()

print(get_summed_priority(data))