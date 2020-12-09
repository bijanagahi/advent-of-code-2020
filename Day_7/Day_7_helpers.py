from Day_7_Classes import Bag

def readInputFile(handler, getCounts):
    allBags = {}
    for line in handler.read().splitlines():
        parts = line.split(" bags contain ")
        rootBag = parts[0]
        if getCounts:
            subBags = getSubBagsAndCounts(parts[1])
        else:
            subBags = getSubBags(parts[1])
        # print(f"Root bag: {rootBag} | Subbags: {subBags}")
        allBags[rootBag] = subBags
    return allBags

# This is horrible
def getSubBags(line):
    subBags = []
    if "no other bags" in line:
        return subBags
    # Oh god it's so bad
    for part in line.replace(', ','').replace('bags','bag').split(' bag')[:-1]:
        subBags.append(part[2:])
    return subBags

# This is horrible
def getSubBagsAndCounts(line):
    subBags = []
    if "no other bags" in line:
        return subBags
    # Oh god it's so bad
    for part in line.replace(', ','').replace('bags','bag').split(' bag')[:-1]:
        subBags.append((part[2:],part[0]))
    return subBags