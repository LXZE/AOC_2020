# in_file = open('input_25.txt', 'r')
in_file = open('test_25.txt', 'r')

cardPubKey, doorPubKey = list(map(lambda x: int(x.rstrip()), in_file.readlines()))
# print(cardPubKey, doorPubKey)

def multiplyAndMod(val, subjectNum):
	val *= subjectNum
	return val % 20201227

def findLoopSize(target):
	count = 0
	result = 1
	while result != target:
		result = multiplyAndMod(result, 7)
		count += 1
	return count

def transform(key, nLoop):
	result = 1
	for _ in range(nLoop):
		result = multiplyAndMod(result, key)
	return result
	
cardLoopSize = findLoopSize(cardPubKey)
doorLoopSize = findLoopSize(doorPubKey)

# print(cardLoopSize, doorLoopSize)

encKey1 = transform(cardPubKey, doorLoopSize)
encKey2 = transform(doorPubKey, cardLoopSize)
if encKey1 == encKey2:
	print(encKey1)