file = open('test.txt', 'r')

lines = file.readlines()
last = lines[-1]
passport = {}
validCount = 0
passKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
# read in lines into a dictionary till you hit a new line or the last line(the last line is not a new line)
for line in lines:

    if line == '\n':
        print(passport)
        # if all(key in passKeys for key in passport.keys()):
        #     print(True)
        keys = passport.keys()
        if len(passport.keys()) == 7 and 'cid' not in passport:
            validCount += 1
            print(True)

        elif len(passport.keys()) == 8:
            validCount += 1
            print(True)

        else:
            print(False)
        passport = {}

    elif line is last:
        line = line.strip('\n')
        passport.update(dict(item.split(':') for item in line.split(' ')))
        print(passport)
        # if all(key in passKeys for key in passport.keys()):
        #     print(True)
        if len(passport.keys()) == 7 and 'cid' in passport:
            validCount += 1
            print(True)

        elif len(passport.keys()) == 8:
            validCount += 1
            print(True)
        
        else:
            print(False)
        passport = {}

    else:
        line = line.strip('\n')
        # split up the string into a list of items with ' ' as the delimiter
        # then split each item into a list with ':' as the delimiter and have all of that as a dictionary
        passport.update(dict(item.split(':') for item in line.split(' ')))

print(validCount)
        

