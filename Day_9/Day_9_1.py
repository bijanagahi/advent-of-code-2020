def main(lines):
    lowBound = 0
    preambleLength = 25
    while lowBound+preambleLength < len(lines)-1:
        preamble = lines[lowBound:lowBound+preambleLength+1]
        if not twoSum(preamble,lines[lowBound+preambleLength+1]):
            print(lines[lowBound+preambleLength+1])
            exit()
        lowBound+=1

def twoSum(list, target):
    s = set()
    for num in list:
        if num not in s:
            s.add(target - num)
        else:
            return True
    return False

if __name__ == "__main__":
    lines = open("./input.txt").read().splitlines()
    main([int(x) for x in lines])