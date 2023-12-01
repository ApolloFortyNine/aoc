with open("input.txt") as file:
    instructions_raw = file.read().splitlines()
instructions = []
for x in instructions_raw:
    instructions.append(int(x))

def is_two_sum(arr, idx):
    two_sum_arr = arr[idx-25:idx]
    print(len(two_sum_arr))
    print(two_sum_arr)
    print(arr[idx])
    
    answers = {}
    
    for i, x in enumerate(two_sum_arr):
        for y in two_sum_arr[i:25]:
            answers[x+y] = 1
    if arr[idx] in answers:
        return True
    else:
        return False
    
bad_number = 0
bad_idx = 0
for i, x in enumerate(instructions[25:]):
    if not is_two_sum(instructions, i+25):
        print("out")
        print(i+25)
        print(instructions[i+25])
        bad_number = instructions[i+25]
        bad_idx = i+25
        break

# Part 2
print("part2 start")
print(bad_number)
answer = []
for i, x in enumerate(instructions[:bad_idx]):
    runner = x
    runner_arr = []
    for y in instructions[i+1:bad_idx]:
        runner += y
        runner_arr.append(y)
        if runner == bad_number:
            answer.append(x)
            answer += runner_arr
            print("part2")
            print(answer)
            print(min(answer) + max(answer))
            print(sum(answer))
            break
        if runner > bad_number:
            # print("bigger")
            break