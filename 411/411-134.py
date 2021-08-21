import math

x0 = 1.0
for i in range(100):
	xn = math.cos(x0)
	x0 = xn
	print(xn)