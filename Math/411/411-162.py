x0 = 1
y0 = 0
for i in range(12):
	xn = (0.8656025 * x0) - (0.5 * y0)
	yn = (0.5 * x0) + (0.866025 * y0)
	x0 = xn
	y0 = yn

print(x0, y0)
