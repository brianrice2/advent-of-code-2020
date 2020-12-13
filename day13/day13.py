import numpy as np

# Load input data
with open('day13/input.txt', 'r') as f:
    inlist = f.read().split('\n')

start_time = int(inlist[0])
all_buses = inlist[1].split(',')
available_buses = [int(bus_no) for bus_no in inlist[1].split(',') if bus_no != 'x']


# Part 1
choose_bus = min([bus - (start_time % bus) for bus in available_buses])
min_bus = 0
for i in range(len(available_buses)):
    bus = available_buses[i]
    wait_time = bus - (start_time % bus)
    if wait_time == choose_bus:
        print(bus * wait_time)
        break


# Part 2
# Sort buses by decreasing remainder (time until bus departure)
remainders = [0] + [int(all_buses[i]) - i for i in range(1, len(all_buses)) if all_buses[i] != 'x']
zipped = sorted(zip(available_buses, remainders), key=lambda x: x[1], reverse=True)
sorted_buses = [x[0] for x in zipped]
sorted_remainders = [x[1] for x in zipped]

# Use Chinese remainder theorem to find satisfying timestamp
N = np.prod(sorted_buses)
bNx = []
for i in range(len(sorted_buses)):
    bi = sorted_remainders[i]
    Ni = int(N / sorted_buses[i])
    xi = pow(Ni, sorted_buses[i] - 2, sorted_buses[i])  # since bus numbers are prime
    bNx.append(bi * Ni * xi)
print(sum(bNx) % N)
