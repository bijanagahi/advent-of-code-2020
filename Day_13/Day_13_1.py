def main(start, schedule):
    time = start
    while True:
        # print("Checking time: ", time)
        for bus in schedule:
            if time % bus == 0:
                print((time - start)*bus)
                exit()
        time+= 1

if __name__ == '__main__':
    rawInput = open('./input.txt').read().splitlines()
    start = int(rawInput[0])
    schedule = [int(x) for x in rawInput[1].split(',') if x != 'x']
    main(start, schedule)