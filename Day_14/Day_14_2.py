import re

def main(lines):
    memory = {}
    mask = ''
    for line in lines:
        if 'mask' in line:
            mask = line[7:]
        else:
            address, value = parseMemory(line)
            maskedAddress= maskAddress(mask, address)
            allAddresses = getAllAddresses(maskedAddress)
            for address in allAddresses:
                memory[address] = value 
    print(sum([_ for _ in memory.values()]))

def parseMemory(line):
    address = int(re.search(r'[0-9]+',line)[0])
    value = int(re.search(r'\s[0-9]+',line)[0][1:])
    return address,value

def maskAddress(mask, address):
    binAddressStr = format(address, '036b')
    for loc,i in enumerate(mask):
        if i=='0':
            continue
        else:
            binAddressStr = binAddressStr[0:loc]+i+binAddressStr[loc+1:]
    return binAddressStr
    #return int(binValueStr,2)

def getAllAddresses(maskedAddress):
    addresses = [] # keeps all the addresses
    numXs = maskedAddress.count('X') # Count how many addresses we're going to create
    bins = [format(x, f'0{numXs}b') for x in range(2**numXs)] # generate all the binary combinations
    # Now, iterate over the possible combinations, and overwrite each X in the original string
    for combo in bins:
        itr = 0
        address = maskedAddress
        for loc,i in enumerate(maskedAddress):
            if i=='X':
                address = address[0:loc] + combo[itr] + address[loc+1:]
                itr += 1
            else:
                continue
        addresses.append(int(address,2))
    return addresses




if __name__ == '__main__':
    lines = open('./input.txt').read().splitlines()

    main(lines)