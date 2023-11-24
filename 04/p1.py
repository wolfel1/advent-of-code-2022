import utils
import re

def get_pairs(pairs):
  
  double_pairs = 0
  assignments = []
  for pair in pairs:
    assignments = list(map(int, re.findall(r'\d+', pair)))
    includes = False
    if assignments[0] >= assignments[2] and assignments[1] <= assignments[3]:
      includes = True
    elif assignments[2] >= assignments[0] and assignments[3] <= assignments[1]:
      includes = True
    
    double_pairs += 1 if includes else 0
    
  return double_pairs

data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

utils.find_solution("\n", data, 2, get_pairs)
