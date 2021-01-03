from Day_17_classes import Layout, Cube

def main(rawInput):
    layout = Layout()
    layout.parseInput(rawInput)
    for i in range(1,7):
        print("Cycle:", i)
        layout.tick()
        print(layout.countActiveCubes())

if __name__ == '__main__':
    rawInput = open('./input.txt').read().splitlines()
    main(rawInput)