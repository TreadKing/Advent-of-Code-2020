passwords = open('passwords.txt', 'r')

def check_line(pass_line):
    count = 0

    limit = pass_line[0].split('-')
    for char in pass_line[2]:
        if char == pass_line[1][0]:
            count += 1
    
    if count <= int(limit[1]) and count >= int(limit[0]):
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

