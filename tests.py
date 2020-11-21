range1 = 6
range2 = 7

for i in range(1, range1):
	for j in range(1, range2):

		array = [ [ [] for k in range(1, range1) ] for l in range(1, range2) ]
		array[i-1].append(f'hola {i}')
print(array)