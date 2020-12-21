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
for stuffs, allergence in zip(ingredients, allergences):
	for a in allergence:
		if a not in allergicToIngredient.keys():
			allergicToIngredient[a] = set(stuffs)
		else:
			allergicToIngredient[a] &= set(stuffs)

allergicList = dict()
while len(allergicToIngredient.keys()) > 0:
	targetAllergic = list(filter(lambda x: len(x[1]) == 1, allergicToIngredient.items()))[0]
	allergicList[targetAllergic[0]] = list(targetAllergic[1])[0]
	del allergicToIngredient[targetAllergic[0]]
	for key in allergicToIngredient.keys():
		allergicToIngredient[key].discard(allergicList[targetAllergic[0]])

res = []
for key in sorted(allergicList.keys()):
	res.append(allergicList[key])
print(','.join(res))
