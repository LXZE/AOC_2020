from itertools import combinations as combs
from functools import reduce
in_file = open('input_1.txt', 'r')
# in_file = open('test_1.txt', 'r')
numList = map(lambda x: int(x[:-1]), in_file.readlines())
target = 2020

numsList = combs(numList, 3)
for nums in numsList:
	if sum(nums) == target:
		print(reduce(lambda x,y: x*y, nums, 1))