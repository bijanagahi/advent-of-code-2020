from Day_20_classes import Tile, SimpleTile
from random import shuffle

def main(lines):
	tiles = parseSimpleTiles(lines)	
	cornerTiles = 1
	for tile in tiles:
		# Given a tile, for each side, check how many other tiles share that border
		sideMatches = {}
		for side,border in tile.borders.items():
			sideMatches[side] = 0
			for otherTile in tiles:
				if tile == otherTile:
					continue
				if border in otherTile.allBorders:
					sideMatches[side]+= 1#otherTile.id
		if len([x for x in sideMatches.values() if x == 0]) == 2:
			print(f"Tile [{tile.id}] side matches: ",sideMatches)
			cornerTiles *= (int(tile.id))
	print(cornerTiles)
	exit()


	# tiles[1].checkBorders(tiles[0])
	# tiles[1].checkBorders(tiles[7])

	# General approach:
	#
	# For each tile, check all the borders against each other tile,
	#	going through all possible transformations in the process.
	# If a tile matches borders though, we shouldn't allow any more transformations.
	for tile in tiles:
		for otherTile in tiles:
			if tile==otherTile:
				continue

			# Check borders
			if tile.checkBorders(otherTile):
				continue

			otherTile.rotateCW() # 90 degress
			if tile.checkBorders(otherTile):
				continue
			
			otherTile.rotateCW() # 180 degress
			if tile.checkBorders(otherTile):
				continue

			otherTile.rotateCW() # 270 degress
			if tile.checkBorders(otherTile):
				continue

			otherTile.rotateCW() # go back to the original
			otherTile.flipV() # Vertical flip
			if tile.checkBorders(otherTile):
				continue

			otherTile.flipV() # back to original
			otherTile.flipH() # horizontal flip
			if tile.checkBorders(otherTile):
				continue


	print(tiles[7].neighbors)
	# print(tiles[0].neighbors)


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
	return tiles

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