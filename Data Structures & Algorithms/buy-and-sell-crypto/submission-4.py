class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force
        n, maxx = len(prices),0
        # for buy in range(n-1):
        #     for sell in range(buy+1,n):
        #         profit = prices[sell] - prices[buy]
        #         if profit>maxx: maxx = max(maxx,profit)
        # return maxx

        # 2 pointer sliding window of variable size, place l on buy, r on sell. if prices[r]>prices[l], we sell, else we change l to r
        l,r = 0,1
        while r<n:
            if prices[r]>prices[l]:
                maxx = max(maxx,prices[r]-prices[l])
            else:
                l = r
            r += 1
        return maxx