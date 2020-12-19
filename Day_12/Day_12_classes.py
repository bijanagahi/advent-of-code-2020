from enum import Enum
# Object for part 2
class Ship2(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.pos = [0,0]
        self.facing = Dir.EAST
        self.dirs = [Dir.NORTH, Dir.EAST, Dir.SOUTH, Dir.WEST]
        self.waypoint = [10,1] # Waypoint starts 1 unit north, 10 units east

    def move(self, direction, amount):
        if direction == Dir.FORWARD:
            self.moveForward(amount)
        else:
            self.shiftWaypoint(direction, amount)
    
    
    # SHIFT the waypoint, relative to the ship. 
    def shiftWaypoint(self, direction, amount):
        # print(f"Moving waypoint {amount} units {direction.name}")
        if direction == Dir.NORTH:
           self.waypoint[1] += amount
        if direction == Dir.SOUTH:
            self.waypoint[1] -= amount
        if direction == Dir.EAST:
            self.waypoint[0] += amount
        if direction == Dir.WEST:
            self.waypoint[0] -= amount
    
    def shiftShip(self, direction, amount):
        # print(f"Moving ship {amount} units {direction.name}")
        if direction == Dir.NORTH:
           self.pos[1] += amount
        if direction == Dir.SOUTH:
            self.pos[1] -= amount
        if direction == Dir.EAST:
            self.pos[0] += amount
        if direction == Dir.WEST:
            self.pos[0] -= amount
    
    # Moving now involves scaling the current pos against the waypoint by an amount
    def moveForward(self, amount):
        x_axis = Dir.EAST if self.waypoint[0] >= 0 else Dir.WEST
        y_axis = Dir.NORTH if self.waypoint[1] >= 0 else Dir.SOUTH
        # print(f"Moving forward by {abs(amount*self.waypoint[0])}, {abs(amount*self.waypoint[1])}")
        self.shiftShip(x_axis, abs(amount*self.waypoint[0]))
        self.shiftShip(y_axis, abs(amount*self.waypoint[1]))
    
    '''
    Rotate the waypoint around the ship.
    General approach:
        - If clockwise (Dir.RIGHT):
            swap x and y, multiply y by -1
         - If counter-clockwise (Dir.LEFT):
            swap x and y, multiply x by -1
    '''
    def rotate(self, direction, amount):
        if direction == Dir.RIGHT: # Clockwise
            self.waypoint = [self.waypoint[1], self.waypoint[0]*-1]
        if direction == Dir.LEFT: # Counter-clockwise
            self.waypoint = [self.waypoint[1]*-1, self.waypoint[0]]
        # Now do it again if we need to
        if amount > 90:
            self.rotate(direction, amount-90)

    def getPos(self):
        return self.x, self.y

    def __str__(self):
        return f"Ship is at {self.pos}, waypoint is at {self.waypoint}. Distance is {abs(self.pos[0])+abs(self.pos[1])}"

class Ship(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = Dir.EAST
        self.dirs = [Dir.NORTH, Dir.EAST, Dir.SOUTH, Dir.WEST]
        self.waypoint = (1,10) # Waypoint starts 1 unit north, 10 units

    def move(self, direction, amount):
        if direction == Dir.FORWARD:
            self.moveForward(amount)
        else:
            self.shift(direction, amount)
    
    def moveWaypoint(self, direction, amount):
        if direction == Dir.FORWARD:
            self.moveForward(amount)
        else:
            self.shift(direction, amount)
    
    # SHIFT will update a single axis, regardless of the bearing of the ship
    def shift(self, direction, amount):
        if direction == Dir.NORTH:
           self.x += amount
        if direction == Dir.SOUTH:
            self.x -= amount
        if direction == Dir.EAST:
            self.y += amount
        if direction == Dir.WEST:
            self.y -= amount
    
    # Moving forward is the same as shifting in the direction the ship is facing
    def moveForward(self, amount):
        self.shift(self.facing, amount)
    
    # direction here refers to a LEFT or RIGHT rotation
    def rotate(self, direction, amount):
        # if direction == Dir.LEFT:
        #     # A left rotation is the same as 360-(amount) in the right.
        #     #   i.e. a 90 left is the same as a 270 right.
        if direction == Dir.RIGHT:
            if self.facing == Dir.WEST:
                self.facing = Dir.NORTH
            else:
                self.facing = self.dirs[self.dirs.index(self.facing)+1]
        if direction == Dir.LEFT:
            if self.facing == Dir.NORTH:
                self.facing = Dir.WEST
            else:
                self.facing = self.dirs[self.dirs.index(self.facing)-1]
        # Now do it again if we need to
        if amount > 90:
            self.rotate(direction, amount-90)

    def getPos(self):
        return self.x, self.y

    def __str__(self):
        return f"Ship is at [{self.x},{self.y}], facing {self.facing.name}. Distance is {abs(self.x)+abs(self.y)}"

class Dir(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    FORWARD = 5
    LEFT = 6
    RIGHT = 7

mapper = {
    "N":Dir.NORTH,
    "S":Dir.SOUTH,
    "E":Dir.EAST,
    "W":Dir.WEST,
    "F":Dir.FORWARD,
    "R":Dir.RIGHT,
    "L":Dir.LEFT
}