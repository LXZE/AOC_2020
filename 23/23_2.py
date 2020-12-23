in_file = open('input_23.txt', 'r')
# in_file = open('test_23.txt', 'r')

cups = list(map(lambda x: x.rstrip(), in_file.readlines()))[0]
cups = list(map(int, list(cups)))

max_cup = 1000000
MAX = max(cups)

cups += list(range(MAX+1, max_cup+1))
MAX = max_cup
MIN = min(cups)

class Node: pass

nodes = [Node() for _ in cups]
for node, nextNode, cup in zip(nodes, nodes[1:] + [nodes[0]], cups):
	node.next = nextNode
	node.label = cup

lookup = {node.label: node for node in nodes}

current = nodes[0]
def shuffle():
	global current
	stack = current.next, current.next.next, current.next.next.next
	current.next = stack[-1].next

	destination = current.label - 1 if current.label > MIN else MAX
	while destination in list(map(lambda x: x.label, stack)):
		if destination > MIN:
			destination -= 1
		else:
			destination = MAX

	target = lookup[destination]
	stack[-1].next = target.next
	target.next = stack[0]
	current = current.next
moves = 10000000
for i in range(moves):
	shuffle()
print(lookup[1].next.label * lookup[1].next.next.label)
