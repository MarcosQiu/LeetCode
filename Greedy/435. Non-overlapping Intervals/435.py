class Solution:
    def eraseOverlapIntervals(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        upper_boundary = float('-inf')
        discard_intervals = 0
        for start, end in sorted_intervals:
            if start >= upper_boundary:
                upper_boundary = end
            else:
                discard_intervals += 1

        return discard_intervals


if __name__ == '__main__':
    s = Solution()
    print(s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))