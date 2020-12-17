file = open('day6.txt', 'r')
data = file.read()
forms = data.split('\n\n')

# part 1
count = 0
for form in forms:
    formSet = set(form)
    if '\n' in formSet:
        count += (len(formSet) - 1)
    else:
        count += len(formSet)

print(count)

# part 2
count2 = 0
for form in forms:
    answersList = []
    for answer in form.split('\n'):

        answersList.append(set(answer))

    count2 += len(set.intersection(*answersList))
print(count2)