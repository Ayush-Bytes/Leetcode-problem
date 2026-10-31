class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # Helper to simulate the exact movement and reflection starting from a cell in a given direction
        # dir: 0 -> moving right, 1 -> moving down
        def simulate(r, c, d):
            curr_r, curr_c = r, c
            while 0 <= curr_r < m and 0 <= curr_c < n and grid[curr_r][curr_c] == 1:
                if d == 0:  # entered moving right into a mirror -> turns down
                    d = 1
                    curr_r += 1
                else:       # entered moving down into a mirror -> turns right
                    d = 0
                    curr_c += 1
            
            if not (0 <= curr_r < m and 0 <= curr_c < n):
                return None
            return (curr_r, curr_c)

        # Precompute the next landing cell for every cell and initial direction (right=0, down=1)
        go = [[[None, None] for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    continue
                # Initial move right from (r, c) goes to (r, c+1)
                go[r][c][0] = simulate(r, c + 1, 0)
                # Initial move down from (r, c) goes to (r+1, c)
                go[r][c][1] = simulate(r + 1, c, 1)

        # DP table to count paths
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0 or grid[i][j] == 1:
                    continue
                
                # Try moving right
                nxt_right = go[i][j][0]
                if nxt_right:
                    nr, nc = nxt_right
                    dp[nr][nc] = (dp[nr][nc] + dp[i][j]) % MOD
                
                # Try moving down
                nxt_down = go[i][j][1]
                if nxt_down:
                    nr, nc = nxt_down
                    dp[nr][nc] = (dp[nr][nc] + dp[i][j]) % MOD
                    
        return dp[m - 1][n - 1]