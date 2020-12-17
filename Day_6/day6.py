file = open('day6.txt', 'r')
output = open('debug.txt', 'a')

data = file.read()
forms = data.split('\n\n')

count = 0
for form in forms:
    formSet = set(form)
    if '\n' in formSet:
        count += (len(formSet) - 1)
    else:
        count += len(formSet)

print(count)