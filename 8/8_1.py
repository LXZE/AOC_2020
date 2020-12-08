in_file = open('input_8.txt', 'r')
# in_file = open('test_8.txt', 'r')

def op(line):
	global acc
	global pointer
	ops, num = line.split(' ')
	if ops == 'acc':
		if num[0] == '+':
			acc += int(num[1:])
		else: acc -= int(num[1:])
		return 1
	elif ops == 'jmp':
		if num[0] == '+':
			pointer += int(num[1:])
		else: pointer -= int(num[1:])
		return 0
	else: return 1
acc = 0
pointer = 0
evaled = []
raw = list(map(lambda x: x.rstrip(), in_file.readlines()))
while True:
	if pointer not in evaled:
		evaled.append(pointer)
	else: break
	line = raw[pointer]
	pc = op(line)
	if pc == 1: pointer += 1
print(acc)