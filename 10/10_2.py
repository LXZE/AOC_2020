from functools import reduce
in_file = open('input_10.txt', 'r')
# in_file = open('test_10.txt', 'r')

def search(data):
	def findCombi(val):
		# according to the given data, the maximum range that can be shuffle is 5 >:D
		return [1, 1 ,2, 4, 7][len(val)-1]
	count = []
	tmp = []
	for i in range(1, len(data)):
		tmp.append(data[i-1])
		if data[i] - data[i-1] == 3:
			count.append(findCombi(tmp))
			tmp = []
	return reduce(lambda x,y: x*y, count, 1)

raw = list(map(lambda x: int(x.rstrip()), in_file.readlines()))	
raw.append(0)
raw.sort()
raw.append(raw[-1] + 3) # have to add this as it will trigger the last loop in search
res = search(raw)
print(res)