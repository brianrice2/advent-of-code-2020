import re
from copy import deepcopy

# Load input data
with open('day08/input.txt', 'r') as file:
    instructions = file.read().split('\n')
num_instructions = len(instructions)

# Helper functions
def parse_input(instruction):
    # Parse operation and argument details
    instruction_parts = instruction.split()
    operation, argument = instruction_parts[0], instruction_parts[1]
    amt = int(argument[1:])
    delta = amt if argument[0] == '+' else -amt

    return operation, delta

def step(instructions, idx, accumulator):
    # Process operation and update accumulator if applicable
    operation, delta = parse_input(instructions[idx])
    if operation == 'jmp':
        idx += delta
    else:
        if operation == 'acc':
            accumulator += delta
        idx += 1
    return idx, accumulator

def loop(instructions, part_one = False):
    # Makes all steps and handles counters
    past_instructions = []
    accumulator = 0
    idx = 0
    
    while idx != num_instructions:
        if idx in past_instructions:
            # Differentiate return value btw infinite loop and success (for Part 2 only)
            return accumulator if part_one else None
        past_instructions.append(idx)
        idx, accumulator = step(instructions, idx, accumulator)
    
    return accumulator

# Part 1
print('Part 1:', loop(instructions, part_one=True))

# Part 2
# Swap a single instruction and check if the loop closes
for swapped_idx in range(num_instructions):
    # Deepcopy to prevent bleedover from previous swaps
    instructions_swapped = deepcopy(instructions)

    # Swap instruction nop -> jmp or jmp -> nop
    if instructions_swapped[swapped_idx][:3] == 'nop':
        instructions_swapped[swapped_idx] = 'jmp' + instructions_swapped[swapped_idx][3:]
    elif instructions_swapped[swapped_idx][:3] == 'jmp':
        instructions_swapped[swapped_idx] = 'nop' + instructions_swapped[swapped_idx][3:]
    else:
        continue
    
    accumulator = loop(instructions_swapped)
    if accumulator:
        print('Part 2:', accumulator)
        break
