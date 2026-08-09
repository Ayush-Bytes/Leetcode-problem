class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        # Suffix sums to quickly calculate total remaining stones from index i
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}

        def dp(i, m):
            # If we can take all remaining piles at once
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            if (i, m) in memo:
                return memo[(i, m)]
            
            min_opponent = float('inf')
            
            # Try taking X piles (1 <= X <= 2M)
            for x in range(1, 2 * m + 1):
                min_opponent = min(min_opponent, dp(i + x, max(m, x)))
            
            # Current player gets total remaining stones minus the opponent's best outcome
            memo[(i, m)] = suffix_sum[i] - min_opponent
            return memo[(i, m)]

        return dp(0, 1)