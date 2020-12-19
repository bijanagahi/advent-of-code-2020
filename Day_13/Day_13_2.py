from Day_13_helpers import multipleGenerator

def main(schedule):
    elements = []
    for i,bus in enumerate(schedule):
        if bus > 1:
            elements.append((bus-i,bus))
    print(elements)
    # Throw this into a CRT calculator...I'm not gonna implement it. Sorry.

    
        

if __name__ == '__main__':
    rawInput = open('./input.txt').read().splitlines()
    schedule = [int(x) for x in rawInput[1].replace('x','1').split(',') if x != 'x']
    main(schedule)