from math import ceil
in_file = open('input_13.txt', 'r')
# in_file = open('test_13.txt', 'r')

raw = list(map(lambda x: x.rstrip(), in_file.readlines()))
startTime = int(raw[0])
busesList = raw[1].split(',')
busesList = list(map(int, filter(lambda x: x.isnumeric(), busesList)))

res = -1
mini = startTime*2
for idx, time in enumerate(busesList):
	tmp = ceil(startTime/time) * time
	if tmp < mini:
		mini = tmp
		res = idx
print((mini-startTime) * busesList[res])