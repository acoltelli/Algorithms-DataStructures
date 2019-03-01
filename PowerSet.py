#recursive
def powerset(arr):
    if not arr: return [[]]
    return powerset(arr[1:]) + [[arr[0]] + i for i in powerset(arr[1:])]



