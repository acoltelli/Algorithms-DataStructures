def nextGreaterElement(nums):
    stack = []
    result = [None] * len(nums)

    for i, num in enumerate(nums):
        # While stack is not empty and current num is greater than the element
        # at the index on top of the stack, pop the stack and update result
        while stack and nums[stack[-1]] < num:
            top_index = stack.pop()
            result[top_index] = num
        # Push current index onto the stack
        stack.append(i)

    return result


nums = [2, 1, 2, 4, 3]
print(nextGreaterElement(nums))
