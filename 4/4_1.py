in_file = open('input_4.txt', 'r')
# in_file = open('test_4.txt', 'r')

def getChecker():
	checkCondition = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	return dict(map(lambda x: (x, False), checkCondition))

def verify(infoLine):
	checkList = getChecker()
	for info in infoLine.split(' '):
		if info[:3] in checkList.keys():
			checkList[info[:3]] = True
	return all(checkList.values())

res = 0
raw = list(map(lambda x: x.rstrip(), in_file.readlines()))
raw.append('') # for trigger last element in below loop
tmp = []
for line in raw:
	if line == '':
		if verify(' '.join(tmp)): res += 1
		tmp = []
	else:
		tmp.append(line)
print(res)