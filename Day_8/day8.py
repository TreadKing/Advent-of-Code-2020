import re

with open('day8.txt') as file:
    boot = file.read().split('\n')
file.close()

acc = 0
line = 0
overlap = False
lines_seen = {}

while line not in lines_seen:

    lines_seen[line] = boot[line]

    if boot[line][0:3] == 'acc':
        acc += int(boot[line][4:])
        line += 1
        print(line)

    elif boot[line][0:3] == 'jmp':
        line += int(boot[line][4:])
        print(line)
    
    else:
        line += 1
        print(line)

print(acc)