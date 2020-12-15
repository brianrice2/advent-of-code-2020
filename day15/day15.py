from collections import defaultdict

inlist = [16,1,0,18,12,14,19]

# In general: track the last two times a number's been said
# Starting round of saying each input number
indict = {}
for i in range(len(inlist)):
    indict[inlist[i]] = i + 1, None  
last2turns = defaultdict(lambda: (None, None), indict)

# Perform next turn automatically (always equals 0)
most_recent = 0
last2turns[most_recent] = (len(inlist) + 1, indict[most_recent][0]) if 0 in last2turns else (len(inlist) + 1, None)

# Perform all turns thereafter
stop = 30000000  # Use stop = 2020 for Part 1
for turn in range(len(inlist) + 2, stop + 1):
    if not last2turns[most_recent][1]:  # last time was 1st time
        age = most_recent = 0
    else:
        age = turn - last2turns[most_recent][1] - 1
    if turn == stop:
        print('Turn ', turn, ': ', age, sep='')
    last2turns[age] = turn, last2turns[age][0]
    most_recent = age
