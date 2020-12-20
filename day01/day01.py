from bisect import bisect_left

# Load input data
nums = []
with open('day01/input.txt', 'r') as f:
    for line in f:
        nums.append(int(line.strip()))
nums = sorted(nums)

def index(a, x):
    """Locate the leftmost value exactly equal to x"""
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None

# Part 1
def part_one():
    for num in nums:
        complement_idx = index(nums, 2020 - num)
        if complement_idx:
            return num * nums[complement_idx]
print('Part 1:', part_one())

# Part 2
def part_two():
    for i, num1 in enumerate(nums):
        for num2 in nums[i+1:]:
            complement_idx = index(nums, 2020 - num1 - num2)
            if complement_idx:
                return num1 * num2 * nums[complement_idx]
print('Part 2:', part_two())
