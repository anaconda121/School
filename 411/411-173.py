import math

def imaginary(i):
	if (i % 4 == 0):
		return 1
	if (i % 2 == 0):
		return -1

done = False
n = 2

while (done == False):
	ans = 1.0
	for x in range(2, n+1, 2):
		b = imaginary(x)
		ans += math.comb(n, x) * (b / math.pow(10, x))
		
	if (ans <= 0.0):
		print("ANSWER: ", n)
		done = True
	
	n += 1
