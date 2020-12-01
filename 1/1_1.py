in_file = open('input_1.txt', 'r')
# in_file = open('test_1.txt', 'r')
numList = map(lambda x: int(x[:-1]), in_file.readlines())
target = 2020
for num in numList:
	if target - num in numList:
		res = [num, target - num]
print(res[0] * res[1])