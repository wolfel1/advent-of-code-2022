

import re


def get_data(data):
  lines = data.split("\n")

  directories = dict()
  current_directory = ""
  for line in lines:
    if line.startswith("$ cd"):
      directory = line.split("cd ", 1)[1]
      directories[directory] = list()
      current_directory = directory
    elif line.startswith("dir"):
      directory = line.split("dir ", 1)[1]
      directories[current_directory].append(directory)


  dir_sizes = dict()
  for line in lines:
    if line.startswith("$ cd"):
      directory = line.split("cd ", 1)[1]
      dir_sizes[directory] = 0
      current_directory = directory
    elif line.startswith("dir"):
      directory = line.split("dir ", 1)[1]
      dir_sizes[current_directory] += directories.get(directory) or 0
    elif line[0].isdigit():
      size = list(map(int, re.findall(r'\d+', line)))[0]
      dir_sizes[current_directory] += size


  for key, item in reversed(directories.items()):
    for directory in item:
      dir_sizes[key] += dir_sizes[directory]

  total = 0
  for value in dir_sizes.values():
    if value < 100000:
      total += value

  return total

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
