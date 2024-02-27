

import re

class Node:
  def __init__(self, name, parent = None, size = 0):
    self.name = name
    self.parent = parent
    self.size = size
    self.childs = set()

  def add_child(self, child):
    self.childs.add(child)

  def has_childs(self):
    return len(self.childs) != 0

  def get_childs(self):
    return self.childs

  def get_parent(self):
    return self.parent

  def get_size(self):
    return self.size

  def set_size(self, size):
    self.size = size

def get_directory_sizes(current_node: Node):
    total_size = 0
    for node in current_node.get_childs():
      if node.has_childs():
        get_directory_sizes(node)
      total_size += node.get_size()

    current_node.set_size(total_size)




def get_data(data):
  lines = data.split("\n")

  directories = list()
  root = Node("/")
  current_node = root
  lines.pop(0)
  for line in lines:
    if line.startswith("$ cd"):
      directory = line.split("cd ", 1)[1]
      if directory != "..":
        node = Node(directory, current_node)
        current_node.add_child(node)
        directories.append(node)
        current_node = node
      else:
        current_node = current_node.get_parent()
    elif line[0].isdigit():
      name = re.findall(r'\s(.*)', line)[0]
      size = list(map(int, re.findall(r'\d+', line)))[0]
      current_node.add_child(Node(name, current_node, size))

  get_directory_sizes(root)


  needed = 30_000_000 - (70_000_000 - root.get_size())
  smallest = 70_000_000
  for dir in directories:
    size = dir.get_size()
    if size >= needed and size < smallest:
        smallest = size

  return smallest


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

assert get_data(data) == 24_933_642

with open("input.txt") as file:
    data = file.read()


print(get_data(data))
