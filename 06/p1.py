

def get_data(data):
  for i in range(4, len(data)):
    a, b, c, d = data[i-4:i]
    if not a == b and not a == c and not a == d:
      if not b == c and not b == d:
        if not c == d:
          return i

  return 0

data = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

assert get_data(data) == 7

data = """bvwbjplbgvbhsrlpgdmjqwftvncz"""

assert get_data(data) == 5

data = """nppdvjthqldpwncqszvftbrmjlhg"""

assert get_data(data) == 6

data = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""

assert get_data(data) == 10

data = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

assert get_data(data) == 11

with open("input.txt") as file:
    data = file.read()


print(get_data(data))
