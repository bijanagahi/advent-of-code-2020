from Day_11_classes import Layout, Cell
import os

def main(rawInput):
    layout = Layout()
    layout.parseInput(rawInput)

    updatedCells = layout.tick(False)
    while updatedCells > 0:
        updatedCells = layout.tick(False)
        # Uncomment these lines if you want live updates
        # os.system('cls')
        # print(layout)
    print(layout.countUnoccupiedSeats())


if __name__ == '__main__':
    rawInput = open('./input.txt').read().splitlines()
    main(rawInput)