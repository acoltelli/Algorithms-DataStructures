
#recursive
def nthFibonacci(n):
	if n == 0 or n == 1:
		return n 
	else:
		return nthFibonacci(n-1) + nthFibonacci(n-2)


#memoization
def nthFibonacci_(n, memo ={0:0,1:1}):
    if n not in memo:
        nthval = nthFibonacci_(n-1) + nthFibonacci_(n-2) #compute recursively if val not already saved in memo
        memo[n] = nthval #save this computed number in memo
    return memo[n]











