class Solution:
    NEG_INF = -999999999999
    def maxProfit(self, prices):
        sell = [0] * len(prices)
        buy = [0] * len(prices)
        hold = [0] * len(prices)
        cool_down = [0] * len(prices)

        buy[0] = -prices[0]
        sell[0] = self.NEG_INF
        hold[0] = self.NEG_INF
        cool_down[0] = 0

        for day in range(1, len(prices)):
            buy[day] = cool_down[day - 1] - prices[day]
            sell[day] = max(buy[day - 1], hold[day - 1]) + prices[day]
            hold[day] = max(hold[day - 1], buy[day - 1])
            cool_down[day] = max(cool_down[day - 1], sell[day - 1])

        return max([
            buy[-1],
            sell[-1],
            hold[-1],
            cool_down[-1]
        ])
