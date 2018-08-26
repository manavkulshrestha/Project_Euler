def smart_consecutive_sum(start, end):
	return ((start+end)*(end-start+1))//2

def smart_consecutive_square_sum(n):
	return n*(n+1)*(2*n+1)//6

sum = smart_consecutive_sum(1, 100)
print(sum*sum - smart_consecutive_square_sum(100))