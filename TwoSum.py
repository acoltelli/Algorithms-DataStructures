from collections import *


def twoSum(nums, target):
    var = Counter(nums)
    for i in nums:
        diff = target - i
        if diff in var.keys():
            if i != diff:
                return nums.index(i), nums.index(target - i)
            if var[diff] == 2:
                return [i for i, x in enumerate(nums) if x == diff]
