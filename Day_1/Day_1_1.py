with open('./input.txt') as inFile:
    s = set()
    for x in [int(_) for _ in inFile.read().split('\n')]:
        s.add(2020-x) if x not in s else print(x*(2020-x))