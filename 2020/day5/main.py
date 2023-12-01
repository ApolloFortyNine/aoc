with open("input.txt") as file:
    lines = file.read().splitlines()
    
seat_id = 0
seats = []
for line in lines:
    rows = [x for x in range(128)]
    cols = [x for x in range(8)]
    for i, x in enumerate(line):
        if i < 7:
            if x == 'F':
                rows = rows[:len(rows)//2]
            elif x == 'B':
                rows = rows[len(rows)//2:]
        else:
            if x == 'L':
                cols = cols[:len(cols)//2]
            elif x == 'R':
                cols = cols[len(cols)//2:]
    seat_id = max(seat_id, rows[0]*8+cols[0])
    seats.append(rows[0]*8 + cols[0])

seats.sort()
print(seats)

highest_seat = max(seats)
lowest_seat = min(seats)

for x in range(lowest_seat, highest_seat):
    if x not in seats:
        print(x)