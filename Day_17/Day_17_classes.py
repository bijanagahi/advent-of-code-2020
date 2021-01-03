from enum import Enum
from Day_17_enums import State

class Layout(object):
    """
    Manager class for all the cubes

    - This layout is infinite in all directions, so anytime something is OOB, it's treated as inactive

    """
    def __init__(self):
        self.cubes = {}
    def parseInput(self, layout):
        for i,line in enumerate(layout):
            for j,space in enumerate(line):
                cube = Cube(i, j, 0, State(space)) # There's only one layer at the start
                self.cubes[(i,j,0)] = cube 

    # Advance the simulation one step forward
    def tick(self):
        newCubesToCheck = []
        for cube in list(self.cubes.values()):
            count, newCubes = self.getNeighbors(cube)
            # Update the current cube, and extend the list of newly created cubes
            cube.update(count)
            newCubesToCheck.extend(newCubes)
        # Now we have a bunch of new cubes, check their neighbors in case anything became active
        for cube in newCubesToCheck:
            # First, check if we've already gotten it
            if cube.getPos() in self.cubes:
                continue
            count, newCubes = self.getNeighbors(cube)
            cube.update(count)
            self.cubes[cube.getPos()] = cube
        for cube in self.cubes.values():
            cube.saveState()

    # Gets all 26 neighbors of a cube, creating new cubes if needed
    #
    # Returns a single number cooresponding to the number of neighboring active cubes
    # and also returns any new cubes created.
    def getNeighbors(self, cube):
        neighborStates = []
        newCubes = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                for z in [-1, 0, 1]:
                    if x == 0 and y == 0 and z == 0:
                        continue # it's itself
                    offset = [x,y,z]
                    neighborCoord = self.getNeighborCoord(cube.getPos(), *offset)
                    try:
                        neighbor = self.cubes[neighborCoord]
                    # Error here means we need to create that cube
                    except:
                        neighbor = Cube(*neighborCoord)
                        # Start tracking it
                        newCubes.append(neighbor)
                    neighborStates.append(neighbor.getState())
        count = len(list(filter(lambda x: x==State.ON, neighborStates)))
        return count, newCubes

    def getNeighborCoord(self, pos, x,y,z):
        return (pos[0]+x, pos[1]+y, pos[2]+z)

    def countActiveCubes(self):
        return len([cube for cube in self.cubes.values() if cube.isActive()])

    def listActiveCubes(self):
        return [cube.getPos() for cube in self.cubes.values() if cube.isActive()]

    def __str__(self):
        s = '**************\n'
        for z,layer in self.layers.items():
            s += f"\nz={z}\n"
            for row in layer:
                s+=''.join([str(c) for c in row])+'\n'
        return s+"**************" #get rid of the last newline

class Cube(object):
    """
    Single cube
    """
    def __init__(self, x, y, z, s=State.OFF):
        self.state = s
        self.x = x
        self.y = y
        self.z = z
        self.nextState = s
    
    def getPos(self):
        return (self.x, self.y, self.z)
    
    def isActive(self):
        return True if self.state == State.ON else False
    
    def update(self, count):
        self.nextState = self.state
        # ON states stay on if only if count is 2 or 3
        if self.state == State.ON and count not in [2,3]:
            # print(f"Cube at {self.getPos()} is turning OFF")
            self.nextState = State.OFF
        # OFF states turn on if count is 3
        if self.state == State.OFF and count == 3:
            # print(f"Cube at {self.getPos()} is turning ON")
            self.nextState = State.ON
        # returns if there was a state change
        return self.nextState == self.state
    
    def saveState(self):
        self.state = self.nextState

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state
    
    def __str__(self):
        return self.state.value

class Hyperspace(object):
    """
    Manager class for all the hypercubes

    - This hyperspace is infinite in all directions, so anytime something is OOB, it's treated as inactive

    """
    def __init__(self):
        self.cubes = {}
    def parseInput(self, layout):
        for i,line in enumerate(layout):
            for j,space in enumerate(line):
                cube = Hypercube(i, j, 0, 0, State(space)) # There's only one layer at the start
                self.cubes[(i,j,0, 0)] = cube 

    # Advance the simulation one step forward
    def tick(self):
        newCubesToCheck = []
        for cube in list(self.cubes.values()):
            count, newCubes = self.getNeighbors(cube)
            # Update the current cube, and extend the list of newly created cubes
            cube.update(count)
            newCubesToCheck.extend(newCubes)
        # Now we have a bunch of new cubes, check their neighbors in case anything became active
        for cube in newCubesToCheck:
            # First, check if we've already gotten it
            if cube.getPos() in self.cubes:
                continue
            count, newCubes = self.getNeighbors(cube)
            cube.update(count)
            self.cubes[cube.getPos()] = cube
        for cube in self.cubes.values():
            cube.saveState()

    # Gets all 80 neighbors of a cube, creating new cubes if needed
    #
    # Returns a single number cooresponding to the number of neighboring active cubes
    # and also returns any new cubes created.
    def getNeighbors(self, cube):
        neighborStates = []
        newCubes = []
        dirs = [-1, 0, 1]
        for x in dirs:
            for y in dirs:
                for z in dirs:
                    for w in dirs:
                        if x == 0 and y == 0 and z == 0 and w == 0:
                            continue # it's itself
                        offset = [x,y,z,w]
                        neighborCoord = self.getNeighborCoord(cube.getPos(), *offset)
                        try:
                            neighbor = self.cubes[neighborCoord]
                        # Error here means we need to create that cube
                        except:
                            neighbor = Hypercube(*neighborCoord)
                            # Start tracking it
                            newCubes.append(neighbor)
                        neighborStates.append(neighbor.getState())
        count = len(list(filter(lambda x: x==State.ON, neighborStates)))
        return count, newCubes

    def getNeighborCoord(self, pos, x,y,z,w):
        return (pos[0]+x, pos[1]+y, pos[2]+z, pos[3]+w)

    def countActiveCubes(self):
        return len([cube for cube in self.cubes.values() if cube.isActive()])

    def listActiveCubes(self):
        return [cube.getPos() for cube in self.cubes.values() if cube.isActive()]

    def __str__(self):
        s = '**************\n'
        for z,layer in self.layers.items():
            s += f"\nz={z}\n"
            for row in layer:
                s+=''.join([str(c) for c in row])+'\n'
        return s+"**************" #get rid of the last newline

          

class Hypercube(object):
    """
    Single hypercube
    """
    def __init__(self, x, y, z, w, s=State.OFF):
        self.state = s
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.nextState = s
    
    def getPos(self):
        return (self.x, self.y, self.z, self.w)
    
    def isActive(self):
        return True if self.state == State.ON else False
    
    def update(self, count):
        self.nextState = self.state
        # ON states stay on if only if count is 2 or 3
        if self.state == State.ON and count not in [2,3]:
            # print(f"Cube at {self.getPos()} is turning OFF")
            self.nextState = State.OFF
        # OFF states turn on if count is 3
        if self.state == State.OFF and count == 3:
            # print(f"Cube at {self.getPos()} is turning ON")
            self.nextState = State.ON
        # returns if there was a state change
        return self.nextState == self.state
    
    def saveState(self):
        self.state = self.nextState

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state
    
    def __str__(self):
        return self.state.value
