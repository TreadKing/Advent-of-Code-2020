passwords = open('passwords.txt', 'r')

def check_line(pass_line):

    string = pass_line[2]
    string = string[0:len(string)-1]

    low, high = pass_line[0].split('-')
    char = pass_line[1][0]

    low = int(low)
    high = int(high)

    if string[low-1] == char and string[high-1] != char:
        return True

    elif string[low-1] != char and string[high-1] == char:
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

print(valid)