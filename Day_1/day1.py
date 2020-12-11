expences = open('expence_report.txt', 'r')

target = 2020
seen = set()
for line in expences:
    line_int = int(line)
    # print(line_int)
    if target - line_int in seen:
        print(line_int * (target - line_int))
    seen.add(line_int)