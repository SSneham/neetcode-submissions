class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        def dfs(ind,amount):
            if ind == 0:
                if amount%coins[ind] == 0:
                    return amount//coins[ind]
                else:
                    return 1e9
            # normal case
            notTake = dfs(ind-1, amount)
            take = 1e9
            if coins[ind] <= amount:
                take = 1 + dfs(ind, amount - coins[ind])
            return min(notTake, take)
        ans = dfs(n-1,amount)
        return ans if ans != 1e9 else -1

