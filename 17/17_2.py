from copy import deepcopy as dc
in_file = open('input_17.txt', 'r')
# in_file = open('test_17.txt', 'r')

toCheck = [(i,j,k,l) for i in range(-1, 2) for j in range(-1, 2) for k in range(-1, 2) for l in range(-1, 2) if (i,j,k,l) != (0,0,0,0)]
templateSpaces = lambda size: [['.']*size for _ in range(size)]

def countState(spaces):
	count = 0
	for cube in spaces:
		for spaceSlice in cube:
			for spaceRow in spaceSlice:
				count += spaceRow.count('#')
	return count

def setCube(cube):
	for i in range(len(cube)):
		for j in range(len(cube[i])):
			for k in range(len(cube[i][j])):
				cube[i][j][k] = '.'

def changeState(spaces):
	global toCheck, cycles, originalDim

	for i in range(len(spaces)):
		spaces[i].insert(0, templateSpaces((cycles*2) +originalDim))
		spaces[i].append(templateSpaces((cycles*2) +originalDim))
	c1 = dc(spaces[0])
	c2 = dc(spaces[0])
	setCube(c1)
	setCube(c2)
	spaces.insert(0, c1)
	spaces.append(c2)
	newSpace = dc(spaces)

	for w, cube in enumerate(spaces):
		for z, spaceSlice in enumerate(cube):
			for row, spaceRow in enumerate(spaceSlice):
				for col, spacePoint in enumerate(spaceRow):
					if spacePoint == '#': # active, if [2,3] neighbors are active then remain else inactive
						count = 0
						for offset in toCheck:
							if 	0 <= row + offset[2] < len(spaceSlice) 	and \
								0 <= col + offset[3] < len(spaceRow) 	and \
								0 <= z + offset[1] < len(cube) and \
								0 <= w + offset[0] < len(spaces):
								if spaces[w+offset[0]][z+offset[1]][row+offset[2]][col+offset[3]] == '#':
									count += 1
						if count not in [2,3]:
							newSpace[w][z][row][col] = '.'
					elif spacePoint == '.': # inactive, if 3 neighbors are active then active else remain
						count = 0
						for offset in toCheck:
							if 	0 <= row + offset[2] < len(spaceSlice) 	and \
								0 <= col + offset[3] < len(spaceRow) 	and \
								0 <= z + offset[1] < len(cube) and \
								0 <= w + offset[0] < len(spaces):
								if spaces[w+offset[0]][z+offset[1]][row+offset[2]][col+offset[3]] == '#':
									count += 1
						if count == 3:
							newSpace[w][z][row][col] = '#'
	return newSpace

spaces = list(map(lambda x: x.rstrip(), in_file.readlines()))
originalDim = len(spaces)
cycles = 6
for i in range(cycles):
	spaces.insert(0, '.'*originalDim)
	spaces.append('.'*originalDim)

for idx, row in enumerate(spaces):
	spaces[idx] = (['.'] * cycles) + list(row) +(['.'] * cycles)

spaces = [[spaces]]
for i in range(cycles):
	# print(f'After {i+1} cycle')
	spaces = changeState(spaces)
	# for iw, cube in enumerate(spaces):
	# 	for iz, spaceSlice in enumerate(cube):
	# 		print(f'z={iz-(i+1)}, w={iw-(i+1)}')
	# 		for row in spaceSlice:
	# 			print(''.join(row))

print(countState(spaces))