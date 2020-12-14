in_file = open('input_14.txt', 'r')
# in_file = open('test_14.txt', 'r')

def masked(mask, code):
	newCode = list(code.zfill(len(mask)))
	for idx in range(len(newCode)-1, -1, -1):
		if mask[idx] != 'X':
			newCode[idx] = mask[idx]
	return '0b' + ''.join(newCode).lstrip('0') or '0b0'

mem = dict()
def interpret(codes):
	global mem
	currentMask = ''

	for code in codes:
		cmd, val = code.split(' = ')
		if cmd == 'mask':
			currentMask = val
			continue
		mem[cmd] = masked(currentMask, bin(int(val))[2:])
		

codes = list(map(lambda x: x.rstrip(), in_file.readlines()))
interpret(codes)
res = 0
for val in mem.values():
	res += int(val, 2)
print(res)