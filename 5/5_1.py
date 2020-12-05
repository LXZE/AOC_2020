in_file = open('input_5.txt', 'r')
# in_file = open('test_5.txt', 'r')

def decode(line):
	row, col = line[:-3], line[-3:]
	cur_x, cur_y = [0, 127], [0, 7]
	f = 128
	for i, ch in enumerate(row):
		if ch == 'F': cur_x[1] -= f/(2**(i+1))
		else: cur_x[0] += f/(2**(i+1))
	f = 8
	for i, ch in enumerate(col):
		if ch == 'L': cur_y[1] -= f/(2**(i+1))
		else: cur_y[0] += f/(2**(i+1))
	return int(cur_x[0]), int(cur_y[0])

res = 0
raw = list(map(lambda x: x.rstrip(), in_file.readlines()))
for line in raw:
	r, c = decode(line)
	tmp = (r*8)+c
	if tmp > res: res = tmp
print(res)