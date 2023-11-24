import string
import utils

def get_summed_priority(rucksacks):

  summed_priorities = 0
  for i in range(0, len(rucksacks), 3):
    badge = ''
    priority = 0
    for l in range(0, len(rucksacks[i])):
      for j in range(0, len(rucksacks[i+1])):
        for k in range(0, len(rucksacks[i+2])):
          if rucksacks[i][l] == rucksacks[i+1][j] == rucksacks[i+2][k]:
            badge = rucksacks[i][l]
            if badge.islower():
              priority = string.ascii_lowercase.index(badge)
            else:
              priority = string.ascii_uppercase.index(badge) + 26
      
    priority += 1
    summed_priorities += priority  

  return summed_priorities

data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


utils.find_solution("\n", data, 70, get_summed_priority)
