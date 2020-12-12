import re
from collections import Counter

# Load input data
with open('day06/input.txt', 'r') as f:
    responses = f.read()
responses = responses.split('\n\n')


# Part 1
num_questions = 0
for group in responses:
    # Remove extra (non-letter) characters
    group = re.sub(r'[^a-z]', '', group)

    # Count number of unique letters
    num_questions += len(''.join(set(group)))
print(num_questions)


# Part 2
num_questions = 0
for group in responses:
    # Count number of total people per group
    num_people = len(group.split('\n'))

    # Identify letters with frequency equal to number of people
    letter_counts = Counter(group)
    for key, value in letter_counts.items():
        if value == num_people:
            num_questions += 1
print(num_questions)
