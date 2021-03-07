class Solution:
	'''
	503. Next Greater Element II
	Decrease stack
	'''
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # initialization
        result = [-1] * len(nums)
        decreaseStack = list()

        for idx, val in enumerate(nums * 2):
            if len(decreaseStack) == 0 or val <= decreaseStack[-1][1]:
                # if current number is no greater than the number
                # sitting on top of the stack, just push it into
                # the stack
                decreaseStack.append((idx, val))
            else:
                # pop the numbers from the stack while they are smaller
                # than current number, and mark them in the result array
                while len(decreaseStack) > 0 and val > decreaseStack[-1][1]:
                    poppedIdx, poppedVal = decreaseStack.pop()
                    result[poppedIdx % len(nums)] = val
                decreaseStack.append((idx, val))

        return result