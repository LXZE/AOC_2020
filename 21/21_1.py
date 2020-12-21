from collections import defaultdict as ddict

in_file = open('input_21.txt', 'r')
# in_file = open('test_21.txt', 'r')

rawInfo = list(map(lambda x: x.rstrip(), in_file.readlines()))
ingredients = []
allergences = []
for info in rawInfo:
	stuffs, allergy = info.split(' (')
	allergy = allergy[:-1]
	stuffs = stuffs.split(' ')
	allergy = allergy.split(' ')
	allergy = (' '.join(allergy[1:])).split(', ')
	ingredients.append(stuffs)
	allergences.append(allergy)

allergicToIngredient = ddict(set)
allIngredient = set()
for stuffs, allergence in zip(ingredients, allergences):
	for a in allergence:
		if a not in allergicToIngredient.keys():
			allergicToIngredient[a] = set(stuffs)
		else:
			allergicToIngredient[a] &= set(stuffs)
	allIngredient |= set(stuffs)

for allergics in allergicToIngredient.values():
	for a in allergics:
		allIngredient.discard(a)

res = 0
for ingredient in allIngredient:
	for stuffs in ingredients:
		res += stuffs.count(ingredient)
print(res)