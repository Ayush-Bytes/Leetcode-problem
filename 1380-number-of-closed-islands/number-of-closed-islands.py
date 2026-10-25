class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Out of bounds or if it's water (1), stop
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return
            
            # Mark the current land cell as visited by turning it into water (1)
            grid[r][c] = 1
            
            # Explore all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Step 1: Flood-fill (sink) all 0s connected to the top and bottom borders
        for c in range(cols):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[rows - 1][c] == 0:
                dfs(rows - 1, c)
                
        # Step 2: Flood-fill (sink) all 0s connected to the left and right borders
        for r in range(rows):
            if grid[r][0] == 0:
                dfs(r, 0)
            if grid[r][cols - 1] == 0:
                dfs(r, cols - 1)
                
        # Step 3: Count the remaining closed islands
        closed_islands_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    closed_islands_count += 1
                    dfs(r, c) # Sink this entire closed island
                    
        return closed_islands_count