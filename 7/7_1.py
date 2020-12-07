from collections import defaultdict as ddict
in_file = open('input_7.txt', 'r')
# in_file = open('test_7.txt', 'r')

def search(b_map, target_bag):
	to_find = [bag_key for bag_key, bag_val in b_map.items() if target in bag_val.keys()]
	uniq = set()
	while len(to_find) > 0:
		b = to_find.pop()
		uniq.add(b)
		for bag_key, bag_val in b_map.items():
			if b in bag_val.keys() and bag_key not in uniq:
				to_find.append(bag_key)
	return len(uniq)

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