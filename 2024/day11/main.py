def process_instructions(input_file, iterations=75):
    with open(input_file) as file:
        instructions_raw = list(map(int, file.read().splitlines()[0].split()))

    print("Initial List:", instructions_raw)
    final_list = instructions_raw

    for k in range(iterations):
        new_final_list = []
        for x in final_list:
            if x == 0:
                new_final_list.append(1)
            else:
                x_str = str(x)
                x_len = len(x_str)
                if x_len % 2 == 0:
                    mid = x_len // 2
                    new_left = int(x_str[:mid])
                    new_right = int(x_str[mid:])
                    new_final_list.append(new_left)
                    new_final_list.append(new_right)
                else:
                    new_final_list.append(x * 2024)
        final_list = new_final_list
        print(k)
    print("Final Length:", len(final_list))
    return final_list


final_result = process_instructions("input.txt")
