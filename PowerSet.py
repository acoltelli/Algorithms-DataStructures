# recursive
def powerset(arr):
    if not arr:
        return [[]]
    return powerset(arr[1:]) + [[arr[0]] + i for i in powerset(arr[1:])]


# iterative
# for every i in arr, the power set consists of the subsets that don't
# contain i, use the previous power set j,
# plus the subsets that do contain i, add [i] onto everything in the previous power set
def ps(arr):
    sol = [[]]
    for i in arr:
        sol.extend([j + [i] for j in sol])
    return sol


ps("noh")
# [[], ['n'], ['o'], ['n', 'o'], ['h'], ['n', 'h'], ['o', 'h'], ['n', 'o', 'h']]
ps("hah")
# [[], ['h'], ['a'], ['h', 'a'], ['h'], ['h', 'h'], ['a', 'h'], ['h', 'a', 'h']]
