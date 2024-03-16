

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
        if abs(head[1] - tail[1]) >= 2:
          tail[1] += 1
          if tail[0] == head[0] -1:
            tail[0] += 1
          elif  tail[0] == head[0] +1:
            tail[0] -= 1
      elif line[0] == "L":
        head[0] -= 1
        if abs(head[0] - tail[0]) >= 2:
          tail[0] -= 1
          if tail[1] == head[1] -1:
            tail[1] += 1
          elif  tail[1] == head[1] +1:
            tail[1] -= 1
      elif line[0] == "R":
        head[0] += 1
        if abs(head[0] - tail[0]) >= 2:
          tail[0] += 1
          if tail[1] == head[1] -1:
            tail[1] += 1
          elif  tail[1] == head[1] +1:
            tail[1] -= 1
      elif line[0] == "D":
        head[1] -= 1
        if abs(head[1] - tail[1]) >= 2:
          tail[1] -= 1
          if tail[0] == head[0] -1:
            tail[0] += 1
          elif  tail[0] == head[0] +1:
            tail[0] -= 1
            
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
