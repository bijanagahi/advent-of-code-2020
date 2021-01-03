from Day_17_classes import Hyperspace, Hypercube

def main(rawInput):
    hyperspace = Hyperspace()
    hyperspace.parseInput(rawInput)
    for i in range(1,7):
        print("Cycle:", i)
        hyperspace.tick()
        print(hyperspace.countActiveCubes())

if __name__ == '__main__':
    rawInput = open('./input.txt').read().splitlines()
    main(rawInput)