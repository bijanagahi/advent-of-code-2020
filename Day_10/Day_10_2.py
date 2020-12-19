def main(lines):
    runningTotals = {lines[0]:1}
    for jolt in lines[1:]: # Assume there's only 1 way to get the first two
        tempTotal = 0
        # Check how many ways there are to get to here from the previous 3
        for prev in range(1,4):
            if jolt-prev in runningTotals:
                tempTotal += runningTotals[jolt-prev]
        runningTotals[jolt] = tempTotal
    print(runningTotals[lines[-1]])
    for key,value in runningTotals.items():
        print(f"[{key}]: {value}")

if __name__ == '__main__':
    lines = open('./input1.txt').read().splitlines()
    lines.append(0)
    main(sorted([int(_) for _ in lines]))