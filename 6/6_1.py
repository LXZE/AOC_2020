in_file = open('input_6.txt', 'r')
# in_file = open('test_6.txt', 'r')

res = 0
raw = list(map(lambda x: x.rstrip(), in_file.readlines()))
raw.append('') # for trigger last element in below loop
tmp = set()
for line in raw:
	if line == '':
		res += len(tmp)
		tmp = set()
	else:
		for c in line: tmp.add(c)
print(res)