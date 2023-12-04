with open("input.txt") as file:
    instructions_raw = file.read().splitlines()
width = len(instructions_raw[0])
height = len(instructions_raw)
mask = [[0 for _ in range(width)] for _ in range(height)]
def populate_mask(i, j):
    mask[i+1][j] = 1
    mask[i+1][j+1] = 1
    mask[i+1][j-1] = 1
    mask[i-1][j] = 1
    mask[i-1][j-1] = 1
    mask[i-1][j+1] = 1
    mask[i][j+1] = 1
    mask[i][j-1] = 1
for i, x in enumerate(instructions_raw):
    for j, y in enumerate(x):
        if not y.isdigit() and y != '.':
            populate_mask(i, j)
print('mask done')

valid_numbers = []
for i, x in enumerate(instructions_raw):
    number = False
    valid = False
    current_number = ''
    for j, y in enumerate(x):
        number = y.isdigit()
        if not number:
            if current_number == '398' and i == 92:
                pass
            if valid:
                if (current_number):
                    valid_numbers.append(int(current_number))
                    current_number = ''
                valid = False
            else:
                if current_number:
                    print(i, current_number)
                current_number = ''
        elif number:
            current_number += y
            if mask[i][j] == 1:
                valid = True
        else:
            print('uhoh')
    else:
        if current_number and valid:
            valid_numbers.append(int(current_number))
print(sum(valid_numbers))