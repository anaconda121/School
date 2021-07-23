# programming is not needed for this problem

import math

def imaginary(i):
    if (i % 5 == 0 || i % 3 == 0):
        return 0
    if (i % 4 == 0):
        return 1
    return -1
    
for i in range(68):
    coefficient = imaginary(i)
    middle_term = i * 1
    if (coefficient == 0):
        denominator = math.pow(40, k)
        print("V_", i, "[A,B] = [", 1, " , ", 1 / denominator, "]") 
    else:
        print("V_", i, "[A,B] = [", 1 + 1 / denominator, "]") 
