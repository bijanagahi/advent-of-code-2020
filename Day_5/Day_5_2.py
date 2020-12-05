def main():
    with open('./input.txt') as inFile:
        passes = [x.strip() for x in inFile.readlines()]
        print(set([binMath(p[0:7],127)*8+binMath(p[7:],7) for p in passes]).symmetric_difference(range(80,927)))
        
def binMath(p, high):
    upper = high
    lower = 0    
    for i,letter in enumerate(p):
        if letter == 'F' or letter == 'L':
            upper -= 2**(len(p)-1-i)
        else:
            lower += 2**(len(p)-1-i)
    if lower != upper:
        raise ValueError
    return lower

if __name__ == "__main__":
    main()