passwords = open('passwords.txt', 'r')

def check_line(pass_line):
    pos1, pos2 = pass_line[0].split('-')
    #print(pass_line[1][0])

    pos1 = int(pos1)
    pos2 = int(pos2)

    print(pos1-1, pos2-1)

    print (pass_line[2][pos1-1] == pass_line[1][0] and pass_line[2][pos2-1] != pass_line[1][0])


    if (pass_line[2][pos1-1] == pass_line[1][0]) and (pass_line[2][pos2-1] != pass_line[1][0]):
        return True
    else: 
        return False

checks = []
for line in passwords:
    checks.append(check_line(line.split(' ')))

valid = 0
for item in checks:
    if item == True:
        valid+=1
    #print(item)
print(valid)
# print(checks[413-1])


