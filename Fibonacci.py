
#recursive
def nthFibonacci(n):
	if n == 0 or n == 1:
		return n 
	else:
		return nthFibonacci(n-1) + nthFibonacci(n-2)



#memoization
memo = {0: 0, 1: 1}
def nthFibonacci_(n):
    if n not in memo:
        nthval = nthFibonacci_(n-1) + nthFibonacci_(n-2)
        memo[n] = nthval
    return memo[n]

print nthFibonacci(10)
print nthFibonacci_(10)