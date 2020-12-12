rows = list(range(128))

testInput = 'BFFFBBFRRR'
actionRows = rows
for i in range(7):
    if testInput[i] == 'B':
        actionRows = actionRows[0:int(len(testInput)/2)+1]
    
    elif testInput[i] == 'F':
        actionRows = actionRows[int(len(testInput)/2)+1:-1]
    
print(actionRows)