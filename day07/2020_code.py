import re
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
lookup = dict()
for line in TEST_INPUT.split('\n'):
    parsed = line.split('contain')
    key = ' '.join(parsed[0].split(' ')[:2])
    for x in parsed[1].split(','):
        quant, qual = bagStripper.search(x).group(1,2)
        if key not in lookup:
            lookup[key] = list()
        lookup[key].append((quant, qual))

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

assert bagAudit('shiny gold') == 4