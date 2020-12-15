in_file = open('input_15.txt', 'r')
# in_file = open('test_15.txt', 'r')

def pushTill2020(l):
	while len(l) < 2020:
		if l[0] not in l[1:]:
			l.insert(0, 0)
		else:
			l.insert(0, l[1:].index(l[0]) + 1)
	return l[0]

start = list(map(lambda x: x.rstrip(), in_file.readlines()))[0].split(',')
start = list(map(int, start[::-1]))
res = pushTill2020(start)
print(res)