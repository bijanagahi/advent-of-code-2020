import re

def main(lines):
    memory = {} 
    mask = ''
    for line in lines:
        if 'mask' in line:
            mask = line[7:]
        else:
            address, value = parseMemory(line)
            newValue = maskValue(mask, value)
            memory[address] = newValue
    print(sum([_ for _ in memory.values()]))

def createMask(line):
    pass

def parseMemory(line):
    address = re.search('[0-9]+',line)[0]
    value = int(re.search('\s[0-9]+',line)[0][1:])
    return address,value

def maskValue(mask, value):
    binValueStr = format(value, '036b')
    for loc,i in enumerate(mask):
        if i=='X':
            continue
        else:
            binValueStr = binValueStr[0:loc]+i+binValueStr[loc+1:]
    return int(binValueStr,2)



if __name__ == '__main__':
    lines = open('./input.txt').read().splitlines()

    main(lines)