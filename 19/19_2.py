import re
in_file = open('input_19.txt', 'r')

def countValid(rules, data):
	return len(list(filter(lambda d: d in rules, data)))

raw = list(map(lambda x: x.rstrip(), in_file.readlines()))
raw.append('')

r = []; tmp = []
for line in raw:
	if line == '':
		r.append(tmp)
		tmp = []
	else:
		tmp.append(line)
ruleList, data = r

ruleList.append('8: 42 | 42 8')
ruleList.append('11: 42 31 | 42 11 31')

rules = dict()
for r in ruleList:
	k, v = r.split(': ')
	if '"' in v:
		rules[k] = v[1]
	else:
		rules[k] = v.split(' | ')
for k, v in rules.items():
	if v not in ['a', 'b']:
		rules[k] = list(map(lambda x: x.split(' '), v))

def build(idx):
	rule = rules[idx]
	if isinstance(rule, str):
		return rule
	elif len(rule) == 1:
		return ''.join(map(build, rule[0]))
	return '(?:' + '|'.join(''.join(map(build, r)) for r in rule) + ')'

# 8: 42 | 42 8 = 42+? 
# 11: 42 31 | 42 11 31 = 42 {n} 31 {n}
# loop n to 10 cuz I dunno max range should it be
res = 0
mainRule = re.compile(
	f"^(?:{build('42')})+?" \
+ 	"(?:" \
+ 	'|'.join( f"(?:{ build('42') }){{{n}}}(?:{ build('31') }){{{n}}}" for n in range(1, 10))
+ 	")$"
)
for line in data:
	if mainRule.match(line):
		res += 1
print(res)
