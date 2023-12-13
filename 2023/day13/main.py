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
old_results = {}
for i, pattern in enumerate(patterns):
    pat_columns_left, pat_rows_above = check_pattern_symmetry(pattern)
    old_results[i] = (pat_columns_left, pat_rows_above)
    if pat_columns_left:
        columns_left += pat_columns_left
    if pat_rows_above:
        rows_above += pat_rows_above
print(rows_above * 100 + columns_left)

columns_left = 0
rows_above = 0
for i, pattern in enumerate(patterns):
    max_cols_left = None
    max_rows_above = None
    for x, row in enumerate(pattern):
        for y, _ in enumerate(row):
            new_pattern = np.copy(pattern)
            new_char = ''
            if new_pattern[x, y] == '.':
                new_char = '#'
            else:
                new_char = '.'
            new_pattern[x, y] = new_char
            pat_columns_left, pat_rows_above = check_pattern_symmetry(new_pattern)
            old_columns_left, old_rows_above = old_results[i]
            if not pat_columns_left and not pat_rows_above:
                continue
            else:
                if pat_columns_left:
                    if pat_columns_left == old_columns_left:
                        pass
                    elif not max_cols_left:
                        max_cols_left = pat_columns_left
                    else:
                        max_cols_left = max(pat_columns_left, max_cols_left)
                if pat_rows_above:
                    if pat_rows_above == old_rows_above:
                        pass
                    elif not max_rows_above:
                        max_rows_above = pat_rows_above
                    else:
                        max_rows_above = max(pat_rows_above, max_rows_above)
    old_columns_left, old_rows_above = old_results[i]
    if max_cols_left and max_cols_left != old_columns_left:
        columns_left += max_cols_left 
    if max_rows_above and max_rows_above != old_rows_above:
        rows_above += max_rows_above
    print(max_rows_above, max_cols_left)
print(rows_above * 100 + columns_left)