import re

def get_crates(data):
  stacks_data, procedures_data = data.split("\n\n")
  
  stacks = {}
  crate_rows = stacks_data.split("\n")
  count = list(map(int, re.findall(r'\d+', crate_rows[-1])))[-1]
  for crate_row in reversed(crate_rows):
    crates = list(map(str, re.findall(r'[A-Z]+|    ', crate_row)))
    for i in range(0, count):
      try:
        if not len(crates[i].strip()) == 0:
          if stacks.get(i+1):
            stacks[i+1].append(crates[i])
          else:
            stacks[i+1] = [crates[i]]
      except:
        continue
      
  
  for procedure in procedures_data.split("\n"):
    steps = list(map(int, re.findall(r'\d+', procedure)))
    crates = stacks.get(steps[1])[-steps[0]:]
    print(crates)
    del stacks.get(steps[1])[-steps[0]:]
    stacks[steps[2]].extend(crates)
      
  top_crates = ""
  for i in range(0, len(stacks)):
    if not len(stacks[i+1]) == 0:
      top_crates += stacks[i+1].pop()
  
  return top_crates

data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

assert get_crates(data) == "MCD"

with open("input.txt") as file:
    data = file.read()
    
print(get_crates(data))

