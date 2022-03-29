#source = https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-12.php
def permute(nums):
	result_perms = [[]]
	for n in nums:
		new_perms = []
		for perm in result_perms:
			for i in range(len(perm)+1):
				new_perms.append(perm[:i] + [n] + perm[i:])
				result_perms = new_perms
	return result_perms		

def possible_dimensions(a, b, c, d):
	#lil check before brute force commences
	if (a > c):
		print("c > a for this example, you can just switch the values of a and c. im too lazy to write another version")
	else:
		nums = [a,b,c,d]
		results = permute(nums)
		possible_side_configs = [[]]

		for i in range (len(results)):
			#giving values to side lengths of triangle
			t1 = results[i][2] - results[i][0] #c-a
			t2 = results[i][1] #b
			t3 = results[i][3] #d

			#check for triangle-inequality thm
			nums = [t1,t2,t3]
			possible_side_configs = permute(nums)
			perm_counter = 0

			for j in range(len(possible_side_configs)):
				if (possible_side_configs[j][0] + possible_side_configs[j][1] > possible_side_configs[j][2]):
					if (possible_side_configs[j][1] + possible_side_configs[j][2] > possible_side_configs[j][0]):
						if (possible_side_configs[j][2] + possible_side_configs[j][0] > possible_side_configs[j][1]):

							if (possible_side_configs[2] > possible_side_configs[0] and possible_side_configs[2] > possible_side_configs[1]):
								print(results[i])
								perm_counter += 1

possible_dimensions(7,5,11,3)