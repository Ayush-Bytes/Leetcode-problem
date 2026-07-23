class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        visited = set()
        def dfs(r,c):
            visited.add((r,c))
            count=1
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1 and (nr,nc)not in visited :
                    visited.add((nr,nc))
                    count += dfs(nr,nc)
            return count
        max_area=0
        for r in range(rows):
            for c in range (cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    max_area = max(max_area,dfs(r,c))
        return max_area
        