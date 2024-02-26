

import re

class Node:
  def __init__(self, name, parent = None, size = 0):
    self.name = name
    self.parent = parent
    self.size = size
    self.childs = set()

  def addChild(self, child):
    self.childs.add(child)

  def hasChilds(self):
    return len(self.childs) != 0

  def getChilds(self):
    return self.childs

  def get_parent(self):
    return self.parent

  def get_size(self):
    return self.size

  def set_size(self, size):
    self.size = size

def get_directory_sizes(current_node: Node):
    total_size = 0
    for node in current_node.getChilds():
      if node.hasChilds():
        get_directory_sizes(node)
      total_size += node.get_size()

    current_node.set_size(total_size)

total_size = 0
def get_total_size(current_node: Node):
  global total_size

  for node in current_node.getChilds():
    if node.hasChilds():
      get_total_size(node)
      size = node.get_size()
      if size <= 100000:
        total_size += size


def get_data(data):
  lines = data.split("\n")

  root = Node("/")
  current_node = root
  lines.pop(0)
  for line in lines:
    if line.startswith("$ cd"):
      directory = line.split("cd ", 1)[1]
      if directory != "..":
        node = Node(directory, current_node)
        current_node.addChild(node)
        current_node = node
      else:
        current_node = current_node.get_parent()
    elif line[0].isdigit():
      name = re.findall(r'\s(.*)', line)[0]
      size = list(map(int, re.findall(r'\d+', line)))[0]
      current_node.addChild(Node(name, current_node, size))

  get_directory_sizes(root)

  get_total_size(root)
  return total_size



  # total = 0
  # for value in dir_sizes.values():
  #   if value < 100000:
  #     total += value

  # return total

data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

assert get_data(data) == 95437

with open("input.txt") as file:
    data = file.read()


print(get_data(data))
