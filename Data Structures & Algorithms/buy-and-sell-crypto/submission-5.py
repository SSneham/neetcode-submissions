class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        n = len(prices)
        profit = 0

        for r in range(1,n):
            buy = prices[l]
            sell = prices[r]
            if sell>buy:
                profit = max(profit, sell-buy)
            else:
                l = r
        return profit