import numpy as np
from collections import Counter
from numpy_lru_cache_decorator import np_cache

# Load input data
with open('day10/input.txt', 'r') as f:
    adapters = list(map(int, f.read().split('\n')))

adapters = np.array([0] + sorted(adapters) + [max(adapters) + 3])


# Part 1
counts = dict(Counter(adapters[1:] - adapters[:-1]))
print(counts[1] * counts[3])


# Part 2
@np_cache()
def num_paths(arr):
    if len(arr) == 1:
        return 1
    steps = [idx for idx in range(1, 4) if (len(arr) > idx) and (arr[idx] - arr[0] <= 3)]
    return sum([num_paths(arr[jumpsize:]) for jumpsize in steps])

print(num_paths(adapters))
