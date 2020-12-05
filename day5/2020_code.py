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

def tester(test, answer):
    TEST_ROW = parser('F','B', 128, test[:-3])
    TEST_SEAT = parser('L','R', 8, test[-3:])
    assert seatId(TEST_ROW, TEST_SEAT) == answer

tester('FBFBBFFRLR',357)
tester('BFFFBBFRRR',567)
tester('FFFBBBFRRR',119)
tester('BBFFBBFRLL',820)

print("yeet")