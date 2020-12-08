in_file = open('input_8.txt', 'r')
# in_file = open('test_8.txt', 'r')

def op(line, acc, pointer):
	new_acc, new_pc = acc, pointer
	ops, num = line.split(' ')
	if ops == 'acc':
		if num[0] == '+':
			new_acc += int(num[1:])
		else: new_acc -= int(num[1:])
	elif ops == 'jmp':
		if num[0] == '+':
			new_pc += int(num[1:])
		else: new_pc -= int(num[1:])
		return new_acc, new_pc
	return new_acc, new_pc + 1

def testCandidate(patch, code):
	acc = 0
	pointer = 0
	evaled = []
	newCode = code[::]
	newCode[patch[0]] = f'{patch[1]} {code[patch[0]].split(" ")[1]}'

	try: 
		while True:
			if pointer >= len(newCode): break
			if pointer not in evaled: evaled.append(pointer)
			else: raise Exception('infinite loop')
			line = newCode[pointer]
			acc, pointer = op(line, acc, pointer)
		return acc
	except Exception as e:
		return -1

candidate = []
raw = list(map(lambda x: x.rstrip(), in_file.readlines()))

for idx, line in enumerate(raw):
	if line[:3] == 'jmp': candidate.append((idx, 'nop'))
	elif line[:-3] == 'nop': candidate.append((idx, 'jmp'))

for c in candidate:
	tmp = testCandidate(c, raw)
	if tmp != -1: print(tmp)
