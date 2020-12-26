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
    while max <= len(list):
        if twoSum(list, min, max, max) == False:
            return int(list[max])
        min += 1
        max += 1

invalid = findInvalid(lines)
print(invalid)


# part 2
def findWeakness(list, invalid):
    min = 0
    max = 1
    sum = int(list[min]) + int(list[max])
    while list[max] != invalid:
        
        if sum < invalid:
            max += 1
            sum += int(list[max])
        
        elif sum > invalid:
            sum -= int(list[min])
            min += 1

        elif sum == invalid:
            minValue = invalid
            maxValue = 0
            for i in range(min, max+1):
                if int(list[i]) >= maxValue:
                    maxValue = int(list[i])

                if int(list[i]) <= minValue:
                    minValue = int(list[i])
            
            return minValue + maxValue

    return 0

print(findWeakness(lines, invalid))