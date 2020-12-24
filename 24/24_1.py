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
		pos = list(map(lambda x: x[0]+x[1], zip(pos, step(p))))
	return pos
flipped = dict()
for t in tiles:
	targetTiles = ','.join(map(str, traverse(t)))
	if targetTiles not in flipped:
		flipped[targetTiles] = True
	else:
		flipped[targetTiles] = not flipped[targetTiles]

# print(flipped)
res = 0
for v in flipped.values():
	if v: res += 1
print(res)