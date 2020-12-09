def main(lines):
    low = 0
    high = 1
    target = 258585477 # Answer from previous part, yours will be different
    curSum = lines[low]
    while high < len(lines):
        while curSum > target and low < high-1:
            curSum = curSum - lines[low]
            low+=1
        if curSum == target:
            print(low,high)
            print(min(lines[low:high])+max(lines[low:high]))
            exit()
        curSum = curSum + lines[high]
        high+=1
    print("Failed")

if __name__ == "__main__":
    lines = open("./input.txt").read().splitlines()
    print(lines)
    main([int(x) for x in lines])