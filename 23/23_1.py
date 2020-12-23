in_file = open('input_23.txt', 'r')
# in_file = open('test_23.txt', 'r')

cups = list(map(lambda x: x.rstrip(), in_file.readlines()))[0]
cups = list(map(int, list(cups)))

MAX = max(cups)

def shuffle(cups):
	# print(f'cups: {cups}')
	current = cups.pop(0)
	stack = [cups.pop(0) for _ in range(3)]
	# print(f'pick up: {stack}')
	destination = current - 1 if current > 1 else MAX
	while destination in stack:
		if destination > 1:
			destination -= 1
		else:
			destination = MAX
	
	# print(f'destination {destination}')
	idx = cups.index(destination) + 1
	cups[idx:idx] = stack
	cups.append(current)
moves = 100
for i in range(moves):
	# print(f'-- move {i+1} --')
	shuffle(cups)
# print('-- final --')
# print(cups)
oneIdx = cups.index(1)
res = cups[oneIdx+1:] + cups[:oneIdx]
print(''.join(map(str,res)))