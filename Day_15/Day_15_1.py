def main():
    nums = [2,0,6,12,1,3]
    seen = {}
    # turn = 0
    spoken = nums[-1] # last spoken number
    for i, num in enumerate(nums[:-1]):
        seen[num] = i+1
    for turn in range(len(nums)+1,30000001):
        if spoken not in seen:
            seen[spoken] = turn-1
            spoken = 0
        else:
            tmp = seen[spoken] # last time it was seen
            seen[spoken] = turn - 1 # update it to a more recent time
            spoken = turn-1 - tmp
        # print(f"Turn {turn} spoke [{spoken}]")
    print(spoken)
if __name__ == "__main__":
    main()