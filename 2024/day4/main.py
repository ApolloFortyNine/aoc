with open("input.txt") as file:
  instructions_raw = file.read().splitlines()

print(len(instructions_raw))
print(len(instructions_raw[0]))
# exit()
example = "XXMASMSMAMMMSSSMASXMXSASXMXAAXXMMXAMXSXMASXAXMAMXXXMSAMSAMXXXMAXSAMXSAMMXXXSSMSMSSXMSMAAXXMX"
grid = instructions_raw
# grid = [example]
dirs = ['right', 'left', 'up', 'down', 'upr', 'upl', 'downr', 'downl']
def spells_xmas(y, x, rem, dir):
  if (dir == 'right'):
    x_diff = 1
    y_diff = 0
  if (dir == 'left'):
    x_diff = -1
    y_diff = 0
  if (dir == 'up'):
    x_diff = 0
    y_diff = -1
  if (dir == 'down'):
    x_diff = 0
    y_diff = 1
  if (dir == 'upr'):
    x_diff = 1
    y_diff = -1
  if (dir == 'upl'):
    x_diff = -1
    y_diff = -1
  if (dir == 'downr'):
    x_diff = 1
    y_diff = 1
  if (dir == 'downl'):
    x_diff = -1
    y_diff = 1
  if len(rem) == 0:
    return True
  new_x = x+x_diff
  new_y = y+y_diff
  # print(new_x, new_y)
  if new_x > (len(grid[0])-1) or new_x < 0 or new_y > (len(grid) - 1) or new_y < 0:
    return False
  next_char = grid[new_y][new_x]
  if grid[new_y][new_x] == rem[0]:
    return spells_xmas(new_y,new_x,rem[1:],dir)
  else:
    return False

def main():
  total = 0
  for i, row in enumerate(grid):
    for j, char in enumerate(row):
      if char == 'X':
        # print(j, i)
        for dir in dirs:
          if spells_xmas(i, j, 'MAS', dir):
            total += 1
  print(total)
main()

# part 2
def forms_x(y, x):
  try:
    if y == 0 or x == 0 or y == (len(grid) - 1) or x == (len(grid[0]) - 1):
      return False
    topl = grid[y-1][x-1]
    botr = grid[y+1][x+1]
    topr = grid[y-1][x+1]
    botl = grid[y+1][x-1]
    if topl == 'S' and botr == 'M' and topr == 'S' and botl == 'M':
      return True
    if topl == 'M' and botr == 'S' and topr == 'M' and botl == 'S':
      return True
    if topl == 'S' and botr == 'M' and topr == 'M' and botl == 'S':
      return True
    if topl == 'M' and botr == 'S' and topr == 'S' and botl == 'M':
      return True
  except:
    return False
def part2():
  total = 0
  for i, row in enumerate(grid):
    for j, char in enumerate(row):
      if char == 'A':
        if forms_x(i, j):
          total += 1
  print(total)
part2()