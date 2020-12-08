# Load input data
nums = []
with open('day1/input.txt', 'r') as f:
    for line in f:
        nums.append(int(line.strip()))

# Part 1
for i in range(0, len(nums)):
    for j in range(i, len(nums)):
        if nums[i] + nums[j] == 2020:
            print(nums[i] * nums[j])
            break

# Part 2
for i in range(0, len(nums)):
    for j in range(i, len(nums)):
        for k in range(j, len(nums)):
            if nums[i] + nums[j] == 2020:
                print(nums[i] * nums[j] * nums[k])
                break
