expences = open('expence_report.txt', 'r').readlines()

target = 2020
seen = set()

"""
2 pointers to look at 2 lines at on time:
2 for loops that at the input seperatly
adding to a hash set at the end of the first for loop so that it can retreive number seen before up past 
"""

for line1 in expences:
    line_int1 = int(line1)
    
    for line2 in expences: 
        line_int2 = int(line2)
    
        if (target - line_int1 - line_int2) in seen:
            print(line_int1 * line_int2 * (target - line_int1 - line_int2))

    seen.add(line_int1)