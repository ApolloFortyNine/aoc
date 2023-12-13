import numpy as np
with open("input.txt") as file:
    instructions_raw = file.read().split('\n\n')

patterns = []
for x in instructions_raw:
    split_by_line = x.split('\n')
    split_by_line = [list(x) for x in split_by_line]
    new_pattern = np.array(split_by_line)
    patterns.append(new_pattern)

def check_pattern_symmetry(pattern):
    rows, cols = pattern.shape
    middle = cols // 2
    vertical = False
    max_col = None
    for i in range(0,cols):
        left_side = pattern[:, :i]
        right_side = pattern[:, i:]
        left_side_flipped = np.flip(left_side, axis=1)
        min_cols = min(left_side_flipped.shape[1], right_side.shape[1])
        left_side_truncated = left_side_flipped[:, :min_cols]
        right_side_truncated = right_side[:, :min_cols]
        if np.array_equal(left_side_truncated, right_side_truncated):
            vertical = True
            max_col = i
    horizontal = False
    max_row = None
    for i in range(0, rows):
        top_side = pattern[:i, :]
        bottom_side = pattern[i:, :]
        top_side_flipped = np.flip(top_side, axis=0)
        min_rows = min(top_side_flipped.shape[0], bottom_side.shape[0])
        top_side_truncated = top_side_flipped[:min_rows, :]
        bottom_side_truncated = bottom_side[:min_rows:, :]
        if np.array_equal(top_side_truncated, bottom_side_truncated):
            horizontal = True
            max_row = i
    return (max_col, max_row)

columns_left = 0
rows_above = 0
for pattern in patterns:
    pat_columns_left, pat_rows_above = check_pattern_symmetry(pattern)
    if pat_columns_left:
        columns_left += pat_columns_left
    if pat_rows_above:
        rows_above += pat_rows_above
print(rows_above * 100 + columns_left)