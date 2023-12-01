with open("input.txt") as file:
    instructions_raw = file.read().splitlines()

instructions = []
for x in instructions_raw:
    command = x[0]
    value = int(x[1:])
    instructions.append((command,value))

location = [0, 0]
heading = 0

for x in instructions:
    match x[0]:
        case 'N':
            location[1] += x[1]
        case 'S':
            location[1] -= x[1]
        case 'E':
            location[0] += x[1]
        case 'W':
            location[0] -= x[1]
        case 'L':
            heading -= x[1]
        case 'R':
            heading += x[1]
        case 'F':
            match heading % 360:
                case 0:
                    location[0] += x[1]
                case 90:
                    location[1] -= x[1]
                case 180:
                    location[0] -= x[1]
                case 270:
                    location[1] += x[1]
print(abs(location[0]) + abs(location[1]))

# Part 2
location = [0, 0]
waypoint_offset = [10, 1]
heading = 0
def get_new_waypoint(waypoint_offset, degrees):
    new_location = [0,0]
    match degrees:
        case 0:
            new_location = waypoint_offset
        case 90:
            new_location[0] = waypoint_offset[1]
            new_location[1] = -waypoint_offset[0]
        case 180:
            new_location[0] = -waypoint_offset[0]
            new_location[1] = -waypoint_offset[1]
            # new_location[0] = waypoint_offset[1]
            # new_location[1] = -waypoint_offset[0]
            # new_location[0] = waypoint_offset[1]
            # new_location[1] = -waypoint_offset[0]
        case 270:
            new_location[0] = -waypoint_offset[1]
            new_location[1] = waypoint_offset[0]
            # new_location[0] = waypoint_offset[1]
            # new_location[1] = -waypoint_offset[0]
            # new_location[0] = waypoint_offset[1]
            # new_location[1] = -waypoint_offset[0]
            # new_location[0] = waypoint_offset[1]
            # new_location[1] = -waypoint_offset[0]
    return new_location
for x in instructions:
    match x[0]:
        case 'N':
            waypoint_offset[1] += x[1]
        case 'S':
            waypoint_offset[1] -= x[1]
        case 'E':
            waypoint_offset[0] += x[1]
        case 'W':
            waypoint_offset[0] -= x[1]
        case 'L':
            degrees = -x[1] % 360
            waypoint_offset = get_new_waypoint(waypoint_offset, degrees)
        case 'R':
            degrees = x[1] % 360
            waypoint_offset = get_new_waypoint(waypoint_offset, degrees)
        case 'F':
            for x in range(x[1]):
                location[0] += waypoint_offset[0]
                location[1] += waypoint_offset[1]
print(abs(location[0]) + abs(location[1]))