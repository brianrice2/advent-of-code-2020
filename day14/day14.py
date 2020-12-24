from itertools import product

# Load input data
with open('day14/input.txt', 'r') as file:
    inlist = file.read().split('\n')


# Part 1
def update(value, mask, mask_override_values):
    result = list(value[2:])  # treat as list for slice assignment, ignoring 0b prefix
    for i in range(0, len(mask)):
        result[i] = mask[i] if mask[i] in mask_override_values else result[i]
    return '0b' + ''.join(result)  # convert back to binary string

mem = {}
mask = 'X' * 36
for line in inlist:
    name, value = line.split(' = ')
    if name == 'mask':
        mask = value
    else:
        mem_location = int(name[:-1][4:])
        val_binary = format(int(value), '#038b')
        mem[mem_location] = int(update(val_binary, mask, '01'), 2)

print('Part 1:', sum(list(mem.values())))


# Part 2
def get_combinations(address):
    addresses = []
    x_count = address[2:].count('X')
    fill_values = product([0, 1], repeat=x_count)
    for fill_value in fill_values:
        x_idx = 0
        combo = list(address[2:])
        for i in range(len(combo)):
            if combo[i] == 'X':
                combo[i] = str(fill_value[x_idx])
                x_idx += 1
        addresses.append('0b' + ''.join(combo))
    return addresses

mem = {}
for line in inlist:
    name, value = line.split(' = ')
    if name == 'mask':
        mask = value
    else:
        mem_location = int(name[:-1][4:])
        mem_binary = format(mem_location, '#038b')
        addresses = get_combinations(update(mem_binary, mask, '1X'))
        for address in addresses:
            mem[int(address, 2)] = int(value)

print('Part 2:', sum(list(mem.values())))
