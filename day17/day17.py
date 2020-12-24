import numpy as np
from copy import deepcopy
from math import ceil

# Load input data
with open('day17/input.txt', 'r') as file:
    initial_state = file.read().split('\n')

INITIAL_SIZE = len(initial_state)
N_CYCLES = 6
xdim = ydim = zdim = INITIAL_SIZE + 2 * (N_CYCLES)
xmid = ymid = zmid = xdim // 2

# Helper functions
def print_state(state, label):
    print('\n', label, ':', sep='')
    for z_axis in range(state.shape[2]):
        print(str(state[:, :, z_axis]), sep='\n', end='\n\n')

def count_active_neighbors(state, x, y, z):
    # Neighbors are within a 1-coordinate range
    active_count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                newx = x + i
                newy = y + j
                newz = z + k
                # Don't count the original point or go out of bounds
                if (((i != 0) or (j != 0) or (k != 0))
                    and (newx >= 0) and (newx < xdim)
                    and (newy >= 0) and (newy < ydim)
                    and (newz >= 0) and (newz < zdim)):
                        neighbor = state[newx, newy, newz]
                        if neighbor > 0:
                            active_count += 1    
    return active_count

def cycle(state):
    newstate = deepcopy(state)
    for x in range(xdim):
        for y in range(ydim):
            for z in range(zdim):
                active_neighbors = count_active_neighbors(state, x, y, z)
                if (state[x, y, z] > 0) and (active_neighbors not in [2, 3]):
                    newstate[x, y, z] = 0
                elif (state[x, y, z] == 0) and (active_neighbors == 3):
                    newstate[x, y, z] = 1
    return newstate


# Initialization - start with all inactive states (zeros)
start = np.zeros((xdim, ydim, zdim))

# Update zmid slice with the given initial state
z_idx = zmid
for row_idx in range(xmid - (INITIAL_SIZE // 2), int(ceil(xmid + (INITIAL_SIZE / 2)))):
    for col_idx in range(ymid - (INITIAL_SIZE // 2), int(ceil(ymid + (INITIAL_SIZE / 2)))):
        # Update if active
        if initial_state[row_idx - (xmid - (INITIAL_SIZE // 2))][col_idx - (ymid - (INITIAL_SIZE // 2))] == '#':
            start[row_idx, col_idx, z_idx] = 1

# Cycle N_CYCLES times
state = deepcopy(start)
for _ in range(N_CYCLES):
    state = cycle(state)
print('Part 1:', np.sum(state))


# Incorporate 4th dim, w ------------------------------------------------------
wdim = xdim
wmid = wdim // 2

def count_active_neighbors(state, x, y, z, w):
    # Neighbors are within a 1-coordinate range
    # This could be changed to a convolution filter/sum
    active_count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    newx = x + i
                    newy = y + j
                    newz = z + k
                    neww = w + l
                    # Don't count the original point or go out of bounds
                    if (((i != 0) or (j != 0) or (k != 0) or (l != 0))
                        and (newx >= 0) and (newx < xdim)
                        and (newy >= 0) and (newy < ydim)
                        and (newz >= 0) and (newz < zdim)
                        and (neww >= 0) and (neww < wdim)):
                            neighbor = state[newx, newy, newz, neww]
                            if neighbor > 0:
                                active_count += 1
    return active_count

def cycle(state):
    newstate = deepcopy(state)
    for x in range(xdim):
        for y in range(ydim):
            for z in range(zdim):
                for w in range(wdim):
                    active_neighbors = count_active_neighbors(state, x, y, z, w)
                    if (state[x, y, z, w] > 0) and (active_neighbors not in [2, 3]):
                        newstate[x, y, z, w] = 0
                    elif (state[x, y, z, w] == 0) and (active_neighbors == 3):
                        newstate[x, y, z, w] = 1
    return newstate

# Initialization
start = np.zeros((xdim, ydim, zdim, wdim))

# Update zmid/wmid slice with the given initial state
z_idx = zmid
w_idx = wmid
for row_idx in range(xmid - (INITIAL_SIZE // 2), int(ceil(xmid + (INITIAL_SIZE / 2)))):
    for col_idx in range(ymid - (INITIAL_SIZE // 2), int(ceil(ymid + (INITIAL_SIZE / 2)))):
        # Update if active
        if initial_state[row_idx - (xmid - (INITIAL_SIZE // 2))][col_idx - (ymid - (INITIAL_SIZE // 2))] == '#':
            start[row_idx, col_idx, z_idx, w_idx] = 1

# Cycle N_CYCLES times
state = deepcopy(start)
for _ in range(N_CYCLES):
    state = cycle(state)
print('Part 2:', np.sum(state))
