class Solution:
    def findDuplicate(self, nums):
        slow_idx = fast_idx = 0
        while True:
            slow_idx = nums[slow_idx]
            fast_idx = nums[nums[fast_idx]]
            if slow_idx == fast_idx:
                break

        fast_idx = 0
        while slow_idx != fast_idx:
            slow_idx = nums[slow_idx]
            fast_idx = nums[fast_idx]

        return slow_idx


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicate([1,3,4,2,2]))