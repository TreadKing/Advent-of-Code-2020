import math
def findRow(ticket):

    highRows = 127
    lowRows = 0
    midRows = 0
    highCols = 7
    lowCols = 0
    midCols = 0
    for i in range(len(ticket)):
        if ticket[i] == 'F':
            highRows = highRows - int(highRows - lowRows + 1) /2

        elif ticket[i] == 'B':
            lowRows = lowRows + int(highRows - lowRows + 1) /2

        elif ticket[i] == 'L':
            highCols = highCols - int(highCols - lowCols + 1) /2
        
        elif ticket[i] == 'R':
            lowCols = lowCols + int(highCols - lowCols + 1) /2

    return ((lowRows)* 8) + lowCols

seatsIds = []
with open('seats.txt', 'r') as seats:
    max = 0
    for seat in seats:
        seatId = findRow(seat.strip())
        seatsIds.append(seatId)
        if seatId > max:
            max = seatId
    
    seatsIds.sort()
    # part 2
    print(set(range(seatsIds[0], seatsIds[len(seatsIds)-1]+1)) - set(seatsIds) )
    # part 1
    print(max)