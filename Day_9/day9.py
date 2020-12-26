with open('day9.txt', 'r') as file:
    lines = file.read().split('\n')

def twoSum(start, stop, target):
    seen = set()
    target_int = int(lines[target])
    # print(target_int)
    for i in range(start, stop):
        line_int = int(lines[i])
        # print(line_int)
        if target_int - line_int in seen:
            return True
        seen.add(line_int)

    return False

print(twoSum(0, 25, 25))

min = 0
max = 25
# part 1
while max < len(lines):
    if twoSum(min, max, max) == False:
        print(lines[max])
    min += 1
    max += 1

