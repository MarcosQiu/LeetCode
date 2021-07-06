class Solution:
    def candy(self, ratings):
        candies = [1] * len(ratings)
        for idx in range(len(ratings) - 1):
            if ratings[idx] < ratings[idx + 1]:
                candies[idx + 1] = candies[idx] + 1

        for idx in range(len(ratings) - 1, 0, -1):
            if ratings[idx - 1] > ratings[idx]:
                candies[idx - 1] = max(candies[idx - 1], candies[idx] + 1)

        return sum(candies)


if __name__ == '__main__':
    s = Solution()
    print(s.candy([1, 0, 2]))
    print(s.candy([1, 2, 2]))
