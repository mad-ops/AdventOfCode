import os

def parser(data):
    return [x.replace("\n", "") for x in data.split("\n\n")]

def parseGranular(data):
    return [x.split() for x in data.split("\n\n")]

scriptdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(scriptdir,'2020_input.txt')) as raw:
    rawData = raw.read()

TEST_INPUT = '''abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb'''

def uniqueCount(value):
    return len(set(value))

TEST_DATA = parser(TEST_INPUT)
data = parser(rawData)
assert sum([uniqueCount(x) for x in TEST_DATA]) == 11
print( sum([uniqueCount(x) for x in data]) )

#part 2
# This is pretty straight forward, we need to redine the parser
# to work make it so that we don't lose individual information.
# After that we stay in set land and use intersection as like ]
# an aggregation function.
def processor(group):
    validAnswer = set(group[0])
    for passenger in group[1:]:
        validAnswer = validAnswer.intersection(set(passenger))
    return uniqueCount(validAnswer)

def looper(data):
    return sum([processor(x) for x in data])

TEST_DATA = parseGranular(TEST_INPUT)
data = parseGranular(rawData)
assert looper(TEST_DATA) == 6
print( looper(data) )