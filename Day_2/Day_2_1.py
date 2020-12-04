with open('./input.txt') as inFile:
    valid = 0
    for line in inFile.readlines():
        minLen = line.split('-')[0]
        maxLen = line.split('-')[1].split(' ')[0]
        target = line.split('-')[1].split(' ')[1][0]
        pw = line.split(' ')[-1][:-1] # drop the newline
        count = 0
        for char in pw:
            if char == target:
                count+=1
        print(f"Min: {minLen}, Max: {maxLen}, target: {target}, pw: {pw}, count: {count}")
        if count >= int(minLen) and count <= int(maxLen):
            valid+=1
    print(valid)
