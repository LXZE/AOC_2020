from itertools import combinations as combi
in_file = open('input_9.txt', 'r'); preamble_size = 25
# in_file = open('test_9.txt', 'r'); preamble_size = 5

def calc_possible(data, current_index, pre_size):
	return list(map(lambda x: x[0]+x[1], combi(data[current_index-pre_size : current_index], 2)))

def solve(data, pre_size):
	for idx, n in enumerate(data[pre_size:]):
		possible_num = calc_possible(data, idx+pre_size, pre_size)
		# print(possible_num, idx+pre_size)
		if n not in possible_num:
			return n

raw = list(map(lambda x: int(x.rstrip()), in_file.readlines()))
res = solve(raw, preamble_size)
print(res)

