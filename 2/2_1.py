in_file = open('input_2.txt', 'r')
# in_file = open('test_2.txt', 'r')

def split(line):
	rules, v = line.split(': ')
	range, char = rules.split(' ')
	mini, maxi = map(int, range.split('-'))
	return [mini, maxi, char, v]

def isValid(s):
	mini, maxi, char, string = split(s)
	return mini <= string.count(char) <= maxi

res = 0
for line in in_file.readlines():
	if isValid(line[:-1]): res += 1
print(res)