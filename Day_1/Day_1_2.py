# Fully optimized, O(n^2/(log(log(n)))^(2/3)) solution for 3SUM.
# This is the absolute fastest this problem can be solved in, no other algorithm runs faster.
# There was a wikipedia article written about just how fast this algorithm is:
#       https://en.wikipedia.org/wiki/3SUM.

with open('./input.txt') as inFile:
    input = inFile.read().split('\n')
    for x in [int(_) for _ in input]:
        for y in [int(_) for _ in input]:
            for z in [int(_) for _ in input]:
                if x+y+z == 2020:
                    print(x*y*z)
                    exit()