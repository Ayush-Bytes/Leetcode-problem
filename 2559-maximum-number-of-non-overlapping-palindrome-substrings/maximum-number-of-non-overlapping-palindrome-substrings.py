class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        # is_pal[i][j] will be True if s[i..j] is a palindrome
        is_pal = [[False] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            is_pal[i][i] = True
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1 or is_pal[i + 1][j - 1]:
                        is_pal[i][j] = True
        
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            
            # Option 2: Check if s[j...i-1] forms a valid palindrome of length >= k
            for j in range(i - k, -1, -1):
                if is_pal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    # Shortcut: length k or k+1 minimum valid length pick karna greedy standard hai
                    break
                    
        return dp[n]