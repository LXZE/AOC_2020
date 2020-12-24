from collections import defaultdict as ddict
from operator import add

in_file = open('input_24.txt', 'r')
# in_file = open('test_24.txt', 'r')

tiles = list(map(lambda x: x.rstrip(), in_file.readlines()))
def splitStep(ls):
	res = []; tmp = ''
	for char in ls:
		if char == 'e' or char == 'w':
			res.append(tmp + char)
			tmp = ''
		else:
			tmp += char
	return res
tiles = list(map(splitStep, tiles))

def traverse(paths):
	pos = [0,0]
	def step(direction):
		r = {
			'ne': [1, 0.5],
			'nw': [1, -0.5],
			'e': [0, 1],
			'w': [0, -1],
			'se': [-1, 0.5],
			'sw': [-1, -0.5]
		}
		return r[direction]
	for p in paths:
		pos = tuple(map(add, pos, step(p)))
	return pos

flipped = ddict(bool)
for t in tiles:
	targetTiles = traverse(t)
	if targetTiles not in flipped:
		flipped[targetTiles] = True
	else:
		flipped[targetTiles] = not flipped[targetTiles]

adjacents = [[1, 0.5],[1, -0.5],[0, 1],[0, -1],[-1, 0.5],[-1, -0.5]]

def expandTiles(tiles):
	newTiles = tiles.copy()
	for tilePos in tiles.keys():
		p = tilePos
		for adj in adjacents:
			newPos = tuple(map(add, p, adj))
			if newPos not in newTiles:
				newTiles[newPos] = False
	return newTiles

def flipTiles(tiles):
	tiles = expandTiles(tiles)
	newTiles = tiles.copy()
	
	for tilePos, tileVal in tiles.items():
		count = 0
		for adj in adjacents:
			toCheckPos = tuple(map(add, tilePos, adj))
			if toCheckPos in tiles.keys() and tiles[toCheckPos]:
				count += 1

		# tile currently flipped to black, check if adjacent is black && amnt = 0 or 2++ flip to white
		if tileVal: 
			if count not in [1,2]:
				newTiles[tilePos] = False
		else: # tile currently white, check if adjacent is 2 flip to black
			if count == 2:
				newTiles[tilePos] = True
	return newTiles

def countFlip(tiles):
	return len(list(filter(lambda x: x, tiles.values())))

day = 100
for i in range(day):
	flipped = flipTiles(flipped)
	# print(f'day {i+1}: {countFlip(flipped)}')
print(countFlip(flipped))