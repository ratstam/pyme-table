import random

# range1 = 6
# range2 = 7

# for i in range(1, range1):
# 	for j in range(1, range2):

# 		array = [ [ [] for k in range(1, range1) ] for l in range(1, range2) ]
# 		array[i-1].append(f'hola {i}')
# print(array)


population = ['a', 'b', 'c']

while len(population) > 0:
	random_sample = random.choice(population)
	population.remove(random_sample)
	print(random_sample)
