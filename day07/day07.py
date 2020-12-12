import re

# Load input data
with open('day07/input.txt', 'r') as f:
    rules = f.read().split('\n')

bag_hierarchy = {}
for rule in rules:
    root_bag = rule.split(' bags contain ')[0].strip()
    contains = rule.split(' bags contain ', maxsplit=1)[1]
    counts = [int(s) for s in rule.split() if s.isdigit()]
    contains = re.sub(r'( )?\d ', '', contains)
    contains = re.sub(r'bag(s)?', '', contains)
    contains = re.sub(r' \.', '', contains)
    contains = re.sub(' ,', ',', contains)
    contains = contains.split(',')
    bag_hierarchy[root_bag] = (contains, counts)


# Part 1
def bag_contains(bag_hierarchy, color_check, looking_for):
    if bag_hierarchy[color_check][0] == ['no other']:  # Reached bottom level
        return False
    elif color_check == looking_for:
        return True
    else:  # Search through nested bags
        return any([bag_contains(bag_hierarchy, color, looking_for) for color in bag_hierarchy[color_check][0]])

results = [{color: bag_contains(bag_hierarchy, color, 'shiny gold')}
           for color in bag_hierarchy.keys() if color != 'shiny gold']
print(sum([color_dict[key] for color_dict in results for key in color_dict.keys()]))


# Part 2
def count_subbags(bag_hierarchy, color):
    if bag_hierarchy[color][0] == ['no other']:  # Reached bottom level
        return 1
    else:  # Count number of nested bags
        subbags = [bag_hierarchy[color][1][i] * count_subbags(bag_hierarchy, bag_hierarchy[color][0][i])
                   for i in range(len(bag_hierarchy[color][0]))]
        return 1 + sum(subbags)

print(count_subbags(bag_hierarchy, 'shiny gold') - 1)  # -1 to exclude the root shiny gold bag itself
