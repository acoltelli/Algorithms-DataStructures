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


# backtracking
def power_set(nums):
    power_set = []

    def backtrack(start_index, subset):
        power_set.append(subset[:])  # append copy of current subset
        for index in range(start_index, len(nums)):
            subset.append(nums[index])  # include nums[i] in the subset
            backtrack(index + 1, subset)  # move forward to build the subset
            subset.pop()  # backtrack to explore subsets without nums[i]

    backtrack(0, [])
    return power_set


print(power_set(["n", "o", "h"]))
# [[], ['n'], ['o'], ['n', 'o'], ['h'], ['n', 'h'], ['o', 'h'], ['n', 'o', 'h']]
