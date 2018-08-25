import timeit
import time

code = '''
n = 600851475143
i = 2
while i * i < n:
	while n % i == 0:
		n = n / i
	i = i + 1
'''

robinscode = '''
#This program calculates the largest prime factor of the number 600851475143.

def largestPrime(n):
    keepGoing = True
    divisor = 2
    
    while(keepGoing):
        if(n % divisor != 0):
            divisor = divisor + 1
        elif(divisor > (n / 2)):
            return n
        else:
            keepGoing = False
            return largestPrime(n / divisor)

largestPrime(600851475143)
'''

mycode = '''
number = 600851475143
def largest_prime_factor(n, divisor=2):
	while True:
		if n%divisor != 0:
			divisor += 1
		elif divisor > n//2:
			return n
		else:
			return largest_prime_factor(n//divisor,divisor=divisor)

largest_prime_factor(number)
'''

# print(timeit.timeit(stmt = code,number = 1))
print(f'Robin\'s code:\t{timeit.timeit(stmt = robinscode,number = 1000)}')
time.sleep(1)
print(f'My code:\t\t{timeit.timeit(stmt = mycode,number = 1000)}')
