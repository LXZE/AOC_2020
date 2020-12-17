from copy import deepcopy as dc
in_file = open('input_17.txt', 'r')
# in_file = open('test_17.txt', 'r')

toCheck = [(i,j,k) for i in range(-1, 2) for j in range(-1, 2) for k in range(-1, 2) if (i,j,k) != (0,0,0)]
templateSpaces = lambda size: [['.']*size for _ in range(size)]

def countState(spaces):
	count = 0
	for spaceSlice in spaces:
		for spaceRow in spaceSlice:
			count += spaceRow.count('#')
	return count

def changeState(spaces):
	global toCheck, cycles, originalDim

	spaces.insert(0, templateSpaces((cycles*2) +originalDim))
	spaces.append(templateSpaces((cycles*2) +originalDim))
	newSpace = dc(spaces)

	for z, spaceSlice in enumerate(spaces):
		for row, spaceRow in enumerate(spaceSlice):
			for col, spacePoint in enumerate(spaceRow):
				if spacePoint == '#': # active, if [2,3] neighbors are active then remain else inactive
					count = 0
					for offset in toCheck:
						if 	0 <= row + offset[1] < len(spaceSlice) 	and \
							0 <= col + offset[2] < len(spaceRow) 	and \
							0 <= z + offset[0] < len(spaces):
							if spaces[z+offset[0]][row+offset[1]][col+offset[2]] == '#':
								count += 1
					if count not in [2,3]:
						newSpace[z][row][col] = '.'
				elif spacePoint == '.': # inactive, if 3 neighbors are active then active else remain
					count = 0
					for offset in toCheck:
						if 	0 <= row + offset[1] < len(spaceSlice) 	and \
							0 <= col + offset[2] < len(spaceRow) 	and \
							0 <= z + offset[0] < len(spaces):
							if spaces[z+offset[0]][row+offset[1]][col+offset[2]] == '#':
								count += 1
					if count == 3:
						newSpace[z][row][col] = '#'
	return newSpace

spaces = list(map(lambda x: x.rstrip(), in_file.readlines()))
originalDim = len(spaces)
cycles = 6
for i in range(cycles):
	spaces.insert(0, '.'*originalDim)
	spaces.append('.'*originalDim)

for idx, row in enumerate(spaces):
	spaces[idx] = (['.'] * cycles) + list(row) +(['.'] * cycles)

spaces = [spaces]

for i in range(cycles):
	# print(f'After {i+1} cycle')
	spaces = changeState(spaces)
	# for iz, spaceSlice in enumerate(spaces):
	# 	print(iz-(i+1))
	# 	for row in spaceSlice:
	# 		print(''.join(row))

print(countState(spaces))