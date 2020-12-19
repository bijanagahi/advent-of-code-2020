from Day_16_helpers import parseInput

def main(lines):
    rules, myTicket, tickets = parseInput(lines)
    # print(rules)
    # print(myTicket)
    # print(tickets)
    invalidNums = []
    for ticket in tickets:
        # print(f"Checking ticket: {ticket}")
        for value in ticket:
            # print(f"Check value: {value} has {checkRules(value, rules)} violations")
            if not checkRules(value, rules):
                invalidNums.append(value)
    print(sum(invalidNums))
def checkRules(value, rules):
    for rule in rules.values():
        if value in rule[0] or value in rule[1]:
            return True
    return False

if __name__ == "__main__":
    lines = open('./input.txt').read().splitlines()
    main(lines)