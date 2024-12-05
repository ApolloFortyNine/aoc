with open("input.txt") as file:
  instructions_raw = file.read()

from collections import defaultdict

first_half,second_half = instructions_raw.split('\n\n')

order_dict = defaultdict(list)

for x in first_half.splitlines():
  num, before = x.split('|')
  order_dict[int(num)].append(int(before))

total = 0
bad_indexes = []
second_half_split = second_half.splitlines()
for j, x in enumerate(second_half_split):
  update = x.split(',')
  update = [int(i) for i in update]
  seen = []
  for y in update:
    before_these = order_dict[y]
    for z in before_these:
      if z in seen:
        break
    else:
      seen.append(y)
      continue
    bad_indexes.append(j)
    break
  else:
    middle_i = len(update)//2
    total += update[middle_i]
print(total)
# print(bad_indexes)

# Part 2
def bubble_sort(arr):
  for n in range(len(arr), 0, -1):
    swapped = False  

    seen = []
    for i in range(n):
      cur = arr[i]
      before_these = order_dict[arr[i]]
      if any(x in seen for x in before_these):
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
        swapped = True
      seen.append(cur)
      
    if not swapped:
        break
total2 = 0
for i in bad_indexes:
  bad_update = second_half_split[i].split(',')
  bad_update = [int(x) for x in bad_update]
  #print(bad_update)
  bubble_sort(bad_update)
  #print(bad_update)
  middle_i = len(bad_update)//2
  total2 += bad_update[middle_i]
print(total2)