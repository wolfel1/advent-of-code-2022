

def get_data(data):
  lines = data.split("\n")
  row_size = len(lines[0]) - 1
  col_size = len(lines) - 1
  grid = [None] * (row_size +1)

  pivot = 0
  for line in lines:

    for char in line:
      if grid[pivot] is None:
        grid[pivot] = list()
      grid[pivot].append(int(char))
      pivot += 1

    pivot = 0

  visible_trees = row_size * col_size

  return visible_trees

data = """30373
25512
65332
33549
35390"""

assert get_data(data) == 21

with open("input.txt") as file:
    data = file.read()


print(get_data(data))
