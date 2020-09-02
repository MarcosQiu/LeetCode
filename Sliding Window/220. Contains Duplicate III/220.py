from sortedcontainers import SortedList

class Solution(object):
    """
    220. Contains Duplicate III
    To make sure that the pairs we found have indices difference
    at most k, we need to maintain a BST of size up to k + 1.
    Everytime we see a new number nums[i], we need to remove
    nums[i - k -1] from the BST. And then we look for numbers that
    fall in range [nums[i] - t, nums[i] + t]. If some numbers found,
    it would be a valid pair together with the new number nums[i]
    we saw.
    """
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # base case
        if (len(nums) == 0 or k <= 0 or t < 0):
            return False
        sortedWindow = SortedList()
        for index in range(len(nums)):
            if index > k:
                sortedWindow.remove(nums[index - k - 1])
            position_left = sortedWindow.bisect_left(nums[index] - t)
            position_right = sortedWindow.bisect_right(nums[index] + t)
            if position_left != position_right:
                return True
            sortedWindow.add(nums[index])
        return False