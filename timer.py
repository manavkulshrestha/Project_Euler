import timeit
import time

code1 = '''
def is_palindrome(n):
	str_n = str(n)
	return (str_n[::-1] == str_n)
is_palindrome(9009)
'''

code2 = '''
def is_palindrome(n):
	reverse, original = 0, n

	while original > 0:
		reverse = reverse*10 + original%10;
		original //= 10

	return n == reverse;
is_palindrome(9009)
'''

# print(timeit.timeit(stmt = code,number = 1))
# print(f'code 2:\t{timeit.timeit(stmt = code2,number = 1000000)}')
# time.sleep(5)
print(f'code 1:\t{timeit.timeit(stmt = code1,number = 1000000)}')
time.sleep(5)
print(f'code 2:\t{timeit.timeit(stmt = code2,number = 1000000)}')
