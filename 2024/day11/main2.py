from collections import defaultdict


def process_instructions_optimized(input_file, iterations=75):
    def split_number(x):
        if x == 0:
            return [1]
        x_str = str(x)
        x_len = len(x_str)
        if x_len % 2 == 0:
            mid = x_len // 2
            left = int(x_str[:mid])
            right = int(x_str[mid:])
            return [left, right]
        else:
            return [x * 2024]

    freq = defaultdict(int)
    with open(input_file) as file:
        instructions_raw = list(map(int, file.read().splitlines()[0].split()))
        for x in instructions_raw:
            freq[int(x)] += 1

    for iteration in range(1, iterations + 1):
        new_freq = defaultdict(int)
        for num, count in freq.items():
            transformed = split_number(num)
            for new_num in transformed:
                new_freq[new_num] += count
        freq = new_freq

    final_length = sum(freq.values())
    print(final_length)
    return final_length


final_length = process_instructions_optimized("input.txt", iterations=75)
