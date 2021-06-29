from collections import Counter

class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = Counter({0: 1})
        cum = 0
        total = 0
        for num in nums:
            cum += num
            total += prefix_sum[cum - k]
            prefix_sum[cum] += 1

        return total


if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([1,1,1], 0))
    print(s.subarraySum([1, 2, 3], 3))