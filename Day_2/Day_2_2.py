with open('./input.txt') as inFile:
    valid = 0
    for line in inFile.readlines():
        minPos = int(line.split('-')[0])-1
        maxPos = int(line.split('-')[1].split(' ')[0])-1
        target = line.split('-')[1].split(' ')[1][0]
        pw = line.split(' ')[-1][:-1] # drop the newline
        if pw[minPos] == target and pw[maxPos] != target:
            valid+=1
        if pw[minPos] != target and pw[maxPos] == target:
            valid+=1
    print(valid)