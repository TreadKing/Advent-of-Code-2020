import re

with open('day8.txt') as file:
    boot = file.read().split('\n')
file.close()

acc = 0
line = 0
lines_seen = {}

while line not in lines_seen:

    lines_seen[line] = boot[line]

    if boot[line][0:3] == 'acc':
        acc += int(boot[line][4:])
        line += 1

    elif boot[line][0:3] == 'jmp':
        line += int(boot[line][4:])

    else:
        line += 1

# part 1
print(acc)


# part 2

def testBoot(bootLines):

    accumulator = 0
    line = 0
    lines_seen = {}
    
    while line not in lines_seen and line < len(bootLines):

        lines_seen[line] = bootLines[line]

        if bootLines[line][0:3] == 'acc':
            accumulator += int(bootLines[line][4:])
            line += 1

        elif bootLines[line][0:3] == 'jmp':
            line += int(bootLines[line][4:])

        else:
            line += 1

    if line in lines_seen:
        return 0
    else:
        return accumulator


# testing line changes
for i, item in enumerate(boot):
    if item[0:3] == 'jmp':
        boot[i] = 'nop' + item[3:]
        output = testBoot(boot)
        if output !=  0: print(output)
        boot[i] = item
    
    if item[0:3] == 'nop':
        boot[i] = 'jmp' + item[3:]
        output = testBoot(boot)
        if output !=  0: print(output)
        boot[i] = item
    