import re
in_file = open('input_4.txt', 'r')
# in_file = open('test_4.txt', 'r')

def getChecker():
	checkCondition = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	return dict(map(lambda x: (x, False), checkCondition))

def validate(key, value):
	def byr(val): return len(val) == 4 and 1920 <= int(val) <= 2002
	def iyr(val): return len(val) == 4 and 2010 <= int(val) <= 2020
	def eyr(val): return len(val) == 4 and 2020 <= int(val) <= 2030
	def hgt(val):
		if val[-2:] == 'cm':
			return 150 <= int(val[:-2]) <= 193
		elif val[-2:] == 'in':
			return 59 <= int(val[:-2]) <= 76
		else: return False
	def hcl(val): return len(val) == 7 and bool(re.match('#([0-9a-f]{6})', val))
	def ecl(val): return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	def pid(val): return len(val) == 9 and bool(re.match('(\d{9})', val))
	switch = {
		'byr': byr,
		'iyr': iyr,
		'eyr': eyr,
		'hgt': hgt,
		'hcl': hcl,
		'ecl': ecl,
		'pid': pid
	}
	return switch.get(key, lambda: False)(value)

def verify(infoLine):
	checkList = getChecker()
	for info in infoLine.split(' '):
		if info[:3] in checkList.keys():
			k, v = info.split(':')
			if validate(k,v): checkList[k] = True
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