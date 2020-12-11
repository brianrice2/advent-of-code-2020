from copy import deepcopy

# Load input data
with open('day11/input.txt', 'r') as f:
    layouts = f.read().split()

# Helper functions
def in_bounds(layouts, rownum, colnum):
    # Check if an index is in bounds
    maxrow = len(layouts)
    maxcol = len(layouts[0])
    return (rownum in range(0, maxrow)) and (colnum in range(0, maxcol))

def nearby_occupied_seats(layouts, rownum, colnum, radius):
    # Count the number of occupied seats around (rownum, colnum)
    # Scan along one direction until an occupied seat or the boundary is found
    occupied_count = 0
    step_size = 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            step_size = 1
            while step_size <= radius:
                newrow = rownum + step_size * i
                newcol = colnum + step_size * j
                if in_bounds(layouts, newrow, newcol) and (i != 0 or j != 0):
                    # If the index is in bounds, check if the seat is occupied
                    if layouts[newrow][newcol] == '.':
                        step_size += 1
                    else:
                        seat = 1 if layouts[newrow][newcol] == '#' else 0
                        occupied_count += seat
                        break
                else:
                    # If the index is out of bounds, no point in checking add'l steps
                    break

    return occupied_count

def seat_one_round(layouts, radius, tolerance):
    new_layouts = deepcopy(layouts)
    num_changes = 0
    for rownum in range(len(layouts)):
        for colnum in range(len(layouts[0])):
            if (layouts[rownum][colnum] == 'L' and
                nearby_occupied_seats(layouts, rownum, colnum, radius) == 0):
                    # Empty seats become occupied if all nearby seats are empty
                    new_layouts[rownum] = new_layouts[rownum][:colnum] + \
                                            '#' + new_layouts[rownum][colnum+1:]
                    num_changes += 1
            elif (layouts[rownum][colnum] == '#' and
                nearby_occupied_seats(layouts, rownum, colnum, radius) >= tolerance):
                    # Occupied seats become empty if at least `tolerance` nearby seats are filled
                    new_layouts[rownum] = new_layouts[rownum][:colnum] + \
                                            'L' + new_layouts[rownum][colnum+1:]
                    num_changes += 1
    
    return new_layouts, num_changes


# Part 1
layouts_part1 = deepcopy(layouts)
num_changes = 1
while num_changes > 0:
    layouts_part1, num_changes = seat_one_round(layouts_part1, radius=1, tolerance=4)

# Count occupied seats
print('Part 1 occupied seats:', ''.join(layouts_part1).count('#'))
# > 2412


# Part 2
layouts_part2 = deepcopy(layouts)
num_changes = 1
while num_changes > 0:
    layouts_part2, num_changes = seat_one_round(layouts_part2, radius=len(layouts_part2[0]), tolerance=5)

# Count occupied seats
print('Part 2 occupied seats:', ''.join(layouts_part2).count('#'))
# > 2176
