with open("input.txt") as file:
    groups_raw = file.read().split('\n\n')

groups = []
for i, group in enumerate(groups_raw):
    groups.append(group.splitlines())
    
total = 0

for group in groups:
    answer_set = set()
    for answers in group:
        for x in answers:
            answer_set.add(x)
    total += len(answer_set)
print(total)

# Part 2
total = 0
for group in groups:
    target = len(group)
    answer_dict = {}
    for answers in group:
        for x in answers:
            answer_dict[x] = answer_dict.get(x, 0) + 1
    for key, value in answer_dict.items():
        if value == target:
            total += 1

print(total)