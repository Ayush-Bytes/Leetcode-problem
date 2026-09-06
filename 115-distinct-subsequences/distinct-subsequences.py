class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # If s is shorter than t, it's impossible to form t
        if m < n:
            return 0
            
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty string t can always be formed once
        
        for char in s:
            # Iterate backwards to avoid using the updated DP values from the current iteration
            for j in range(n, 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]