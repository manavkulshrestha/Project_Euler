from math import sqrt
number = 600851475143

# def largest_factor(n):
# 	for i in range(int(n**.5),0,-1):
# 		if n%i == 0:
# 			return i

# #quicksort kinda implementation?
# def largest_prime_factor(n):
# 	_largest_factor = largest_factor(n)
# 	if _largest_factor == 1:
# 		return n
# 	else:
# 		one = largest_prime_factor(_largest_factor)
# 		two = largest_prime_factor(int(n/_largest_factor))
# 		return (one if (one > two) else two)

# print(largest_prime_factor(number))

## yeah, okay, but why?

# limit = int(sqrt(number))

# def prime(n):
# 	check_limit = int(sqrt(n))

# 	if n%2 == 0 and n != 2:
# 		return False
# 	if n%3 == 0 and n != 3:
# 		return False

# 	divisor, step = 5, 2
# 	while divisor <= check_limit:
# 		if n%divisor == 0:
# 			return False
# 		divisor += step
# 		step = 6-step
# 	return True

# for i in range(limit,1,-1):
# 	if number%i == 0 and prime(i):
# 		print(i)
# 		break

## Pretty good, but we can do better

def largest_prime_factor(n, divisor=2):
	while True:
		if n%divisor != 0:
			divisor += 1
		elif divisor > n//2:
			return n
		else:
			return largest_prime_factor(n//divisor,divisor=divisor)

print(largest_prime_factor(number))