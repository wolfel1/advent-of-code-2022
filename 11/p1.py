from typing import Callable
import re
from functools import reduce

class Monkey:
  def __init__(self):
     pass

  def set_items(self, items: list[int]):
     self.items = items

  def set_operation(self, operation: Callable[[int], int]):
     self.operation = operation

  def set_test(self, test: Callable[[int], int]):
     self.test = test

  def inspect(self, monkeys: list) -> int:
      inspections = 0
      for item in self.items:
        inspections += 1
        item = self.operation(item)
        item //= 3
        index = self.test(item)
        monkeys[index].add_item(item)
      
      self.items = []

      return inspections

  def add_item(self, item: int):
    self.items.append(item)

def parse_input(data):
  monkeys: list[Monkey] = []

  monkeys_data = data.split("\n\n")
   
  for monkey_data in monkeys_data:
    lines = monkey_data.split("\n")
    monkey = Monkey()
    i = 0
    for line in lines:
      if "Starting items" in line:
        items = [int(s) for s in re.findall(r'\d+', line)]
        monkey.set_items(items)
      elif "Operation" in line:
        operator = re.findall(r'[\+\*]', line)[0]
        amount = [int(s) for s in re.findall(r'\d+', line)]
        if len(amount) == 0:
          if operator == "+":
              operation = lambda item: item + item
          elif operator == "*":
              operation = lambda item: item * item
        elif operator == "+":
            operation = lambda item, c=amount[0]: item + c
        elif operator == "*":
            operation = lambda item, c=amount[0]: item * c

        monkey.set_operation(operation)
      elif "Test" in line:
          amount = [int(s) for s in re.findall(r'\d+', line)][0]
          true_index = [int(s) for s in re.findall(r'\d+', lines[i + 1])][0]
          false_index = [int(s) for s in re.findall(r'\d+', lines[i + 2])][0]
          test = lambda item, c=amount, true_cond=true_index, false_cond=false_index: true_cond if item % c == 0 else false_cond
          monkey.set_test(test)
      
      i += 1
    
    monkeys.append(monkey)

  return monkeys

def get_data(data):
  monkeys = parse_input(data)
  inspections_each = [0 for m in range(0, len(monkeys))]
  monkey_index = 0
  rounds = 20

  for round in range(0, rounds):
    for monkey in monkeys:
        inspection = monkey.inspect(monkeys)
        inspections_each[monkey_index] += inspection
        monkey_index += 1

    monkey_index = 0

  most_active = sorted(inspections_each, reverse=True)
  result = reduce(lambda a, b: a * b, most_active[:2])
  return result

data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

assert get_data(data) == 10605

with open("input.txt") as file:
    data = file.read()


print(get_data(data))
