from itertools import chain
from functools import reduce
in_file = open('input_16.txt', 'r')
# in_file = open('test_16.txt', 'r')
# in_file = open('test_16_2.txt', 'r')

flatten = lambda t: [item for sublist in t for item in sublist]
def getRange(data):
	def genRange(v):
		r = list(map(lambda r: list(map(int, r.split('-'))), v))
		r = list(map(lambda x: range(x[0], x[1]+1), r))
		return set(chain(*r))
	res = dict()
	for line in data:
		dataType, val = line.split(': ')
		res[dataType] = genRange(val.split(' or '))
	return res

def removeClass(mk, cl, idx):
	global skippedIdx
	newMK = []
	for i, m in enumerate(mk):
		if i in skippedIdx or i == idx:
			newMK.append(m)
			continue
		elif len(m) > 1 and cl in m:
			m.pop(m.index(cl))
			newMK.append(m)
	return newMK

raw = list(map(lambda x: x.rstrip(), in_file.readlines()))
raw.append('')
sec = []; tmp = []
for line in raw:
	if line == '':
		sec.append(tmp)
		tmp = []
	else:
		tmp.append(line)
sec[2] = sec[2][1:]
crit = getRange(sec[0])

numFilter = set()
for s in crit.values(): numFilter.update(s)

validTicket = []
for ticket in sec[2]:
	vecNum = list(map(int, ticket.split(',')))
	err = False
	for num in vecNum:
		if num not in numFilter:
			err = True
			break
	if not err:
		validTicket.append(vecNum)

marker = [''] * len(sec[0])
for idx, col in enumerate(zip(*validTicket)):
	marker[idx] = []
	for k, v in crit.items():
		if set(col).issubset(v):
			marker[idx].append(k)

skippedIdx = set()
while any([len(m) > 1 for m in marker]):
	for idx, m in enumerate(marker):
		if len(m) == 1 and idx not in skippedIdx:
			checkedType = m[0]
			skippedIdx.add(idx)
			marker = removeClass(marker, checkedType, idx)
			break

myTicket = sec[1][1].split(',')
res = 1
for idx, m in enumerate(flatten(marker)):
	if 'departure' in m:
		res *= int(myTicket[idx])
print(res)
