class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        k = k % total_elements
        
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                flat_index = i * n + j
                
                new_flat_index = (flat_index + k) % total_elements
                
                new_r = new_flat_index // n
                
                new_c = new_flat_index % n
                
                result[new_r][new_c] = grid[i][j]
                
        return result