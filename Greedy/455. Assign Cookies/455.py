import heapq

class Solution:
    def findContentChildren(self, g, s):
        greedy = g[:]
        size = s[:]
        heapq.heapify(greedy)
        heapq.heapify(size)

        children_fed = 0
        while len(greedy) > 0 and len(size) > 0:
            while len(size) > 0 and size[0] < greedy[0]:
                heapq.heappop(size)
            if len(size) > 0:
                children_fed += 1
                heapq.heappop(greedy)
                heapq.heappop(size)

        return  children_fed


if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren([1, 2, 3], [1, 1]))
    print(s.findContentChildren([1, 2], [1, 2, 3]))

