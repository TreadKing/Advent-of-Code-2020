expences = open('expence_report.txt', 'r')

target = 2020
seen = set()

"""
2 pointers to look at 2 lines at on time:
2 for loops that at the input seperatly
adding to a hash set at the end of the first for loop so that it can retreive number seen before up past 
"""
for line in expences:
    line_int = int(line)
    # print(line_int)
    if target - line_int in seen:
        print(line_int * (target - line_int))
    seen.add(line_int)