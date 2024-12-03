import re

with open("input.txt") as file:
  instructions_raw = file.read()

exp = r"mul\(\d+,\d+\)"

x = re.findall(exp, instructions_raw)
def mul(x, y):
  return x * y
total = 0
for y in x:
  total += eval(y)
print(total)

# part 2
x = re.finditer(exp, instructions_raw)
dos = re.finditer(r"do\(\)", instructions_raw)
donts = re.finditer(r"don't\(\)", instructions_raw)
enabled = True
enabled_dict = {}
total_2 = 0
for index in range(len(instructions_raw)):
  my_str = instructions_raw[:index]
  dos = list(re.finditer(r"do\(\)", my_str))
  donts = list(re.finditer(r"don't\(\)", my_str))
  if donts:
    if not dos:
      do_index = 0
    else:
      do_index = dos[-1].end()
    if donts[-1].end() > do_index:
      enabled = False
    else:
      enabled = True
  enabled_dict[index] = enabled
for y in x:
  is_enabled = enabled_dict[y.start()]
  if is_enabled:
    total_2 += eval(y.group())
print(total_2)