def gcd(a, b):
	# Euclid's algorithm
	while b:      
		a, b = b, a%b
	return a

def lcm(a, b):
	return (a*b)//gcd(a,b)

def lcm_multiple(*args):
	_lcm = args[0]
	for arg in args[1:]:
		_lcm = lcm(_lcm, arg)
	return _lcm

print(lcm_multiple(*range(2,20)))