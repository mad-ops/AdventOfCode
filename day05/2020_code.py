import os
scriptdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(scriptdir,'2020_input.txt')) as seats:
    seatList = [x.strip() for x in seats.readlines()]

def halfer(flag, spread):
    if len(spread) == 2:
        return spread[flag]
    midpoint = int(len(spread)/2)
    if flag == 0:
        return spread[:midpoint]
    return spread[midpoint:]

def parser(l, h, spread, value):
    spread = list(range(spread))
    for flag in value:
        if flag == l:
            spread = halfer(0, spread)
        else:
            spread = halfer(1,spread)
    return spread

def seatId(row, column):
    return row * 8 + column

def returnSeatId(value):
    row = parser('F','B', 128, value[:-3])
    column = parser('L','R', 8, value[-3:])
    return seatId(row, column)

def tester(test, answer):
    assert returnSeatId(test) == answer

tester('FBFBBFFRLR',357)
tester('BFFFBBFRRR',567)
tester('FFFBBBFRRR',119)
tester('BBFFBBFRLL',820)

def p1(seatList):
    seatList = [returnSeatId(seat) for seat in seatList]
    return max(seatList)

def p2(seatList):
    seatList = [returnSeatId(seat) for seat in seatList] 
    seatList.sort()
    haystack = [x - seatList[i - 1] for i, x in enumerate(seatList)][1:]
    return seatList[haystack.index(2)] + 1

print(p1(seatList))
print(p2(seatList))