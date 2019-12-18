from timeit import *

#recursive
def nthFibonacci(n):
	if n == 0 or n == 1:
		return n
	else:
		return nthFibonacci(n-1) + nthFibonacci(n-2)


#memoization
def nthFibonacci_(n, memo ={0:0,1:1}):
    if n not in memo:
        memo[n] = nthFibonacci_(n-1) + nthFibonacci_(n-2) #compute recursively if val not already saved in memo
    return memo[n]



###tests


testRecurse = Timer("nthFibonacci(20)",
               "from __main__ import nthFibonacci")
testMemo = Timer("nthFibonacci_(20)",
                "from __main__ import nthFibonacci_")
testRecurse1 = Timer("nthFibonacci(50)",
               "from __main__ import nthFibonacci")
testMemo1 = Timer("nthFibonacci(50)",
                "from __main__ import nthFibonacci")



print testRecurse.timeit(number=10) #statement executed ten times
print testMemo.timeit(number=10)
# print testRecurse1.timeit(number=10)
print testMemo1.timeit(number=10)
