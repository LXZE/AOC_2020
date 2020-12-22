in_file = open('input_22.txt', 'r')
# in_file = open('test_22.txt', 'r')

raws = list(map(lambda x: x.rstrip(), in_file.readlines()))
raws.append('')
data = []; tmp = []
for line in raws:
	if line == '':
		data.append(tmp)
		tmp = []
	else:
		tmp.append(line)
# print(data)
p1, p2 = data
p1 = list(map(int, p1[1:]))
p2 = list(map(int, p2[1:]))

def convert(deck1, deck2):
	return ''.join(map(str, deck1)) + '/' + ''.join(map(str, deck2))

def subGame(d1, d2):
	memo = set()
	while len(d1) > 0 and len(d2) > 0:
		state = convert(d1,d2)

		if state in memo:
			return 1
		else:
			memo.add(state)
		
		x1 = d1.pop(0)
		x2 = d2.pop(0)
		if x1 <= len(d1) and x2 <= len(d2):
			result = subGame(d1[:x1], d2[:x2])
			if result == 1:
				d1.extend([x1, x2])
			else:
				d2.extend([x2, x1])
		else:
			if x1 > x2:
				d1.extend([x1, x2])
			else:
				d2.extend([x2, x1])

	return 1 if len(d1) > 0 else 2

memo = []
i = 0
while len(p1) != 0 and len(p2) != 0:
	state = convert(p1,p2)

	x1 = p1.pop(0)
	x2 = p2.pop(0)
	if state in memo:
		p1.append(x1); p1.append(x2)
		continue
	else:
		memo.append(state)
	
	if x1 <= len(p1) and x2 <= len(p2):
		result = subGame(p1[:x1], p2[:x2])
		if result == 1:
			p1.extend([x1, x2])
		else:
			p2.extend([x2, x1])
	else:
		if x1 > x2:
			p1.extend([x1, x2])
		else:
			p2.extend([x2, x1])

winner = p1 if len(p1) > 0 else p2
res = sum(map(lambda x: (x[0]+1)*x[1], enumerate(winner[::-1])))
print(res)