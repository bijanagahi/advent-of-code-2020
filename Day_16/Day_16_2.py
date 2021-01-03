from Day_16_helpers import parseInput
import math

def main(lines):
    rules, myTicket, tickets = parseInput(lines)
    print(rules)
    print(myTicket)
    print(tickets)
    print("********")
    fieldSets = [[] for i in range(len(tickets[0]))]

    for ticket in tickets:
        # print(f"Checking ticket: {ticket}")
        for fieldNum, value in enumerate(ticket):
            matchedRules = whichRules(value, rules)
            # print(f"FieldNum: {fieldNum} with ({value}) matches rules: {matchedRules}")
            if len(matchedRules) > 0:
                fieldSets[fieldNum].append(matchedRules)
    fieldSets = [field[0].intersection(*field) for field in fieldSets] # Collapse it

    # Iterate over the fieldSets:
    #   Lock in fields that only have one option and remove it from the other locations
    #   Repeat until all fields only have one option
    lockedFields = []
    while sum([0 if len(field) == 1 else 1 for field in fieldSets]) > 0:
        singles = [list(field)[0] for field in fieldSets if len(field) == 1]
        for single in singles:
            # remove that from the other fields
            for field in fieldSets:
                if single in field and len(field) > 1:
                    field.remove(single)
    mapper = {}
    for loc,field in enumerate(fieldSets):
        mapper[loc] = field.pop()
    print(mapper)
    # Now, looking at our ticket we find the 6 fields we're looking for
    targetFields = ['class']
    targetValues = []
    for loc, num in enumerate(myTicket):
        fieldName = mapper[loc]
        if 'departure' in fieldName:
            targetValues.append(num)
        # print(f"Loc: {loc} value: {num} is field {mapper[loc]}")
    print(math.prod(targetValues))

def whichRules(value, rules):
    matchedRules = set()
    for rule,ranges in rules.items():
        if value in ranges[0] or value in ranges[1]:
            matchedRules.add(rule)
    return matchedRules

if __name__ == "__main__":
    lines = open('./input.txt').read().splitlines()
    main(lines)