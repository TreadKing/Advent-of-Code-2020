with open('day9.txt', 'r') as file:
    lines = file.read().split('\n')

def twoSum(list, start, stop, target):
    seen = set()
    target_int = int(list[target])
    # print(target_int)
    for i in range(start, stop):
        line_int = int(list[i])
        # print(line_int)
        if target_int - line_int in seen:
            return True
        seen.add(line_int)

    return False


# part 1
def findInvalid(list):
    min = 0
    max = 25    
    while max < len(list):
        if twoSum(list, min, max, max) == False:
            return list[max]
        min += 1
        max += 1

print(findInvalid(lines))

#