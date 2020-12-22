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
# print(p1,p2)
while len(p1) != 0 and len(p2) != 0:
	x1 = p1.pop(0)
	x2 = p2.pop(0)
	if x1 > x2:
		p1.extend([x1, x2])
	else:
		p2.extend([x2, x1])
winner = p1 if len(p1) > 0 else p2
res = sum(map(lambda x: (x[0]+1)*x[1], enumerate(winner[::-1])))
print(res)