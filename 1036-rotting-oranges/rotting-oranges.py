class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dq=deque()
        visited = set()
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        fresh_orange=0
        for r in range (rows):
            for c in range(cols):
                if grid[r][c]==2:
                    dq.append((r,c))
                    visited.add((r,c))
                elif grid[r][c]==1:
                    fresh_orange+=1
        
        minutes = 0
        while dq and fresh_orange>0:
            lq = len(dq)
            for _ in range(lq):
                r,c=dq.popleft()
                for dr,dc in directions:
                    nr=r+dr
                    nc = c+dc
                    if 0 <= nr < rows and 0<=nc<cols and grid[nr][nc]==1 and (nr,nc) not in visited:
                        grid[nr][nc]=2
                        visited.add((nr,nc))
                        fresh_orange -=1
                        dq.append((nr,nc))
            minutes +=1
        if fresh_orange==0:
            return minutes
        return -1
