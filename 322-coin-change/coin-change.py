class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [[-1] * (amount + 1) for _ in range(n)]

        def calc(i, amount):
            if amount == 0:
                return 0
            
            if i < 0 or amount < 0:
                return float('inf')
            
            if dp[i][amount] != -1:
                return dp[i][amount]


            take = float('inf')
            if coins[i] <= amount:
                take = 1 + calc(i, amount - coins[i])

            ntake = calc(i - 1, amount)

            dp[i][amount] = min(take, ntake)
            return dp[i][amount]

        ans = calc(n - 1, amount)
        return ans if ans != float('inf') else -1
