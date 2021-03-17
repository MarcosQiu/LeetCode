class Solution:
    '''
    115. Distinct Subsequences
    dynamic programming
    '''
    def numDistinct(self, s: str, t: str) -> int:
        # cover the edge cases
        if t == '':
            return 1
        if s == '':
            return 0

        distinct_nums = list()
        for _ in range(len(t)):
            distinct_nums.append([0] * len(s))

        # initialise the first line
        for idx in range(len(s)):
            if s[idx] == t[0]:
                distinct_nums[0][idx] = (distinct_nums[0][idx - 1] + 1) if idx > 0 else 1
            else:
                distinct_nums[0][idx] = distinct_nums[0][idx - 1] if idx > 0 else 0

        # from left to right, top to down, fill the matrix
        for i in range(1, len(t)):
            for j in range(1, len(s)):
                distinct_nums[i][j] = distinct_nums[i][j - 1]
                if s[j] == t[i]:
                    distinct_nums[i][j] += distinct_nums[i - 1][j - 1]

        return distinct_nums[-1][-1]