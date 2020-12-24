import numpy as np

# Load input data
with open('day16/input.txt', 'r') as file:
    inlist = file.read().split('\n\n')

rules, ticket, nearby = inlist
rules = rules.strip().split('\n')
ticket = list(map(int, ticket.split('\n')[1].split(',')))
nearby = [list(map(int, tkt.split(','))) for tkt in nearby.strip().split('\n')[1:]]

# Helper functions
def inrange(fieldname, testvalue):
    for tup in rulesdict[fieldname]:
        lo, hi = tup
        if testvalue >= lo and testvalue <= hi:
            return True
    return False

def check_all_classes(testvalue):
    for field in rulesdict.keys():
        if inrange(field, testvalue):
            return True
    return False

def get_possible_fields(testvalue):
    fields = set()
    for field in rulesdict.keys():
        if inrange(field, testvalue):
            fields.add(field)
    return fields


# Part 1
# Keep track of valid ranges for each rule/field name
rulesdict = {}
for rule in rules:
    field, limit = rule.split(': ')
    limit = limit.split(' or ')
    ranges = []
    for rng in limit:
        lo_hi = tuple(map(int, rng.split('-')))
        ranges.append(lo_hi)
    rulesdict[field] = ranges

# Based on valid ranges, identify which tickets are valid and invalid
invalid = []
valid = []
for tkt in nearby:
    valid_tkt = True
    for num in tkt:
        isvalid = check_all_classes(num)
        if not isvalid:
            invalid.append(num)
            valid_tkt = False
        
    if valid_tkt:
        valid.append(tkt)

print('Part 1:', sum(invalid))


# Part 2
# Start off with every field as an option
possible_fields = {}
for i in range(len(ticket)):
    possible_fields[i] = set(rulesdict.keys())

for tkt in valid:
    # Narrow down set of possible fields through set intersection
    for idx in range(len(tkt)):
        num = tkt[idx]
        possible_fields[idx] &= get_possible_fields(num)

# Pare down possible fields to just one final field
# Keep going until we've found exactly one field for every index
final_fields = {}
while len(tuple(final_fields.keys())) < len(ticket):
    # Find indexes with only one possible field
    # There must be at least one at the start for there to be a unique solution
    for idx, field_set in possible_fields.items():
        if len(field_set) == 1:
            # Add that index/field to the final listing
            field_name = tuple(field_set)[0]
            final_fields[idx] = field_name

            # Remove that field from all other possibilities
            # Use discard(), not remove(), in case the field is not present
            for field_set in possible_fields.values():
                field_set.discard(field_name)

departures = []
for idx in range(len(ticket)):
    field_name = final_fields[idx]
    if field_name.startswith('departure'):
        departures.append(ticket[idx])

print('Part 2:', np.prod(departures))
