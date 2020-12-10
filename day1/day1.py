# Load input data
nums = []
with open('day1/input.txt', 'r') as f:
    for line in f:
        nums.append(int(line.strip()))

nums = sorted(nums)

def binary_search(arr, low_index, high_index, num, sum_to): 
    if high_index >= low_index:
        mid = (high_index + low_index) // 2

        if num + arr[mid] == sum_to:
            return mid
        elif num + arr[mid] > sum_to:
            return binary_search(arr, low_index, mid - 1, num, sum_to) 
        else:
            return binary_search(arr, mid + 1, high_index, num, sum_to) 
    else: 
        # Element is not present in the array
        return None

# Part 1
for i in range(0, len(nums)):
    complement = binary_search(nums, i + 1, len(nums), nums[i], sum_to=2020)
    if complement:
        print(nums[i] * nums[complement])
        break


# Part 2
for i in range(0, len(nums)):
    for j in range(i, len(nums)):
        complement = binary_search(nums, i, len(nums), nums[i] + nums[j], sum_to=2020)
        if complement:
            print(nums[i] * nums[j] * nums[complement])
            break
