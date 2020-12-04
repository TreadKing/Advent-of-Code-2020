slope = open('slope.txt', 'r')
slopeOut = open('slopeOut.txt', 'a')


position = 0
hits = 0
# for line in slope:
#     if line[position] == '\n':
#         position = 0

#     if line[position] == '#':
#         hits += 1
#         line = line[:position] + 'X' + line[position+1:]
 
#     else:
#         line = line[:position] + 'O' + line[position+1:]

#     position += 7
#     if position >= len(line):
#         position -= len(line)
#         position += 1

#     slopeOut.write(line)

count = 0
for line in slope:
    if count % 2 == 0:

        if line[position] == '\n':
            position = 0

        if line[position] == '#':
            hits += 1
            line = line[:position] + 'X' + line[position+1:]
    
        else:
            line = line[:position] + 'O' + line[position+1:]

        position += 1
        if position >= len(line):
            position -= len(line)
            position += 1

    slopeOut.write(line)
    count += 1

print('Trees Hit: ' + str(hits))