in_file = open('input_10.txt', 'r')
# in_file = open('test_10.txt', 'r')

res = [0,0,1] # + 3 volt for the built-in adapter

raw = list(map(lambda x: int(x.rstrip()), in_file.readlines()))
raw.append(0) # 0 is nearest one according to the question
raw.sort()
for idx in range(1, len(raw)):
	try:
		res[raw[idx] - raw[idx-1]-1] += 1
	except IndexError:
		print(raw[idx])
print(res[0] * res[2])