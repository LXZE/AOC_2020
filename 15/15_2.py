in_file = open('input_15.txt', 'r')
# in_file = open('test_15.txt', 'r')

def pushTillX(l, X):
	lookup = dict([[x, i+1] for i, x in enumerate(l[:-1])])
	once = set(l[:-1])
	i = len(l) + 1
	latest = l[-1]

	while i <= X:
		if latest not in once:
			once.add(latest)
			lookup[latest] = i-1
			latest = 0
		else:
			lookup[latest], latest = i-1, (i-1)-lookup[latest]
		i += 1
	return latest


start = list(map(lambda x: x.rstrip(), in_file.readlines()))[0].split(',')
start = list(map(int, start))
res = pushTillX(start, 30000000)
print(res)