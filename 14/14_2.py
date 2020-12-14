in_file = open('input_14.txt', 'r')
# in_file = open('test_14.txt', 'r')

def masked(mask, memAddress):
	newAddress = list(memAddress.zfill(len(mask)))
	for idx in range(len(newAddress)-1, -1, -1):
		if mask[idx] != '0':
			newAddress[idx] = mask[idx]
	return ''.join(newAddress).lstrip('0') or '0'

mem = dict()
def interpret(codes):
	global mem
	currentMask = ''

	for code in codes:
		cmd, val = code.split(' = ')
		if cmd == 'mask':
			currentMask = val
			continue

		possibleAddress = masked(currentMask, bin(int(cmd[4: -1]))[2:])
		cases = possibleAddress.count('X')
		for i in range(2**cases):
			substi = bin(i)[2:].zfill(cases)
			tmpAddress = possibleAddress
			for s in substi:
				tmpAddress = tmpAddress.replace('X', s, 1)
			tmpAddress = tmpAddress.zfill(36)
			mem[tmpAddress] = int(val)

codes = list(map(lambda x: x.rstrip(), in_file.readlines()))
interpret(codes)
res = 0

for memPos, val in mem.items():
	caseAmount = memPos.count('X')
	res += (2**caseAmount) * val
print(res)
