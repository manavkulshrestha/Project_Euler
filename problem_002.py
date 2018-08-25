# Epiphany!
# 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# every 3rd number is even
# 2, 8, 34, 144

# Get fn in terms of fn_3 and fn_6 instead of fn_1 and fn_2

# fn_x means F sub n-x

# fn = fn_1 + fn_2
# 	 = fn_2+fn_3 + fn_3+fn_4
# 	 = 2*fn_3 + fn_2 + fn_4
# 	 = 2*fn_3 + fn_3+fn_4 + fn_5+fn_6
# 	 = 3*fn_3 + fn_4 + fn_5 + fn_6
# 	 = 4*fn_3 + fn_6

fn_1, fn_2, sum, max, = 2, 8, 10, 4000000
while True:
	fn_1, fn_2 = fn_2, 4*fn_2+fn_1
	if fn_2 > max:
		break
	sum += fn_2

print(sum)