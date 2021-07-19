x0 = 1

for i in range(500):
	if (i % 2 == 0):
		#even
		x0 = 1/2 * x0

	else:
		#odd
		x0 = 3 * x0 + 1

	print(x0)
