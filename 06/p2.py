

def get_data(data):
  for i in range(14, len(data)):
    message = data[i-14:i]
    if len(list(set(message))) == 14:
      return i

  return 0

data = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

assert get_data(data) == 19

data = """bvwbjplbgvbhsrlpgdmjqwftvncz"""

assert get_data(data) == 23

data = """nppdvjthqldpwncqszvftbrmjlhg"""

assert get_data(data) == 23

data = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""

assert get_data(data) == 29

data = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

assert get_data(data) == 26

with open("input.txt") as file:
    data = file.read()


print(get_data(data))
