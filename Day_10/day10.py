with open('day10.txt', 'r') as file:
    lines = file.read().split('\n')

for i in range(len(lines)):
    lines[i] = int(lines[i])

def findDiffs(list):
    diff1 = 0
    diff3 = 1
    list.sort()
    if list[0] - 0 == 1:
        diff1 += 1
    elif list[0] - 0 == 3:
        diff3 += 3
    for i in range(len(list)-1):
        if lines[i+1] - lines[i] == 1:
            diff1 += 1

        elif lines[i+1] - lines[i] == 3:
            diff3 += 1
    
    return diff1 * diff3


print(findDiffs(lines))