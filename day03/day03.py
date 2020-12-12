# Load input data
raw_data = []
with open('day03/input.txt', 'r') as f:
    for line in f:
        raw_data.append(line.strip())

def calc_trees_hit(raw_data, step_size_down, step_size_right):
    trees_counter = 0
    row = 0
    col = 0
    while row < len(raw_data):
        if raw_data[row][col] == '#':
            trees_counter += 1
        col = (col + step_size_right) % len(raw_data[row])
        row += step_size_down
    
    return trees_counter


# Part 1
print(calc_trees_hit(raw_data, 1, 3))


# Part 2
print(
    calc_trees_hit(raw_data, 1, 1) *
    calc_trees_hit(raw_data, 1, 3) *
    calc_trees_hit(raw_data, 1, 5) *
    calc_trees_hit(raw_data, 1, 7) *
    calc_trees_hit(raw_data, 2, 1)
)
