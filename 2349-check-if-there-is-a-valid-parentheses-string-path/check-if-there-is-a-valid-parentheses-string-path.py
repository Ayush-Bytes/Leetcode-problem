class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Pruning: Total path length must be even, and start/end must be valid.
        if (m + n - 1) % 2 != 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        # dp[r][c] will store the set of all possible balance values when reaching cell (r, c)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        start_val = 1 if grid[0][0] == '(' else -1
        dp[0][0].add(start_val)
        
        for r in range(m):
            for c in range(n):
                if not dp[r][c]:
                    continue
                
                # Try moving right
                if c + 1 < n:
                    val = 1 if grid[r][c + 1] == '(' else -1
                    for b in dp[r][c]:
                        new_b = b + val
                        if new_b >= 0:
                            dp[r][c + 1].add(new_b)
                            
                # Try moving down
                if r + 1 < m:
                    val = 1 if grid[r + 1][c] == '(' else -1
                    for b in dp[r][c]:
                        new_b = b + val
                        if new_b >= 0:
                            dp[r + 1][c].add(new_b)
                            
        return 0 in dp[m - 1][n - 1]