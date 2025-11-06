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
  start_x = 0
  start_y = 0
  
  rope = [[start_x, start_y] for i in range(0, 10)]
  head = rope[0]
  one = rope[1]
  tail = rope[9]
  tail_covered = list()
  for line in lines:
    line = line.split(" ")
    for i in range(0, int(line[1])):
      last_knot = one.copy()
      if line[0] == "U":
        head[1] += 1
        move_up(head, one)
      elif line[0] == "L":
        head[0] -= 1
        move_left(head, one)
      elif line[0] == "R":
        head[0] += 1
        move_right(head, one)
      elif line[0] == "D":
        head[1] -= 1
        move_down(head, one)

      movement = False if last_knot[0] == one[0] and last_knot[1] == one[1] else True

      if movement:
        for j in range(2, 10):
          knot = rope[j]
          if not last_knot[0] == knot[0] or not last_knot[1] == knot[1]:
            temp = knot.copy()
            rope[j] = last_knot.copy()
            last_knot = temp.copy()
        
            
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

result = get_data(data)
print(result)
assert result == 1

data = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

result = get_data(data)
print(result)
assert result == 36

with open("input.txt") as file:
    data = file.read()


print(get_data(data))
