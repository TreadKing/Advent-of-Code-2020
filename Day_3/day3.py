slope = open('slope.txt', 'r')
# slopeOut = open('slopeOut.txt', 'a')

position1 = 0
position2 = 0
position3 = 0
position4 = 0
position5 = 0
hits1 = 0
hits2 = 0
hits3 = 0
hits4 = 0
hits5 = 0
count = 0

for line in slope:
    if line[position1] == '\n':
        position1 = 0

    if line[position2] == '\n':
        position2 = 0

    if line[position3] == '\n':
        position3 = 0

    if line[position4] == '\n':
        position4 = 0


    if line[position1] == '#':
        hits1 += 1

    if line[position2] == '#':
        hits2 += 1

    if line[position3] == '#':
        hits3 += 1

    if line[position4] == '#':
        hits4 += 1
        # line = line[:position] + 'X' + line[position+1:]
 
    # else:
    #     line = line[:position] + 'O' + line[position+1:]


    position1 += 1
    position2 += 3
    position3 += 5
    position4 += 7

    if position1 >= len(line):
        position1 -= len(line)
        position1 += 1

    if position2 >= len(line):
        position2 -= len(line)
        position2 += 1

    if position3 >= len(line):
        position3 -= len(line)
        position3 += 1

    if position4 >= len(line):
        position4 -= len(line)
        position4 += 1


    if count % 2 == 0:

        if line[position5] == '\n':
            position5 = 0

        if line[position5] == '#':
            hits5 += 1

        position5 += 1
        if position5 >= len(line):
            position5 -= len(line)
            position5 += 1

    # slopeOut.write(line)
    count += 1

print('Trees Hit 1: ' + str(hits1))
print('Trees Hit 2: ' + str(hits2))
print('Trees Hit 3: ' + str(hits3))
print('Trees Hit 4: ' + str(hits4))
print('Trees Hit 5: ' + str(hits5))

print('Total Trees hit: ' + str(hits1 * hits2 * hits3 * hits4 * hits5))
