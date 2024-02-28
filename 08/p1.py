class Tree:
  def __init__(self, size):
    self.size = size
    self.top = None
    self.right = None
    self.left = None
    self.bottom = None
    self.edge = True
    self.neighbours = 0

  def set_edge(self):
    self.neighbours += 1
    self.edge = self.neighbours != 4

  def set_top(self, top):
    self.top = top
    self.set_edge()

  def set_bottom(self, bottom):
    self.bottom = bottom
    self.set_edge()

  def set_left(self, left):
    self.left = left
    self.set_edge()

  def set_right(self, right):
    self.right = right
    self.set_edge()

  def get_size(self) -> int:
    return self.size

  def get_top(self):
    return self.top

  def get_bottom(self):
    return self.bottom

  def get_right(self):
    return self.right

  def get_left(self):
    return self.left

  def is_edge(self):
    return self.edge

def get_data(data):
  lines = data.split("\n")
  row_size = len(lines[0])
  col_size = len(lines)
  grid = [None] * row_size

  for line in lines:
    pivot = 0
    for char in line:
      if grid[pivot] is None:
        grid[pivot] = list()
      grid[pivot].append(Tree(int(char)))
      pivot += 1

  column_index = 0
  while column_index < row_size:
    row_index = 0
    while row_index < col_size:
      tree: Tree = grid[column_index][row_index]

      if row_index -1 >= 0:
        tree.set_top(grid[column_index][row_index-1])

      if row_index +1 < row_size:
        tree.set_bottom(grid[column_index][row_index+1])

      if column_index -1 >= 0:
        tree.set_left(grid[column_index-1][row_index])

      if column_index + 1 < col_size:
        tree.set_right(grid[column_index+1][row_index])

      row_index += 1

    column_index  += 1

  column_index = 0
  visible_trees = 0
  while column_index < row_size:
    row_index = 0
    while row_index < col_size:
      greater = 0
      actual_tree = grid[column_index][row_index]
      if not actual_tree.is_edge():

        size = actual_tree.get_size()
        tree = actual_tree
        while tree is not None:
          tree = tree.get_top()
          if tree is not None and tree.get_size() >= size:
            greater += 1
            break

        tree = actual_tree
        while tree is not None:
          tree = tree.get_bottom()
          if tree is not None and tree.get_size() >= size:
            greater += 1
            break


        tree = actual_tree
        while tree is not None:
          tree = tree.get_left()
          if tree is not None and tree.get_size() >= size:
            greater += 1
            break


        tree = actual_tree
        while tree is not None:

          tree = tree.get_right()
          if tree is not None and tree.get_size() >= size:
            greater += 1
            break

      if greater != 4:
        visible_trees += 1

      row_index += 1
    column_index += 1

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
