from enum import Enum

class Layout(object):
    """
    Manager class for all the cells
    """
    def __init__(self):
        self.grid = []
        self.cells = {}
    def parseInput(self, layout):
        for i,line in enumerate(layout):
            row = []
            for j,space in enumerate(line):
                cell = Cell(space, i, j)
                row.append(cell)
                self.cells[(i,j)] = cell 
            self.grid.append(row)
    
    def tick(self, LOS):
        updatedCells = 0
        for cell in self.cells.values():
            if not LOS:
                count = len(list(filter(lambda c: c.isOccupied(), self.getNeighbors(cell))))
            else:
                count = self.getNeighborsLOS(cell)
            updatedCells += 0 if cell.update(count) else 1
        for cell in self.cells.values():
            cell.saveState()
        return updatedCells
    
    def countUnoccupiedSeats(self):
        return len(list(filter(lambda c: c.isOccupied(), self.cells.values()))) 
    
    # This is where we deal with the boundary logic
    def getNeighbors(self, cell):
        neighbors = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if (self.isValidPos(cell.x + i, cell.y + j)):
                    neighbors.append(self.cells[(cell.x + i, cell.y + j)])
        return neighbors
    
    def getNeighborsLOS(self, cell):
        startPos = (cell.x,cell.y) # starting position
        occupiedSeats = 0
        # Check all the directions, count seats
        for d in Dir:
            if self.castRay(d,startPos):
                occupiedSeats += 1
        return occupiedSeats

    # Cast a ray from a point in a direction, returning true if it hits an occupied seat
    def castRay(self, direction, startingPos):
        nextPos = self.getNextLocation(direction, *startingPos)
        # Keep iterating until this loop breaks
        while self.isValidPos(*nextPos) and self.cells[nextPos].isFloor():
            nextPos = self.getNextLocation(direction, *nextPos)
        # We've cast the ray, now we check if we hit a wall or another seat
        if not self.isValidPos(*nextPos):
            return False # Did not encounter anything, hit the wall.
        elif self.cells[nextPos].isOccupied():
            return True
        else:
            return False


    def isValidPos(self, x, y):
        if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid[0]):
            return False
        return True
    
    def getNextLocation(self, d, x, y):
        return d.value[0]+x,d.value[1]+y

    def __str__(self):
        s = '**************\n'
        for row in self.grid:
            s+=''.join([str(c) for c in row])+'\n'
        return s+"**************" #get rid of the last newline
    

class Cell(object):
    """
    Single cell
    """
    def __init__(self, t, x, y):
        self.type = t
        self.x = x
        self.y = y
        self.nextState = t
    
    def getPos(self):
        return (self.x, self.y)
    
    def isOccupied(self):
        return True if self.type == '#' else False
    
    def isFloor(self):
        return True if self.type == '.' else False

    def update(self, count):
        self.nextState = self.type
        # Empty seats become occupied if count is 0
        if self.type == 'L' and count == 0:
            self.nextState = '#'
        # Occupied seats become empty if count >= 4
        if self.type == '#' and count >= 5:
            self.nextState = 'L'
        return self.nextState == self.type
    
    def saveState(self):
        self.type = self.nextState
    
    def __str__(self):
        return self.type

class Dir(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UPLEFT = (-1, -1)
    UPRIGHT = (-1, 1)
    DOWNLEFT = (1, -1)
    DOWNRIGHT = (1, 1)