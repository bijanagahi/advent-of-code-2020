from Day_20_classes import Tile, SimpleTile
from random import shuffle

def main(lines):
    tiles = parseSimpleTiles(lines)    
    cornerTileProduct = 1
    for tile in tiles:
        # Given a tile, for each side, check how many other tiles share that border
        sideMatches = {}
        for side,border in tile.borders.items():
            sideMatches[side.name] = 0
            for otherTile in tiles:
                if tile == otherTile:
                    continue
                if border in otherTile.allBorders:
                    sideMatches[side.name]+= 1#otherTile.id
        if len([x for x in sideMatches.values() if x == 0]) == 2:
            cornerTileProduct *= (int(tile.id))
    print(cornerTileProduct)
    exit()

def parseSimpleTiles(lines):
    tiles = []
    curTileId = 0
    curTileGrid = []
    for line in lines:
        if len(line) < 1:
            tiles.append(SimpleTile(curTileId, curTileGrid))
            curTileGrid = []
        elif 'Tile' in line:
            curTileId = line[5:-1]
        else:
            curTileGrid.append(line)
    tiles.append(SimpleTile(curTileId, curTileGrid))
    return tiles

if __name__ == '__main__':
    lines = open('./input.txt').read().splitlines()
    main(lines)