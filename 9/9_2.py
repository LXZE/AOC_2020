from itertools import combinations as combi
in_file = open('input_9.txt', 'r'); preamble_size = 25
# in_file = open('test_9.txt', 'r'); preamble_size = 5

def calc_possible(data, current_index, pre_size):
	return list(map(lambda x: x[0]+x[1], combi(data[current_index-pre_size : current_index], 2)))

def solve(data, pre_size):
	for idx, n in enumerate(data[pre_size:]):
		if n not in calc_possible(data, idx+pre_size, pre_size):
			return n, idx+pre_size

def solve2(data, target):
	for i in range(len(data)):
		for j in range(i, len(data)):
			if sum(data[i:j]) == target:
				return min(data[i:j]) + max(data[i:j])

raw = list(map(lambda x: int(x.rstrip()), in_file.readlines()))
res1, target_idx = solve(raw, preamble_size)
raw = raw[:target_idx]
res = solve2(raw, res1)
print(res)




