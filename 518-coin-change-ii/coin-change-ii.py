class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] represent karta hai ki amount 'i' banane ke kitne total combinations hain
        dp = [0] * (amount + 1)
        
        # Base case: 0 amount banane ka hamesha 1 tareeka hota hai (koi coin mat lo)
        dp[0] = 1
        
        # Unbounded Knapsack pattern:
        # Pehle coins ka loop chalayenge taaki duplicates/permutations count na ho (combos chahiye, permutations nahi)
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
                
        return dp[amount]