from timeit import *


#subsequences are not required to be consecutive elements
#recursive
def lcs(str1, str2, m, n):
    if m == 0 or n == 0: return 0
    if str1[m-1] == str2[n-1]:
       return 1 + lcs(st1, str2, m-1, n-1);
    else:
       return max(lcs(str1, str2, m, n-1), lcs(str1, str2, m-1, n)); 



# memoization
def lcs_(X , Y):
    memo = [[None]*(len(Y)+1) for i in range(len(X)+1)] #create matrix memo, initially filled with None
  	#build matrix from bottom up, memo[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]

    for i in range(len(X)+1):
        for j in range(len(Y)+1):
            if i == 0 or j == 0 :
                memo[i][j] = 0
            elif X[i-1] == Y[j-1]:
                memo[i][j] = memo[i-1][j-1]+1
            else:
                memo[i][j] = max(memo[i-1][j] , memo[i][j-1])
    return memo[len(X)][len(Y)] # return bottom right most element of matrix


#########

testRecurse = Timer("lcs('sailboat', 'bgtosetgagerrt', 8, 14)",
               "from __main__ import lcs")
testMemo = Timer("lcs_('sailboat', 'bgtosetgagerrt')",
                "from __main__ import lcs_")
testMemo1 = Timer("lcs_('WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS', 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC')",
                "from __main__ import lcs_")
# testRecurse1 = Timer("lcs('WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS', 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC', 50, 50)",
#                 "from __main__ import lcs")


print testRecurse.timeit(number=10)
print testMemo.timeit(number=10)
# print testRecurse1.timeit(number=1)
print testMemo1.timeit(number=1)
