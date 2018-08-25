# 1000^2 = 1000000 so, number of digits is 6

def is_palindrome(n):
	reverse, original = 0, n

	while original > 0:
		reverse = reverse*10 + original%10;
		original //= 10

	return n == reverse;

print(is_palindrome(9009))