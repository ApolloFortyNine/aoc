import re

with open("input.txt") as file:
    lines = file.read().splitlines()

all_rules = {}
counter = 0
for line in lines:
    counter += 1
    original_bag_re = re.compile(r'(.*?) bags contain')
    contained_bags_re = re.compile(r'(\d) (.+?) bag')
    parsed_contained = contained_bags_re.findall(line)
    parsed_original = original_bag_re.findall(line)
    # print(parsed_contained)
    all_rules[parsed_original[0]] = parsed_contained
print(counter)
# print(all_rules)
# parsed_rules_shiny_gold = {}
# def traverse(color):
#     if color in parsed_rules_shiny_gold:
#         return parsed_rules_shiny_gold[color]
#     elif color == 'shiny gold':
#         return 1
#     else:
#         next_colors = all_rules[color]
#         if not next_colors:
#             return 0
#         found = False
#         for num, next_color in next_colors:
#             result = traverse(next_color)
#             if result == 1:
#                 found = True
#             parsed_rules_shiny_gold[next_color] = result
#         if found:
#             parsed_rules_shiny_gold[color] = 1
#             return 1
#         else:
#             parsed_rules_shiny_gold[color] = 0
#             return 0
# print("start")
# all_colors = set()
# for key, value in all_rules.items():
#     # if not value:
#     #     print(key)
#     traverse(key)
#     all_colors.add(key)
#     for pair in value:
#         num, color = pair
#         all_colors.add(color)
#         # print(num, color)
#         # print(color)
#         # traverse(color)
# print("end")
# print(parsed_rules_shiny_gold)

# total = 0
# for key, value in parsed_rules_shiny_gold.items():
#     if key == 'shiny gold':
#         continue
#     if value == 1:
#         total += 1
# print(total)

# Part 2
parsed_bag_nums = {}
def traverse2(color):
    if color in parsed_bag_nums:
        return parsed_bag_nums[color]
    else:
        next_colors = all_rules[color]
        if not next_colors:
            parsed_bag_nums[color] = 0
            return 0
        total_result = 0
        counter = 0
        for num, next_color in next_colors:
            result = traverse2(next_color)
            total_result += (int(num) * result)
            total_result += int(num)
            counter += 1
            # parsed_bag_nums[next_color] = int(num) * result
        parsed_bag_nums[color] = total_result
        if (total_result == 0):
            print("panic")
        return total_result

for key, value in all_rules.items():
    traverse2(key)
# print(parsed_bag_nums)
print(parsed_bag_nums['shiny gold'])

mine = all_rules['shiny gold']
print(mine)
my_total = 0
for x in mine:
    my_total += (parsed_bag_nums[x[1]] * int(x[0]))
print(my_total)
print(len(parsed_bag_nums.keys()))
# print(len(all_colors))
print(len(all_rules.keys()))
value2 = 100000
for key, value in parsed_bag_nums.items():
    if (value == 1):
        print(key)
print(value2)
# print(all_rules)