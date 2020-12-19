from Day_12_classes import Ship, Dir, mapper


def main(instructions):
    ship = Ship()
    print(ship)
    for line in instructions:
        if line[0] == Dir.RIGHT or line[0] == Dir.LEFT:
            ship.rotate(*line)
        else:
            ship.move(*line)
    print(ship)

if __name__ == '__main__':
    rawInput = open('./input.txt').read().splitlines()
    instructions = []
    for line in rawInput:
        direction = mapper[line[0]]
        amount = int(line[1:])
        instructions.append((direction, amount))
    main(instructions)
