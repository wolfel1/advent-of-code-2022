def move_up(front, knot):
    if abs(front[1] - knot[1]) >= 2:
      knot[1] += 1
      follow_horizontal(front, knot)

def move_left(front, knot):
    if abs(front[0] - knot[0]) >= 2:
      knot[0] -= 1
      follow_vertical(front, knot)

def move_right(front, knot):
    if abs(front[0] - knot[0]) >= 2:
      knot[0] += 1
      follow_vertical(front, knot)

def move_down(front, knot):
    if abs(front[1] - knot[1]) >= 2:
      knot[1] -= 1
      follow_horizontal(front, knot)

def follow_vertical(front, knot):
    if knot[1] == front[1] -1:
      knot[1] += 1
    elif  knot[1] == front[1] +1:
      knot[1] -= 1

def follow_horizontal(front, knot):
    if knot[0] == front[0] -1:
      knot[0] += 1
    elif  knot[0] == front[0] +1:
      knot[0] -= 1

def get_data(data):
  lines = data.split("\n")
  
  head = [0, 0]
  tail = [0, 0]
  tail_covered = list()
  for line in lines:
    line = line.split(" ")
    for i in range(0, int(line[1])):
      if line[0] == "U":
        head[1] += 1
        move_up(head, tail)
      elif line[0] == "L":
        head[0] -= 1
        move_left(head, tail)
      elif line[0] == "R":
        head[0] += 1
        move_right(head, tail)
      elif line[0] == "D":
        head[1] -= 1
        move_down(head, tail)
            
      tail_covered.append(tail.copy())
    
  unique_covered = set(tuple(i) for i in tail_covered)
      
  return len(unique_covered)

data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

assert get_data(data) == 13

with open("input.txt") as file:
    data = file.read()


print(get_data(data))
