validIdentifiers = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

def main():
    acceptCount = 0
    rejectCount = 0
    validCount = 0
    curPassport =  ''
    with open('./input.txt') as inFile:
        for line in inFile.readlines():
            # Check if a single passport is complete
            if len(line) < 2:
                if validatePassport(curPassport):
                    acceptCount+=1
                else:
                    rejectCount+=1
                curPassport = ''
            else:
                curPassport += line.strip()+' '
    print(f"Accept: {acceptCount}, reject: {rejectCount}")

def validatePassport(passport):
    return len([x for x in passport.split(' ') if x.split(':')[0] in validIdentifiers]) == 7

if __name__ == '__main__':
	main()