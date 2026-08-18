class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}

        def f(res):
            if res == target:
                return 1
            if res in dp:
                return dp[res]

            count = 0

            for num in nums:
                if res + num <= target:
                    count += f(res+num)
            dp[res] = count
            return count
        return f(0)

            