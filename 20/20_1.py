from copy import deepcopy as dc
import math
# in_file = open('input_20.txt', 'r')
in_file = open('test_20.txt', 'r')

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

# (n, m) -> n = flipped?, m = rotated * 90
tileCombi = [(n, m) for n in range(0, 2) for m in range(0, 4)]

def resolve(tilesDict):

	def modified(tile, flip, rotate):
		modTile = dc(tile)
		if bool(flip):
			for i, row in enumerate(tile):
				modTile[i] = row[::-1]
		for i in range(rotate):
			modTile = list(map(lambda x: ''.join(x), list(zip(*modTile[::-1]))))
		return modTile

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

		for tileKey, tileVal in tilesDict.items():
			oldTileVal = dc(tileVal)

			for flip, rotate in tileCombi:
				tileVal = modified(dc(oldTileVal), flip, rotate)
				
				# check top
				if tileData[0] == tileVal[-1]:
					links[selectedKey]['top'] = { 'key': tileKey, 'val': tileVal }
					links[tileKey]['bottom'] =  { 'key': selectedKey, 'val': tileData }
					queue.append(tileKey)
				# check bot
				elif tileData[-1] == tileVal[0]:
					links[selectedKey]['bottom'] = { 'key': tileKey, 'val': tileVal }
					links[tileKey]['top'] =  { 'key': selectedKey, 'val': tileData }
					queue.append(tileKey)
				
				# check left
				elif list(zip(*tileData))[0] == list(zip(*tileVal))[-1]:
					links[selectedKey]['left'] = { 'key': tileKey, 'val': tileVal }
					links[tileKey]['right'] =  { 'key': selectedKey, 'val': tileData }
					queue.append(tileKey)

				# check right
				elif list(zip(*tileData))[-1] == list(zip(*tileVal))[0]:
					links[selectedKey]['right'] = { 'key': tileKey, 'val': tileVal }
					links[tileKey]['left'] =  { 'key': selectedKey, 'val': tileData }
					queue.append(tileKey)

	res = 1
	for k, v in links.items():
		if len(v.keys()) == 2:
			res *= k
	return res
res = resolve(tiles)
print(res)
