import math
import numpy as np
from copy import deepcopy as dc
in_file = open('input_20.txt', 'r')
# in_file = open('test_20.txt', 'r')

raws = list(map(lambda x: x.rstrip(), in_file.readlines()))
tiles = dict()
tmp = []
for line in raws:
	if line == '':
		tileID = tmp[0].split(' ')[1][:-1]
		tiles[int(tileID)] = tmp[1:]
		tmp = []
	else:
		tmp.append(line)
size = int(math.sqrt(len(tiles.keys())))

# (n, m) -> n = flipped?, m = rotated * 90
tileCombi = [(n, m) for n in range(0, 2) for m in range(0, 4)]

def modified(tile, flip, rotate):
	modTile = dc(tile)
	if bool(flip):
		for i, row in enumerate(tile):
			modTile[i] = row[::-1]
	for i in range(rotate):
		modTile = list(map(lambda x: ''.join(x), list(zip(*modTile[::-1]))))
	return modTile

def resolve(tilesDict):
	links = dict()
	for k in tilesDict.keys():
		links[k] = dict()

	queue = [list(tilesDict.keys())[0]]
	while len(tilesDict.keys()) > 1:
		selectedKey = queue.pop(0)

		if len(links[selectedKey].keys()) == 0:
			tileData = tilesDict[selectedKey]
		else:
			 # if iterated then use that modified data
			for tileKey, info in links.items():
				for v in info.values():
					if v['key'] == selectedKey:
						tileData = v['val']
		
		if selectedKey in tilesDict.keys():
			del tilesDict[selectedKey]
		else:
			continue
		links[selectedKey]['self'] = {'key': selectedKey, 'val': tileData} # for next path to indicate self tile
		for tileKey, tileVal in tilesDict.items():
			oldTileVal = dc(tileVal)

			for flip, rotate in tileCombi:
				tileVal = modified(dc(oldTileVal), flip, rotate)
				
				# check top
				if tileData[0] == tileVal[-1]:
					links[selectedKey]['top'] = { 'key': tileKey, 'val': tileVal }
					links[tileKey]['bottom'] =  { 'key': selectedKey, 'val': tileData }
					links[tileKey]['self'] = {'key': tileKey, 'val': tileVal}
					queue.append(tileKey)
				# check bot
				elif tileData[-1] == tileVal[0]:
					links[selectedKey]['bottom'] = { 'key': tileKey, 'val': tileVal }
					links[tileKey]['top'] =  { 'key': selectedKey, 'val': tileData }
					links[tileKey]['self'] = {'key': tileKey, 'val': tileVal}
					queue.append(tileKey)
				
				# check left
				elif list(zip(*tileData))[0] == list(zip(*tileVal))[-1]:
					links[selectedKey]['left'] = { 'key': tileKey, 'val': tileVal }
					links[tileKey]['right'] =  { 'key': selectedKey, 'val': tileData }
					links[tileKey]['self'] = {'key': tileKey, 'val': tileVal}
					queue.append(tileKey)

				# check right
				elif list(zip(*tileData))[-1] == list(zip(*tileVal))[0]:
					links[selectedKey]['right'] = { 'key': tileKey, 'val': tileVal }
					links[tileKey]['left'] =  { 'key': selectedKey, 'val': tileData }
					links[tileKey]['self'] = {'key': tileKey, 'val': tileVal}
					queue.append(tileKey)
				
	return links
connMap = resolve(tiles)

finalMap = [[[] for i in range(size)] for j in range(size)]
curRow, curCol = 0, 0
start = ''
for k, v in connMap.items():
	if len(v.keys()) == 3 and set(v.keys()) == set(['bottom', 'right', 'self']):
		start = k
		break
nextKey = [start]

def removeEdge(val):
	new = []
	for v in val[1:-1]:
		new.append(v[1:-1])
	return new

while len(nextKey) > 0:
	key = nextKey.pop()
	data = connMap[key]
	del connMap[key]
	finalMap[curRow][curCol] = removeEdge(data['self']['val'])
	if curCol == 0:
		if 'bottom' in data.keys():
			nextKey.append(data['bottom']['key'])
	if 'right' in data.keys():
		nextKey.append(data['right']['key'])
		curCol += 1
	else: curCol = 0; curRow += 1
fMap = []
for row in finalMap:
	for r in zip(*row):
		fMap.append(''.join(list(r)))

monsterImg = '''\
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   \
'''
monsterImg = monsterImg.split('\n')

def findMonster(image, monsterStruct):

	def isMatch(mask, toCheck):
		for (x, y) in zip(mask, toCheck):
			if x == '#' and y == '.':
				return False
		return True

	res = 0
	for flip, rotate in tileCombi:
		modImage = modified(dc(image), flip, rotate)
		for rowIdx, row in enumerate(modImage[1:-1]):
			for offset in range(len(modImage)-len(monsterImg[1])):
				if isMatch(monsterImg[1], row[offset:]) and \
					isMatch(monsterImg[0], modImage[rowIdx][offset:]) and \
					isMatch(monsterImg[2], modImage[rowIdx+2][offset:]):
					res += 1
	return res

def countSharp(image):
	res = 0
	for row in image:
		res += row.count('#')
	return res

res = findMonster(fMap, monsterImg)
print(countSharp(fMap) - (countSharp(monsterImg) * res))