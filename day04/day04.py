import re

# Load input data
with open('day04/input.txt', 'r') as f:
    passports = f.read()

# Split into separate passports using empty line delimiter
passports = [re.sub('\n', ' ', passport) for passport in passports.split('\n\n')]

expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

# Part 1
def is_valid_dict(passport_dictionary):
    keys = set(passport_dictionary.keys())
    return ((keys == set(expected_fields)) or
            (keys == set([x for x in expected_fields if x != 'cid'])))

valid_passport_count = 0
for passport in passports:
    # Parse into dictionary
    passport_dictionary = dict(re.findall(r'(\w+):([^\ ]+)', passport))
    # Check validity
    valid_passport_count += int(is_valid_dict(passport_dictionary))

print('Part 1:', valid_passport_count)

# Part 2
def is_valid_dict(passport_dictionary):
    keys = set(passport_dictionary.keys())

    # Check for correct fields, as in Part 1
    if not ((keys == set(expected_fields)) or
         (keys == set([x for x in expected_fields if x != 'cid']))):
            return False
    
    # Check individual field requirements
    byr_val = passport_dictionary['byr']
    if (len(byr_val) != 4) or (int(byr_val) < 1920) or (int(byr_val) > 2002):
        return False
    
    iyr_val = passport_dictionary['iyr']
    if (len(iyr_val) != 4) or (int(iyr_val) < 2010) or (int(iyr_val) > 2020):
        return False

    eyr_val = passport_dictionary['eyr']
    if (len(eyr_val) != 4) or (int(eyr_val) < 2020) or (int(eyr_val) > 2030):
        return False
    
    hgt_val = passport_dictionary['hgt']
    units = hgt_val[-2:]
    if units != 'cm' and units != 'in':
        return False
    else:
        height = int(hgt_val[:-2])
        if (units == 'cm') and ((height < 150) or (height > 193)):
            return False
        elif (units == 'in') and ((height < 59) or (height > 76)):
            return False

    hcl_val = passport_dictionary['hcl']
    if not re.match(r'#[0-9a-f]{6}', hcl_val):
        return False

    ecl_val = passport_dictionary['ecl']
    if ecl_val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    pid_val = passport_dictionary['pid']
    if len(pid_val) != 9:
        return False
    
    return True

valid_passport_count = 0
for passport in passports:
    # Parse into dictionary
    passport_dictionary = dict(re.findall(r'(\w+):([^\ ]+)', passport))
    # Check validity
    valid_passport_count += int(is_valid_dict(passport_dictionary))

print('Part 2:', valid_passport_count)
