with open("input.txt") as file:
  instructions_raw = file.read().splitlines()

total_safe = 0
for x in instructions_raw:
  num_report = [int(y) for y in x.split()]
  sort_1 = sorted(num_report)
  sort_2 = sorted(num_report, reverse=True)
  if num_report != sort_1 and num_report != sort_2:
    continue
  prev = None
  for level in num_report:
    if not prev:
      prev = level
    else:
      diff = abs(level - prev)
      prev = level
      if diff == 0 or diff > 3:
        break
  else:
    total_safe += 1
print(total_safe)

# part 2

def is_safe(all_reports):
  for num_report in all_reports:
    sort_1 = sorted(num_report)
    sort_2 = sorted(num_report, reverse=True)
    if num_report != sort_1 and num_report != sort_2:
      continue
    prev = None
    for level in num_report:
      if not prev:
        prev = level
      else:
        diff = abs(level - prev)
        prev = level
        if diff == 0 or diff > 3:
          break
    else:
      return True
total_safe_2 = 0
for x in instructions_raw:
  print(x)
  num_report = [int(y) for y in x.split()]
  all_reports = [num_report]
  all_reports.extend([num_report[:i] + num_report[i+1:] for i in range(len(num_report))])
  print(all_reports)
  if is_safe(all_reports):
    total_safe_2 += 1
print(total_safe_2)