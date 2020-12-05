def main():
    with open('./input.txt') as inFile:
        # Drop half the inputs since any row starting with F will never be higher
        passes = [x.strip() for x in inFile.readlines() if x[0] == "B"]
        print(max([binMath(p[0:7],127)*8+binMath(p[7:],7) for p in passes]))

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