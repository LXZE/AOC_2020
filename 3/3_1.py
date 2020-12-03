in_file = open('input_3.txt', 'r')
# in_file = open('test_3.txt', 'r')

res = 0
terrain = map(lambda x: x.rstrip(), in_file.readlines())
current_y = 0
for line in terrain:
	if line[current_y] == '#': res += 1
	current_y += 3
	if current_y >= len(line) - 1: current_y -= len(line)
print(res)