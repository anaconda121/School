import math

x0 = 2.4
n = 4
xN = 0

def f_prime(x):
	return 1 - math.cos(x)

def f(x):
	return x - math.sin(x) - 0.5

for i in range(n):
	xN = x0 - (f(x0)/f_prime(x0))
	x0 = xN
	print(xN)
