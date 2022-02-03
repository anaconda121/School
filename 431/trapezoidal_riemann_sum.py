delta_x = 0.5 # width of trapezoidal segments

# ranges of riemann sum
a = 1 
b = 3

x_vals = [1, 1.5, 2, 2.5, 3, 3.5] # x values that are inputed into equation 

iterations = int((b-a) / delta_x)

ans = 0

def equation(x):
	return 1 / x

for i in range(iterations):
	# print(i, i+1, iterations)
	h1 = equation(x_vals[i])
	h2 = equation(x_vals[i+1])
	b = delta_x 

	ans += 1/2 * (h1+h2) * b

print(ans) 

# 1, 1.5
# 1.5, 2
# 2, 2.5
# 3, 3.5
