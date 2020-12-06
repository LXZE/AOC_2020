from collections import defaultdict as ddict
from functools import reduce
in_file = open('input_6.txt', 'r')
# in_file = open('test_6.txt', 'r')

def counter(data):
	s = len(data)
	d = ddict(int)
	for ans in data:
		for c in ans:
			d[c] += 1
	return reduce(lambda x, y: x + 1 if y == s else x, d.values(), 0)

res = 0
raw = list(map(lambda x: x.rstrip(), in_file.readlines()))
raw.append('') # for trigger last element in below loop
tmp = []
for line in raw:
	if line == '':
		res += counter(tmp)
		tmp = []
	else:
		tmp.append(line)
print(res)