from functools import reduce
in_file = open('input_18.txt', 'r')
# in_file = open('test_18.txt', 'r')

flatten = lambda t: [item for sublist in t for item in sublist]

def solve(eq):
	def calc(statement):
		stackNum = []
		stackOps = []
		for val in statement:
			if isinstance(val, int) and len(stackOps) > 0 and stackOps[-1] == '+':
				stackOps.pop()
				v = stackNum.pop()
				stackNum.append(v+val)
			elif isinstance(val, int):
				stackNum.append(val)
			else:
				stackOps.append(val)
		return reduce(lambda x, y: x*y, stackNum, 1)

	stack = []
	values = flatten(list(map(lambda x: list(x), eq.split(' '))))
	values = list(map(lambda x: int(x) if x.isnumeric() else x, values))
	for val in values:
		if val == ')':
			tmp = [')']
			while True:
				tmp.append(stack.pop())
				if tmp[-1] == '(':
					break
			stack.append(calc(tmp[::-1][1:-1]))
		else: stack.append(val)
	return calc(stack)

equations = list(map(lambda x: x.rstrip(), in_file.readlines()))
res = 0

for eq in equations:
	res += solve(eq)
print(res)