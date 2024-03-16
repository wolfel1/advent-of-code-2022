

def get_data(data):
  lines = data.split("\n")
  
  movement_start = 11
  difference = 10
  head = [0, 0]
  tail = [0, 0]
  tail_covered = list()
  for line in lines:
    line = line.split(" ")
    for i in range(0, int(line[1])):
      if line[0] == "U":
        head[1] += 1
        if abs(head[1] - tail[1]) >= movement_start:
          tail[1] += 1
          if tail[0] == head[0] -difference:
            tail[0] += 1
          elif  tail[0] == head[0] +difference:
            tail[0] -= 1
      elif line[0] == "L":
        head[0] -= 1
        if abs(head[0] - tail[0]) >= movement_start:
          tail[0] -= 1
          if tail[1] == head[1] -difference:
            tail[1] += 1
          elif  tail[1] == head[1] +difference:
            tail[1] -= 1
      elif line[0] == "R":
        head[0] += 1
        if abs(head[0] - tail[0]) >= movement_start:
          tail[0] += 1
          if tail[1] == head[1] -difference:
            tail[1] += 1
          elif  tail[1] == head[1] +difference:
            tail[1] -= 1
      elif line[0] == "D":
        head[1] -= 1
        if abs(head[1] - tail[1]) >= movement_start:
          tail[1] -= 1
          if tail[0] == head[0] -difference:
            tail[0] += 1
          elif  tail[0] == head[0] +difference:
            tail[0] -= 1
            
      tail_covered.append(tail.copy())
    
  unique_covered = set(tuple(i) for i in tail_covered)
      
  return len(unique_covered)

data = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

assert get_data(data) == 36

with open("input.txt") as file:
    data = file.read()


print(get_data(data))
