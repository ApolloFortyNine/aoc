with open("input.txt") as file:
    instructions_raw = file.read().splitlines()
    
arrival_time = int(instructions_raw[0])
departures = instructions_raw[1].split(',')
print(departures)

closest = 1000000
c_bus_id = 0
for x in departures:
    if x == 'x':
        continue
    bus_id = int(x)
    remainder = bus_id - (arrival_time % bus_id)
    if remainder < closest:
        c_bus_id = bus_id
        closest = remainder

print(closest * c_bus_id)

# Part 2
print("Part2")
departure_arr = []
max_bus = 0
for i, x in enumerate(departures):
    if x == 'x':
        continue
    max_bus = max(max_bus, int(x))
    departure_arr.append([i, int(x)])
print(departure_arr)
print(max_bus)

start = max_bus - 60
jump = departure_arr[0][1]
time_stamp = 0
for delta, bus_id in departure_arr[1:]:
    while (time_stamp + delta) % bus_id != 0:
        time_stamp += jump
    jump *= bus_id
print(time_stamp)

while True:
    left = 0
    for x in departure_arr:
        check_time = start + x[0]
        remainder = check_time % x[1]
        if remainder != 0:
            left = x[1] - remainder
            # print(x[1], left, start)
            break
    else:
        print(start)
    if (start % 100000000) == 0:
        print(start)
    start += max_bus
    # start += 1