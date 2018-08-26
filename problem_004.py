# 1000^2 = 1000000 so, number of digits is 6

def is_palindrome(n):
	str_n = str(n)
	return (str_n[::-1] == str_n)

maximum = -1

for i in range(999,99,-1):
	for j in range(999,99,-1):
		product = i*j
		if is_palindrome(product) and product > maximum:
			maximum = product

print('No palindrome in range' if maximum == -1 else maximum)


