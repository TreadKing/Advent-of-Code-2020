slope = open('slope.txt', 'r')
slopeOut = open('slopeOut.txt', 'a')


position = 0
hits = 0
for line in slope:
    if line[position] == '\n':
        position = 0

    if line[position] == '#':
        hits += 1
        line = line[:position] + 'X' + line[position+1:]
 
    else:
        line = line[:position] + 'O' + line[position+1:]

    position += 3
    if position >= len(line):
        position -= len(line)
        position += 1

    slopeOut.write(line)

print('Trees Hsit: ' + str(hits))