import re
from collections import Counter

# Load input data
with open('day06/input.txt', 'r') as file:
    responses = file.read()
responses = responses.split('\n\n')

# Part 1
# Remove extra (non-letter) characters
groups = [re.sub(r'[^a-z]', '', group) for group in responses]

# Count number of unique letters
num_questions = sum([len(''.join(set(group))) for group in groups])

print('Part 1:', num_questions)

# Part 2
num_questions = 0
for group in responses:
    # Count number of total people per group
    num_people = len(group.split('\n'))

    # Identify letters with frequency equal to number of people
    letter_counts = Counter(group)
    num_questions += sum([value == num_people for value in letter_counts.values()])

print('Part 2:', num_questions)
