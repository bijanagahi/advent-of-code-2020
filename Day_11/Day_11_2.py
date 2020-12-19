from Day_11_classes import Layout, Cell
import os

def main(rawInput):
    layout = Layout()
    layout.parseInput(rawInput)

    updatedCells = layout.tick(True)
    while updatedCells > 0:
        updatedCells = layout.tick(True)
    print(layout.countUnoccupiedSeats())

if __name__ == '__main__':
    rawInput = open('./input.txt').read().splitlines()
    main(rawInput)