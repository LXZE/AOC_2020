from collections import defaultdict as ddict
in_file = open('input_7.txt', 'r')
# in_file = open('test_7.txt', 'r')

def search(b_map, target_bag):
	count = 0
	to_find = list(b_map[target_bag].items())
	def loop(bag):
		if bag[0] == 'no other': return 0
		tmp = 0
		for new in list(b_map[bag[0]].items()):
			tmp += loop(new)
		return bag[1] + (bag[1]*tmp)

	for b in to_find:
		count += loop(b)
	return count

def get_color(val):
	if val[0] == 'n':
		return val[:-5]
	return ' '.join(val.split(' ')[1:3])

res = 0
raw = list(map(lambda x: x.rstrip(), in_file.readlines()))
tmp = []
bag_map = ddict(lambda: ddict(int))
target = 'shiny gold'
for line in raw:
	[parent, childs] = line.split(' contain ')
	for child in childs[:-1].split(', '):
		bag_map[parent[:-5]][get_color(child)] = int(child[0]) if child[0] != 'n' else 0
res = search(bag_map, target)
print(res)