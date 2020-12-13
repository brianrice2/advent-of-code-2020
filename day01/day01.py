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
    for i in range(0, len(nums)):
        complement_idx = index(nums, 2020 - nums[i])
        if complement_idx:
            return nums[i] * nums[complement_idx]
print(part_one())


# Part 2
def part_two():
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            complement_idx = index(nums, 2020 - nums[i] - nums[j])
            if complement_idx:
                return nums[i] * nums[j] * nums[complement_idx]
print(part_two())
