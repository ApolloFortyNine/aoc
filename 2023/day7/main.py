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
    # 1 0 0 0 0 0 