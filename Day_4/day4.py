file = open('test.txt', 'r')

lines = file.readlines()
last = lines[-1]
passport = {}
# read in lines into a dictionary till you hit a new line or the last line(the last line is not a new line)
for line in lines:

    if line == '\n':
        print(passport)
        passport = {}
    elif line is last:
        print(passport)
    else:
        line = line.strip('\n')
        # split up the string into a list of items with ' ' as the delimiter
        # then split each item into a list with ':' as the delimiter and have all of that as a dictionary
        passport.update(dict(item.split(':') for item in line.split(' ')))
        

