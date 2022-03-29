import math
import numpy as np 

# euler's method
# y_n+1 = y_n + h(f'(x))

h = 0.1 # step size 
x_val_wanted = 1
iterations = int(x_val_wanted / h)

x0 = 0.36

yn = x0
f_prime = 0.18432

vals = []
vals = [0 for i in range((iterations+1))]

vals[0] = x0 
for i in range(iterations):
	vals[i + 1] = vals[i] + ((0.8 * (vals[i])) * (1 - vals[i]) * (h))
	print(vals[i+1])
