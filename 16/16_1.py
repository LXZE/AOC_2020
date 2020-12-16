from itertools import chain
in_file = open('input_16.txt', 'r')
# in_file = open('test_16.txt', 'r')

flatten = lambda t: [item for sublist in t for item in sublist]
def getRange(data):
	res = []
	for line in data:
		tmp = line.split(': ')[1].split(' or ')
		res.append(tmp)
	res = list(map(lambda r: list(map(int, r.split('-'))), flatten(res)))
	res = list(map(lambda x: range(x[0], x[1]+1), res))
	return set(chain(*res))

raw = list(map(lambda x: x.rstrip(), in_file.readlines()))
raw.append('')
sec = []
tmp = []
for line in raw:
	if line == '':
		sec.append(tmp)
		tmp = []
	else:
		tmp.append(line)
crit = getRange(sec[0])

err = 0
for ticket in sec[2][1:]:
	vecNum = list(map(int, ticket.split(',')))
	for num in vecNum:
		if num not in crit:
			err += num
print(err)
