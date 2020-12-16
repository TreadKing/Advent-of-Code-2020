import re
file = open('day4.txt', 'r')

lines = file.readlines()
last = lines[-1]
passport = {}
validCount = 0
validCount1 = 0
passKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
# read in lines into a dictionary till you hit a new line or the last line(the last line is not a new line)
for line in lines:

    if line == '\n':
        # print(passport)
        # if all(key in passKeys for key in passport.keys()):
        #     print(True)
        keys = passport.keys()
        
        if (len(passport.keys()) == 7 and 'cid' not in passport) or (len(passport.keys()) == 8):
            # print(passport)
            validCount1 +=1
            if (
                (1920 <= int(passport['byr']) <= 2002) 
                and (2010 <= int(passport['iyr']) <= 2020) 
                and (2020 <= int(passport['eyr']) <= 2030)
                and (re.match('^[0-9]{9}', passport['pid']))
                and (re.match('^#[a-fA-F0-9]{6}', passport['hcl']))
                and (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
                and ((passport['hgt'][-2:] == 'in' and 59 <= int(passport['hgt'][:-2] <= 76)) 
                    or (passport['hgt'][-2:] == 'cm' and 150 <= int(passport['hgt'][:-2]) <= 196))):
                validCount += 1


        passport = {}

    elif line is last:
        line = line.strip('\n')
        passport.update(dict(item.split(':') for item in line.split(' ')))
       
        if (len(passport.keys()) == 7 and 'cid' not in passport) or (len(passport.keys()) == 8):
            validCount1 += 1
            if (1920 <= int(passport['byr']) <= 2002 
                and 2010 <= int(passport['iyr']) <= 2020 
                and re.match('^[0-9]{9}', passport['pid'])
                and re.match('^#[a-fA-F0-9]{6}', passport['hcl'])
                and passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                and ((passport['hgt'][-2:] == 'in' and 59 <= int(passport['hgt'][:-2] <= 76)) or (passport['hgt'][-2:] == 'cm' and 150 <= int(passport['hgt'][:-2]) <= 196))
            ):
                validCount += 1

        passport = {}

    else:
        line = line.strip('\n')
        # split up the string into a list of items with ' ' as the delimiter
        # then split each item into a list with ':' as the delimiter and have all of that as a dictionary
        passport.update(dict(item.split(':') for item in line.split(' ')))
print(validCount1)
print(validCount)