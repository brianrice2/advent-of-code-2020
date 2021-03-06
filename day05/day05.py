# Load input data
with open('day05/input.txt', 'r') as file:
    partitions = file.read()

NROWS = 128
SEATS_PER_ROW = 8
FRONT_BACK_SPLIT = 7
LEFT_RIGHT_SPLIT = 3

def locate(partition, available_rows, front_delim = 'F', back_delim = 'B'):
    # Recursive binary split to locate row/seat
    # Exit condition at the last binary split
    if partition == front_delim:
        return available_rows[0]
    elif partition == back_delim:
        return available_rows[1]

    # Split in half and recursively analyze again
    midpoint = len(available_rows) // 2
    if partition[0] == front_delim:
        return locate(partition[1:], available_rows[:midpoint + 1], front_delim=front_delim, back_delim=back_delim)
    else:
        return locate(partition[1:], available_rows[midpoint:], front_delim=front_delim, back_delim=back_delim)

# Part 1
seat_ids = []
for partition in partitions.split():
    row_partition = partition[:FRONT_BACK_SPLIT]
    seat_partition = partition[-LEFT_RIGHT_SPLIT:]

    # Find ticket's row and seat number
    row_number = locate(row_partition, list(range(0, NROWS)))
    seat_number = locate(seat_partition, list(range(0, SEATS_PER_ROW)), front_delim = 'L', back_delim = 'R')
    seat_ids.append(row_number * 8 + seat_number)

print('Part 1:', max(seat_ids))

# Part 2
# Find where neighboring seat IDs are _two_ apart instead of just one
sorted_seat_ids = sorted(seat_ids)
for i in range(1, len(sorted_seat_ids)):
    current_seat = sorted_seat_ids[i]
    previous_seat = sorted_seat_ids[i - 1]
    if current_seat - previous_seat > 1:
        print('Part 2:', current_seat - 1)
        break
