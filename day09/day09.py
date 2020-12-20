# Load input data
with open('day09/input.txt', 'r') as f:
    encodings = list(map(int, f.read().split('\n')))

preamble_length = 25

# Helper functions
def binary_search(arr, low_index, high_index, base_num, sum_to): 
    # Given `base_num`, find some other number in `arr` which together sum to `sum_to`
    if high_index >= low_index:
        mid = (high_index + low_index) // 2

        if base_num + arr[mid] == sum_to:
            return mid
        elif base_num + arr[mid] > sum_to:
            return binary_search(arr, low_index, mid - 1, base_num, sum_to) 
        else:
            return binary_search(arr, mid + 1, high_index, base_num, sum_to) 
    else: 
        # Element is not present in the array
        return None

def has_counterpart(window, preamble_length, num):
    for x in range(preamble_length):
        counterpart = binary_search(window, x + 1, preamble_length - 1, window[x], sum_to=num)
        if counterpart:
            return True
    return False

# Part 1
for i in range(preamble_length, len(encodings)):
    window = sorted(encodings[i - preamble_length:i])
    current_num = encodings[i]
    if not has_counterpart(window, preamble_length, current_num):
        print('Part 1:', current_num)
        break

# Part 2
target_sum = 257342611
for i in range(len(encodings)):
    contig_nums = [encodings[i]]
    contig_sum = sum(contig_nums)
    
    # Add neighboring numbers if they don't put sum over the limit
    next_idx = i + 1
    while contig_sum < target_sum:
        if (next_idx < len(encodings) and contig_sum < target_sum):
            contig_nums += [encodings[next_idx]]
            contig_sum = sum(contig_nums)
            next_idx += 1

    # Check for exit condition
    if contig_sum == target_sum:
        print('Part 2:', min(contig_nums) + max(contig_nums))
        break
