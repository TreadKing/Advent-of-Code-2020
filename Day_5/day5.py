def findRow(ticket):
    highRows = 127
    lowRows = 0
    midRows = 0
    highCols = 7
    lowCols = 0
    midCols = 0
    for i in range(len(ticket)):

        midRows = (highRows + lowRows) // 2
        midCols = (highCols + lowCols) // 2
        if ticket[i] == 'F':
            highRows = midRows - 1

        elif ticket[i] == 'B':
            lowRows = midRows + 1

        elif ticket[i] == 'L':
            highCols = midCols - 1
        
        elif ticket[i] == 'R':
            lowCols = midCols + 1

    return ((midRows + 1 )* 8) + midCols

with open('seats.txt', 'r') as seats:
    max = 0
    for seat in seats:
        seatId = findRow(seat.strip())
        if seatId > max:
            max = seatId

    print(max)