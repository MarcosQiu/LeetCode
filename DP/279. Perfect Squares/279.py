from math import floor, sqrt


class Solution:
    def numSquares(self, n):
        candidates = [i ** 2 for i in range(1, floor(sqrt(n)) + 1)]
        least_perfect_square = list(range(n + 1))
        for idx in range(1, len(least_perfect_square)):
            least_perfect_square[idx] = min([least_perfect_square[idx - candidate] + 1 for candidate in candidates if idx - candidate >= 0])

        return least_perfect_square[-1]


if __name__ == '__main__':
    s = Solution()
    s.numSquares(12)