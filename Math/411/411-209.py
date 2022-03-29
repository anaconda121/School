n0 = 0
n1 = 1

for i in range(20):
	f_n = 0
	if (n0 == 0):
		f_n = 0
	else:
		f_n = n1 / n0
	print("N1: ", n1, "N0:" , n0, "D_n: ", n1 - n0, "F_n: ", f_n, "I: ", (i+1))
	n0 += n1
	n1 += n0