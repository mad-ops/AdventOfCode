import re
import os

scriptdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(scriptdir,'2020_input.txt')) as raw:
    rawData = raw.read()

TEST_INPUT = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

bagStripper = re.compile('''(\d|no) (.*) bag.?s?''')
def create_lookup(data):
    lookup = dict()
    for line in data.split('\n'):
        parsed = line.split('contain')
        key = ' '.join(parsed[0].split(' ')[:2])
        for x in parsed[1].split(','):
            quant, qual = bagStripper.search(x).group(1,2)
            if key not in lookup:
                lookup[key] = list()
            lookup[key].append((quant, qual))
    return lookup

def bagFinder(type):
    containingBags = set()
    for key in lookup:
        for bag in lookup[key]:
            if type == bag[1]:
               qual = ' '.join(key.split(' ')[:2])
               containingBags.add(qual)
    return containingBags

def bagAudit(type):
    processedBags = set()
    unProcessedBags = set()
    unProcessedBags.add(type)
    while len(unProcessedBags) != 0:
        queued = unProcessedBags.pop()
        hits = bagFinder(queued)
        unProcessedBags = unProcessedBags | hits
        processedBags = processedBags | hits
    return len(processedBags)

lookup = create_lookup(TEST_INPUT)
assert bagAudit('shiny gold') == 4

#p1
lookup = create_lookup(rawData)
print(bagAudit('shiny gold'))

#p2
TEST_INPUT = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''

def bagCounter(type):
    containingBags = 0
    for bag in lookup[type]:
        quant, qual = bag
        if quant == 'no':
            # print (type, bag, containingBags)
            return 1
        containingBags += int(quant) * bagCounter(qual)
        # print(type, bag, containingBags)

    if type == 'shiny gold':
        return containingBags
    return containingBags + 1

lookup = create_lookup(TEST_INPUT)
assert bagCounter('shiny gold') == 126


lookup = create_lookup(rawData)
print(bagCounter('shiny gold'))