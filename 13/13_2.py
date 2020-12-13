in_file = open('input_13.txt', 'r')
# in_file = open('test_13.txt', 'r')

raw = list(map(lambda x: x.rstrip(), in_file.readlines()))
busesList = raw[1].split(',')

res = 0
prod = 1
for idx, busID in enumerate(busesList):
	if busID == 'x': continue
	while (res + idx) % int(busID) != 0:
		res += prod
	prod *= int(busID)
print(res)
