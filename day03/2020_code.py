import os

# look mah, im a straight line
# flipping along x
# y = 3x
scriptdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(scriptdir,'2020_input.txt')) as slopes:
    track = [x.strip() for x in slopes.readlines()]

def ski(track, m):
    count, tree, width = 0, 0, None
    for row in track[1:]:
        count += 1
        if width is None:
            width = len(row)
        track = row.strip() * (1 + int(m*count/width))
        tree += 1 if track[count*m] == '#' else 0
    return tree

if __name__ == "__main__":
    tree = lambda x: ski(track,x)
    print(tree(3))
    #ooh this is cool, we just rip out all the tracks we're skipping
    #over and process it as the same as the first run asked for
    print( tree(1) * tree(3) * tree(5) * tree(7) * ski(track[::2], 1))