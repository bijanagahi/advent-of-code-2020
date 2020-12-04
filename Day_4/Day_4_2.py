import re 
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
    # once more...with feeling!
    if validatePassport(curPassport):
        acceptCount+=1
    else:
        rejectCount+=1
    print(f"Accept: {acceptCount}, reject: {rejectCount}")




def validatePassport(passport):
    numValidFields = 0
    # Crap logic ahead, honestly just ignore this day, it's FUBAR.
    for key,value in [(x.split(":")[0],x.split(":")[1]) for x in passport.split(' ')[:-1]]:
        # Please forgive me
        try:
            if key=="byr":
                if int(value) >= 1920 and int(value) <= 2002:
                    numValidFields+=1
            elif key=="iyr":
                if int(value) >= 2010 and int(value) <= 2020:
                    numValidFields+=1
            elif key=="eyr":
                if int(value) >= 2020 and int(value) <= 2030:
                    numValidFields+=1
            elif key=="hgt":
                val = re.search("[0-9]+",value)[0]
                if value[-1] == "n":
                    if int(val) >= 59 and int(val) <= 76:
                        numValidFields+=1
                elif value[-1] == "m":
                    if int(val) >= 150 and int(val) <= 193:
                        numValidFields+=1
            elif key=="hcl":
                if re.search("#[0-9a-f]{6}",value)[0]:
                    numValidFields+=1
            elif key=="ecl":
                if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    numValidFields+=1
            elif key=="pid":
                if re.search("[0-9]{9}",value)[0]:
                    numValidFields+=1
        except TypeError:
            continue
    return numValidFields == 7

if __name__ == '__main__':
	main()