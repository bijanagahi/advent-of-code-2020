import re

def createRule(line):
    # Line looks like: class: 1-3 or 5-7
    name = re.search(r'^.*:', line)[0]
    parsedRanges = re.findall(r'[0-9]+-[0-9]+', line) # There's always two ranges
    ranges = []
    for r in parsedRanges:
        interval = [int(x) for x in r.split('-')]
        ranges.append(range(interval[0], interval[1]+1))
    return name, ranges

def parseInput(lines):
    rules = {}
    myTicket = []
    tickets = []
    for i,line in enumerate(lines):
        if len(line) < 1:
            continue
        if 'your ticket' in line:
            myTicket = [int(x) for x in lines[i+1].split(',')]
            tickets = [[int(x) for x in line.split(',')] for line in lines[i+4:]] # guess this works!?
            break
        name, ranges = createRule(line)
        rules[name] = ranges
    return rules,myTicket,tickets
