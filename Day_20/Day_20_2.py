from Day_20_classes import Tile, SimpleTile, Transform, Layout, Side, Image
# from Day_20_classes/Transform import ROTATE_CW, ROTATE_CCW, FLIP_H, FLIP_V
from random import shuffle
import re

''' Approach

- First, go through all the files and organize them based on whether they are
a corner piece, edge piece (not including corners), or inner piece. Also, keep
track of what tiles border eachother, regardless of orientation.
- Begin building out the puzzle:
- Add a random corner piece to the queue, then while the queue is not empty:
  - Pop a tile off the queue.
  - Add each bordering tiles to the queue to be proccessed.
  - Check its borders and matching tile, and rotate/flip the tile such that
    the borders align in NORTH/SOUTH and EAST/WEST pairs.
      - ex. corner tile shares NORTH border with another tile's WEST border:
         first rotate that tile until it's WEST border becomes SOUTH, then 
         determine if a flip is needed to align the borders. If a tile gets
         rotated, the side matches must also be updated to reflect the new sides
'''

def main(lines):
    tiles = parseTiles(lines)
    layout = Layout(tiles)

    # Find each tiles neighboring tile
    layout.populateMatches()
    
    queue = [] # holds tiles that need to be processed
    processed = [] # holds tiles that have already been processed
    # Add the first corner piece into the queue.
    queue.append(layout.cornerTiles[0])

    while queue:
        tile = queue.pop()        
        # Assumption here is that the tiles in the queue have already been oriented.
        # So we need to orient its neighbors (unless one of those has already been processed)
        for side, otherTileId in tile.matches.items():
            otherTile = layout.getTile(otherTileId)
            if otherTile in processed:
                continue
            # We want to check here if the other tile's side matches this one.
            otherTileMatchingSide, _ = otherTile.getNeighbor(side=None, otherTileId=tile.id)
            if not layout.isSeam(side, otherTileMatchingSide):
                # The seams don't match, so we need to rotate until they do.
                while not Side((side.value+2)%4) == otherTileMatchingSide:
                    otherTile.transform(Transform.ROTATE_CW)
                    otherTileMatchingSide = Side((otherTileMatchingSide.value+1) %4)
            
            # Now, compare the borders to determine if a flip needs to happen.
            if not tile.getBorder(side) == otherTile.getBorder(otherTileMatchingSide):
                # Borders don't match, need to flip.
                # Flip horizontal if we're reversing a NORTH/SOUTH side, vertical if EAST/WEST
                if side in [Side.NORTH, Side.SOUTH]:
                    otherTile.transform(Transform.FLIP_H)
                else:
                    otherTile.transform(Transform.FLIP_V)
            # We've handled orienting this tile correctly.
            # Now we add it to the queue so its neighbors can also be processed similarly.
            queue.append(otherTile)
        processed.append(tile)

    layout.createGrid()
    image = Image(layout.grid)
    # Now we have the flat image, let's turn it into a tile so we can transform it. 
    bigTile = Tile(0, image.grid)
    # Time to search for sea monsters!
    monstersFound = checkForMonsters(bigTile)
    if monstersFound == 0:
        for i in range(4):
            bigTile.transform(Transform.ROTATE_CW)
            if monstersFound:=checkForMonsters(bigTile):
                finishUp(bigTile, monstersFound)
        bigTile.transform(Transform.FLIP_H)
        if monstersFound:=checkForMonsters(bigTile):
            finishUp(bigTile, monstersFound)
        for i in range(4):
            bigTile.transform(Transform.ROTATE_CW)
            if monstersFound:=checkForMonsters(bigTile):
                finishUp(bigTile, monstersFound)
        bigTile.transform(Transform.FLIP_H)
        bigTile.transform(Transform.FLIP_V)
        if monstersFound:=checkForMonsters(bigTile):
            finishUp(bigTile, monstersFound)
        for i in range(4):
            bigTile.transform(Transform.ROTATE_CW)
            if monstersFound:=checkForMonsters(bigTile):
                finishUp(bigTile, monstersFound)
    

def checkForMonsters(bigTile):
    lines = bigTile.getLines()
    monstersFound = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if searchAround(lines,i, j):
                monstersFound+=1
    return monstersFound

def searchAround(lines, row, col):
    try:
        if lines[row+1][col-1] == '#' and lines[row+1][col-4] == '#' and lines[row+1][col-7] == '#' and lines[row+1][col-10] == '#' and lines[row+1][col-13] == '#' and lines[row+1][col-16] == '#':
            if lines[row][col-5] == '#' and lines[row][col-6] == '#' and lines[row][col-17] == '#' and lines[row][col-12] == '#' and lines[row][col-11] == '#':
                if lines[row-1][col+1] == '#':
                    return True
    except:
        return False

def finishUp(bigTile, found):
    numOctos = 0
    for line in bigTile.grid:
        numOctos += line.count('#')
    print(f"found {found} monsters")
    print(numOctos)
    print(numOctos - (found*15))
    print()
    
        




def parseTiles(lines):
    tiles = []
    curTileId = 0
    curTileGrid = []
    for line in lines:
        if len(line) < 1:
            tiles.append(Tile(curTileId, curTileGrid))
            curTileGrid = []
        elif 'Tile' in line:
            curTileId = line[5:-1]
        else:
            curTileGrid.append(line)
    tiles.append(Tile(curTileId, curTileGrid))
    return tiles

if __name__ == '__main__':
    lines = open('./input.txt').read().splitlines()
    main(lines)