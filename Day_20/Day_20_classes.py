from enum import Enum

class SimpleTile(object):
	''' Simple version of a Tile that only knows its borders'''
	def __init__(self, ID, lines):
		self.id = ID
		self.grid = [list(line) for line in lines]
		self.borders = self._calculateBorders()
		self.allBorders = self._calculateAllBorders()

	# def checkBorders(self, otherBorders):
	# 	for borders in self.borders.values():
	# 		for border in borders:

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
		self.id = ID
		self.grid = [list(line) for line in lines]
		self.neighbors = {
			Side.NORTH:None,
			Side.SOUTH:None,
			Side.EAST:None,
			Side.WEST:None
		}
		self.locked = False # Once neighbors have been added, no more transformations

	## Utility Functions


	# Checks if any borders are shared with another tile
	#
	# If a border matches, both tiles are updated with their respective neighbor
	# Returns True if a match was found
	def checkBorders(self, otherTile):
		otherBorders = otherTile.getBorders()
		for side,border in self.getBorders().items():
			for otherSide, otherBorder in otherBorders.items():
				if border == otherBorder:
					# We found a border that matches ours
					if self.isSeam(side, otherSide):
						print(f"Tile [{self.id}] found a matching border with Tile [{otherTile.id}]: Our [{side.name}] with their [{otherSide.name}]")
						otherTile.addNeighbor(otherSide, self)
						self.addNeighbor(side, otherTile)
						return True
		return False

	def addNeighbor(self, side, otherTile):
		if not self.neighbors[side] == None and not self.neighbors[side]==otherTile:
			print(f"Oh no this neighbor is already taken by Tile [{self.neighbors[side].id}]")
			raise ValueError
		self.neighbors[side] = otherTile
		self.locked = True

	def getBorders(self):
		return {
			Side.NORTH:self.grid[0],
			Side.SOUTH:self.grid[-1],
			Side.EAST:[x[-1] for x in self.grid],
			Side.WEST:[x[0] for x in self.grid]
		}

	def isSeam(self, side, otherSide):
		if side == otherSide:
			return False
		if side == Side.NORTH:
			return True if otherSide == Side.SOUTH else False
		if side == Side.SOUTH:
			return True if otherSide == Side.NORTH else False
		if side == Side.WEST:
			return True if otherSide == Side.EAST else False
		if side == Side.EAST:
			return True if otherSide == Side.WEST else False



	# Transformation Functions
	def rotateCW(self):
		if not self.locked:
			self.grid = list(zip(*self.grid[::-1]))
	def rotateCCW(self):
		if not self.locked:
			self.grid = list(reversed(list(zip(*self.grid))))
	def flipV(self):
		if not self.locked:
			self.grid = self.grid[::-1]
	def flipH(self):
		if not self.locked:
			self.grid = [_[::-1] for _ in self.grid]

	# Instance Functions
	def __str__(self):
		return '\n'.join(''.join(line) for line in self.grid)+'\n'


class Side(Enum):
	NORTH = 1
	EAST = 2
	SOUTH = 3
	WEST = 4



