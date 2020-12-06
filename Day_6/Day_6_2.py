inFile = open("./input.txt")
group = []
totalSum = 0
for line in inFile.read().splitlines():
    if len(line) <1:
        totalSum += len(group[0].intersection(*group))
        group = []
    else:
        group.append(set(line))
print(totalSum)