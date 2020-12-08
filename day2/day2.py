# Load input data
raw_data = []
with open('day2/input.txt', 'r') as f:
    for line in f:
        raw_data.append(line.strip())

# Part 1
def is_valid_pt1(lower_bound, upper_bound, letter, password):
    return ((password.count(letter) >= lower_bound) and 
            (password.count(letter) <= upper_bound))

# Count number of valid passwords
valid_password_counter = 0
for line in raw_data:
    line_split = line.strip().split()

    # Lower and upper bounds
    lo_hi = line_split[0].split('-')
    lower_bound = int(lo_hi[0])
    upper_bound = int(lo_hi[1])

    # Letter that the bounds apply to
    letter = line_split[1][:-1]

    # Password to test
    password = line_split[2]

    # Test validity
    valid_password_counter += is_valid_pt1(lower_bound, upper_bound, letter, password)

print(valid_password_counter)


# Part 2
def is_valid_pt2(lower_index, upper_index, letter, password):
    return ((password[lower_index] == letter) ^
            (password[upper_index] == letter))

# Count number of valid passwords
valid_password_counter = 0
for line in raw_data:
    line_split = line.strip().split()

    # Lower and upper bounds
    lo_hi = line_split[0].split('-')
    lower_index = int(lo_hi[0]) - 1
    upper_index = int(lo_hi[1]) - 1

    # Letter that the bounds apply to
    letter = line_split[1][:-1]

    # Password to test
    password = line_split[2]

    # Test validity
    valid_password_counter += is_valid_pt2(lower_index, upper_index, letter, password)

print(valid_password_counter)
