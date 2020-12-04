topo = []
col = 0
ctr = 0
with open('./input.txt') as inFile:
    for line in inFile.readlines():
        topo.append([_ for _ in line.strip()])

for row in range(len(topo)):
    if(topo[row][col%31] == '#'):
        ctr+=1
    col+=3
print(ctr)