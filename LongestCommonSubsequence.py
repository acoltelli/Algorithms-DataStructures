

#subsequences are not required to be consecutive elements 

#recursive
def lcs(X, Y, m, n): 
    if m == 0 or n == 0: return 0 
    if X[m-1] == Y[n-1]: 
       return 1 + lcs(X, Y, m-1, n-1); 
    else: 
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 




















