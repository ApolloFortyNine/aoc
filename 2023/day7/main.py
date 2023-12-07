from collections import Counter
with open("input.txt") as file:
    instructions_raw = file.read().splitlines()

card_ranks = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
all_ranks = []
def calc_rank(hand):
    counts = Counter(hand)
    rank = 0
    count_dict = {}
    for key, value in counts.items():
        count_dict[value] = count_dict.get(value, '') + key
    if 5 in count_dict:
        rank = 900000000000
    elif 4 in count_dict:
        rank = 800000000000
    elif 3 in count_dict and 2 in count_dict:
        rank = 700000000000
    elif 3 in count_dict:
        rank = 600000000000
    elif 2 in count_dict and 2 == len(count_dict[2]):
        rank = 500000000000
    elif 2 in count_dict:
        rank = 400000000000
    else:
        rank = 100000000000
    for i, x in enumerate(hand):
        value = 13 - card_ranks.index(x)
        multiplier = 100**(4-i)
        rank += (value * multiplier)
    return rank
for x in instructions_raw:
    splits = x.split()
    hand = splits[0]
    bet = int(splits[1])
    rank = calc_rank(hand)
    all_ranks.append([rank, bet])

all_ranks.sort()
total = 0
for i, x in enumerate(all_ranks):
    total += x[1] * (i+1)
print(all_ranks)
print(total)

# Part 2
card_ranks = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
all_ranks = []
def calc_rank(hand):
    if hand == 'JJJJJ':
        pass
    counts = Counter(hand)
    rank = 0
    count_dict = {}
    max_count = 0
    for key, value in counts.items():
        count_dict[value] = count_dict.get(value, '') + key
        if key != 'J':
            max_count = max(value, max_count)
    if 'J' in counts and 5 not in count_dict:
        if len(count_dict[max_count]) > 1:
            # Fix it
            first = count_dict[max_count][0]
            if first == 'J':
                first = count_dict[max_count][1]
                count_dict[max_count] = count_dict[max_count].replace(first, '')
            if len(count_dict[max_count]) == 1:
                count_dict.pop(max_count)
            else:
                count_dict[max_count] = count_dict[max_count][1:]
            count_dict[max_count + counts['J']] = first
            # counts['J'] = 0
            # counts[first] = counts[first] + counts['J']
        else:
            letter = count_dict[max_count]
            count_dict.pop(max_count)
            count_dict[max_count + counts['J']] = letter
    key_to_delete = None
    for key, value in count_dict.items():
        if 'J' in value:
            if 5 in count_dict:
                if count_dict[5] == 'J':
                    continue
            key_to_delete = key
    if key_to_delete:
        if len(count_dict[key_to_delete]) > 1:
            count_dict[key_to_delete] = count_dict[key_to_delete].replace('J', '')
        else:
            count_dict.pop(key_to_delete)
    sum_total = 0
    for key, value in count_dict.items():
        sum_total += (key * len(value))
    if sum_total > 5:
        print("panic")
    if sum_total < 5:
        print("panic")
    if 5 in count_dict:
        rank = 900000000000
    elif 4 in count_dict:
        rank = 800000000000
    elif 3 in count_dict and 2 in count_dict:
        rank = 700000000000
    elif 3 in count_dict:
        rank = 600000000000
    elif 2 in count_dict and 2 == len(count_dict[2]):
        rank = 500000000000
    elif 2 in count_dict:
        rank = 400000000000
    else:
        rank = 100000000000
    for i, x in enumerate(hand):
        value = 13 - card_ranks.index(x)
        multiplier = 100**(4-i)
        rank += (value * multiplier)
    return rank
for x in instructions_raw:
    splits = x.split()
    hand = splits[0]
    bet = int(splits[1])
    rank = calc_rank(hand)
    all_ranks.append([rank, bet])

all_ranks.sort()
total = 0
for i, x in enumerate(all_ranks):
    total += x[1] * (i+1)
print(all_ranks)
print(total)