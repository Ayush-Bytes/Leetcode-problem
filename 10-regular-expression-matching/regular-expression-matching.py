class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] will be True if s[i:] matches p[j:]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string matches empty pattern
        dp[m][n] = True
        
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                # Check if current characters match
                first_match = i < m and (p[j] == s[i] or p[j] == '.')
                
                if j + 1 < n and p[j + 1] == '*':
                    # Two choices with '*':
                    # 1. Skip the '#' and '*' (match 0 occurrences): dp[i][j+2]
                    # 2. Use '*' to match current character if first_match: dp[i+1][j]
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    # Regular character or '.' match
                    dp[i][j] = first_match and dp[i + 1][j + 1]
                    
        return dp[0][0]