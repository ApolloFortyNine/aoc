with open("input.txt") as file:
    instructions_raw = file.read().splitlines()

time_arr = instructions_raw[0].split(':')[1].split()
time_arr = list(map(lambda x: int(x), time_arr))
distance_arr = instructions_raw[1].split(':')[1].split()
distance_arr = list(map(lambda x: int(x), distance_arr))
print('hi')

win_ways_arr = [0, 0, 0, 0]
for i, x in enumerate(time_arr):
    built_speed = 0
    for y in range(x):
        distance_traveled = (x-y) * built_speed
        if distance_traveled > distance_arr[i]:
            win_ways_arr[i] += 1
        built_speed += 1
runner = 1
for x in win_ways_arr:
    runner = runner * x
print(runner)

# Part 2
total_time = ''
total_distance = ''

for x in time_arr:
    total_time += str(x)
for x in distance_arr:
    total_distance += str(x)

total_time = int(total_time)
total_distance = int(total_distance)
win_ways_arr = [0]
built_speed = 0
for i, x in enumerate([total_time]):
    built_speed = 0
    for y in range(x):
        distance_traveled = (x-y) * built_speed
        if distance_traveled > total_distance:
            win_ways_arr[i] += 1
        built_speed += 1
print(win_ways_arr)