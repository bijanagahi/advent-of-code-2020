from enum import Enum

class SimpleTile(object):
    ''' Simple version of a Tile that only knows its borders'''
    def __init__(self, ID, lines):
        self.id = ID
        self.grid = [list(line) for line in lines]
        self.borders = self._calculateBorders()
        self.allBorders = self._calculateAllBorders()

    def getBorders(self):
        return self.borders

    def getAllBorders(self):
        return self.allBorders

    def _calculateBorders(self):
        return {
            Side.NORTH:self.grid[0],
            Side.SOUTH:self.grid[-1],
            Side.EAST:[x[-1] for x in self.grid],
            Side.WEST:[x[0] for x in self.grid]
            }

    def _calculateAllBorders(self):
        allBorders = []
        for border in self.borders.values():
            allBorders.append(border)
            allBorders.append(list(reversed(border)))
        return allBorders

class Tile(object):
    def __init__(self, ID, lines):
        self.id = int(ID)
        self.grid = [list(line) for line in lines]
        self.borders = self._calculateBorders()
        self.allBorders = self._calculateAllBorders()
        self.matches = {} # {SIDE:TILE}
        self.appliedTransforms = []

    def getBorders(self):
        return self.borders
    
    def getBorder(self, side):
        for b,s in self.borders.items():
            if s == side:
                return b

    def getAllBorders(self):
        return self.allBorders
    
    def getLines(self):
        return [''.join(row) for row in self.grid]

    def setMatches(self, matches):
        self.matches = matches

    def getNeighbor(self, side=None, otherTileId=None):
        if otherTileId:
            for side,tile in self.matches.items():
                if tile == otherTileId:
                    return side,otherTileId
        if side:
            return side,self.matches[side]
    
    def trim(self):
        newGrid = []
        for line in self.grid[1:-1]:
            newGrid.append(line[1:-1])
        self.grid = newGrid


    # Transform the tile, either rotating or flipping it.
    #
    # Once transformed, the tile's matching neighbors must also be updated,
    # as well as new borders calculated
    def transform(self, transformation):
        newMatches = {}
        if transformation == Transform.ROTATE_CW:
            self.rotateCW()
            for side,value in self.matches.items():
                newMatches[Side((side.value+1) %4)] = value
        elif transformation == Transform.ROTATE_CCW:
            self.rotateCCW()
            for side,value in self.matches.items():
                newMatches[Side((side.value-1) %4)] = value
        elif transformation == Transform.FLIP_H:
            self.flipH()
            for side,value in self.matches.items():
                if side == Side.EAST:
                    newMatches[Side.WEST] = value
                    continue
                if side == Side.WEST:
                    newMatches[Side.EAST] = value
                    continue
                newMatches[side] = value
        elif transformation == Transform.FLIP_V:
            self.flipV()
            for side,value in self.matches.items():
                if side == Side.NORTH:
                    newMatches[Side.SOUTH] = value
                    continue
                if side == Side.SOUTH:
                    newMatches[Side.NORTH] = value
                    continue
                newMatches[side] = value
        self.appliedTransforms.append(transformation)
        self.borders = self._calculateBorders()
        self.allBorders = self._calculateAllBorders()
        self.matches = newMatches

    def rotateCW(self):
        self.grid = list(zip(*self.grid[::-1]))
    def rotateCCW(self):
        self.grid = list(reversed(list(zip(*self.grid))))
    def flipV(self):
        self.grid = self.grid[::-1]
    def flipH(self):
        self.grid = [_[::-1] for _ in self.grid]
    
    def _calculateBorders(self):
        return {
            ''.join(self.grid[0]):Side.NORTH,
            ''.join(self.grid[-1]):Side.SOUTH,
            ''.join([x[-1] for x in self.grid]):Side.EAST,
            ''.join([x[0] for x in self.grid]):Side.WEST
            }

    def _calculateAllBorders(self):
        allBorders = []
        for border in self.borders.keys():
            allBorders.append(border)
            allBorders.append(border[::-1])
        return allBorders

    # Instance Functions
    def __str__(self):
        return str(self.id)+'\n'+'\n'.join(''.join(line) for line in self.grid)+'\n'

class Layout(object):
    def __init__(self, tiles):
        self.tiles = {}
        self.allTiles = tiles
        for tile in tiles:
            self.addTile(tile)
        self.cornerTiles = []
        self.edgeTiles = []
        self.innerTiles = []
        self.grid = []
    
    def addTile(self, tile):
        self.tiles[tile.id] = tile
    
    def getTile(self, tileId):
        return self.tiles[tileId]
    
    def populateMatches(self):
        for tile in self.tiles.values():
            sideMatches = {}
            for border,side in tile.borders.items():
                for otherTile in self.tiles.values():
                    # Skip itself.
                    if tile == otherTile:
                        continue
                    if border in otherTile.allBorders:
                        sideMatches[side] = otherTile.id
            tile.setMatches(sideMatches)
            if len(sideMatches) == 2:
                self.cornerTiles.append(tile)
            elif len(sideMatches) == 3:
                self.edgeTiles.append(tile)
            elif len(sideMatches) == 4:
                self.innerTiles.append(tile)
            else:
                raise ValueError # this shouldn't happen
    
    def createGrid(self):
        grid = []
        line = []
        topLeft, bottomRight = self.findDiagonals()
        # line.append(topLeft)
        curTile = topLeft
        lineStart = topLeft
        while not curTile == bottomRight:
            line.append(curTile)
            if Side.EAST not in curTile.matches:
                # if this tiles doesn't have an east match, it's the end of the line
                grid.append(line)
                line = []
                _,neighborId = lineStart.getNeighbor(side=Side.SOUTH, otherTileId=None)
                neighbor = self.getTile(neighborId)
                curTile = neighbor
                lineStart = neighbor
            else:
                _,neighborId = curTile.getNeighbor(side=Side.EAST, otherTileId=None)
                curTile = self.getTile(neighborId)
        #Now handle the last tile
        line.append(curTile)
        grid.append(line)
        self.grid = grid
    
    def printGrid(self):
        for line in self.grid:
            print([tile.id for tile in line])
            
            

    # Finds the tile in the top left corner.
    def findDiagonals(self):
        topLeft = None
        bottomRight = None
        for tile in self.tiles.values():
            if self.isCornerTile(tile):
                if Side.SOUTH in tile.matches and Side.EAST in tile.matches:
                    topLeft = tile
                if Side.NORTH in tile.matches and Side.WEST in tile.matches:
                    bottomRight = tile
        return topLeft, bottomRight

    def isCornerTile(self, tile):
        return True if tile in self.cornerTiles else False
    def isEdgeTile(self, tile):
        return True if tile in self.edgeTiles else False
    def isInnerTile(self, tile):
        return True if tile in self.innerTiles else False
    def isSeam(self, side, otherSide):
        return Side((side.value+2)%4) == otherSide

class Image(object):
    def __init__(self, grid):
        self.tileGrid = grid
        self.trimTiles()
        self.grid = self.merge()
    
    def createImage(self):
        self.trimTiles()

    def merge(self):
        lines = []
        totalLines = len(self.tileGrid) * len(self.tileGrid[0][0].grid)
        for i in range(totalLines):
            lines.append('')
        ctr = 0
        for tileRow in self.tileGrid:
            for i,tile in enumerate(tileRow):
                for row in tile.grid:
                    lines[ctr] += ''.join(row)
                    ctr+=1
                ctr -= 8
            ctr+=8
        return lines


    def trimTiles(self):
        for line in self.tileGrid:
            for tile in line:
                tile.trim()
    
    def __str__(self):
        return '\n'.join(self.grid)

class Side(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Transform(Enum):
    """
    Different transformations for the tile
    """
    ROTATE_CW = 1
    ROTATE_CCW = 2
    FLIP_V = 3
    FLIP_H = 4