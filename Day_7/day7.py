import re
with open('day7.txt', 'r') as file:
    lines = [re.sub(' bags?|\.', '', line) for line in file.read().split('\n')]
print(lines)
rules = {}
for line in lines:
    line = re.split(' contain |, ', line)

    bagsLst = []
    for item in line[1:]:
        print(item)
        if item == 'no other':
            bagsLst.append([0, item])
            
        else:
            bagsLst.append([int(item[0]), item[2:]])

    
    rules[line[0]] = bagsLst

print(rules)
gold_count = 0

def hasGold(color):
    if color == 'shiny gold':
        return True

    elif color == 'no other':
        return False
    
    else:
        return any(hasGold(c) for b, c in rules[color])

for color in rules:
    if hasGold(color):
        gold_count += 1
# part 1
print(gold_count -1)


def countBags(bag_color):
    if bag_color == 'no other':
        return 0
    else:
        return 1 + sum(int(num) * countBags(color) for num, color, in rules[bag_color])
# part 2
print(countBags('shiny gold')-1)

