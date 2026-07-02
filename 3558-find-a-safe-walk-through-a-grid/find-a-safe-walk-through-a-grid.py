from collections import deque

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        

        max_health = [[-1] * n for _ in range(m)]

        start_health = health - grid[0][0]

        if start_health <= 0:
            return False
            
        dq = deque([(0, 0, start_health)])
        max_health[0][0] = start_health
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while dq:
            r, c, h = dq.popleft()
 
            if r == m - 1 and c == n - 1:
                return True
                

            if h < max_health[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                
                if 0 <= nr < m and 0 <= nc < n:
                    next_health = h - grid[nr][nc]
                    
                    
                    if next_health > 0 and next_health > max_health[nr][nc]:
                        max_health[nr][nc] = next_health
                        
                      
                        if grid[nr][nc] == 0:
                            dq.appendleft((nr, nc, next_health))
                        else:
                            dq.append((nr, nc, next_health))
                            
        return max_health[m-1][n-1] >= 1