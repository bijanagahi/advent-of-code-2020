from math import prod
topo = []
col = 0
ctr = 0
numHit = [0]*5
with open('./input.txt') as inFile:
    for line in inFile.readlines():
        topo.append([_ for _ in line.strip()])
# Case 1: Right 1, down 1
for row in range(len(topo)):
    if(topo[row][col%31] == '#'):
        ctr+=1
    col+=1
numHit[0] = ctr
ctr = 0
col = 0

# Case 2: Right 3 down 1
for row in range(len(topo)):
    if(topo[row][col%31] == '#'):
        ctr+=1
    col+=3
numHit[1] = ctr
ctr = 0
col = 0

# Case 3: Right 5, down 1
for row in range(len(topo)):
    if(topo[row][col%31] == '#'):
        ctr+=1
    col+=5
numHit[2] = ctr
ctr = 0
col = 0

# Case 4: Right 7, down 1
for row in range(len(topo)):
    if(topo[row][col%31] == '#'):
        ctr+=1
    col+=7
numHit[3] = ctr
ctr = 0
col = 0

# Case 1: Right 1, down 2
for row in range(0,len(topo),2):
    if(topo[row][col%31] == '#'):
        ctr+=1
    col+=1
numHit[4] = ctr
ctr = 0
print(numHit)
print(prod(numHit))