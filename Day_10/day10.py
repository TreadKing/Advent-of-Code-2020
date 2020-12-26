with open('day10.txt', 'r') as file:
    lines = file.read().split('\n')

for i in range(len(lines)):
    lines[i] = int(lines[i])

lines.sort()
lines.append(lines[-1] + 3)
lines.insert(0,0)

def findDiffs(list):
    diff1 = 0
    diff3 = 0
    
    for i in range(len(list)-1):
        if lines[i+1] - lines[i] == 1:
            diff1 += 1

        elif lines[i+1] - lines[i] == 3:
            diff3 += 1
    
    return diff1 * diff3

# part 1
print(findDiffs(lines))

from collections import defaultdict

counts = defaultdict(int, {0: 1})
for a in lines[1:]:
    counts[a] = counts[a -3] + counts[a - 2] + counts[a - 1]

print(counts[lines[-1]])