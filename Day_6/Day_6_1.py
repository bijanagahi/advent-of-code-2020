inFile = open("./input.txt")
curSet = set()
totalSum = 0
for line in inFile.read().splitlines():
    if len(line) <1:
        totalSum += len(curSet)
        curSet = set()
    else:
        curSet.update(set(line))
print(totalSum)