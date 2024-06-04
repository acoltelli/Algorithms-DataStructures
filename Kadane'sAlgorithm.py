def maxSubArray(nums):
    maxSubUpToHere = maxTotal = nums[0]  # pick first element as initial max sub
    for i in nums[1:]:
        # maximum subarray is either the current element
        # or the current element combined with the previous maximum subarray
        maxSubUpToHere = max(i, maxSubUpToHere + i)
        maxTotal = max(maxTotal, maxSubUpToHere)
    return maxTotal
