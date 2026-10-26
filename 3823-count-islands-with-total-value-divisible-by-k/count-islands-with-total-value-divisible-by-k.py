from collections import deque
from typing import List


class Solution:

  def countIslands(self, grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    visited = [[False * n for _ in range(n)] for _ in range(m)]
    # Alternatively, you can modify the grid in-place instead of a visited matrix to save space:
    # visited = grid itself (change visited cells to 0)

    count = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for r in range(m):
      for c in range(n):
        if grid[r][c] > 0 and not visited[r][c]:
          island_sum = 0
          queue = deque([(r, c)])
          visited[r][c] = True

          while queue:
            row, col = queue.popleft()
            island_sum += grid[row][col]

            for dr, dc in directions:
              nr, nc = row + dr, col + dc
              if (
                  0 <= nr < m
                  and 0 <= nc < n
                  and grid[nr][nc] > 0
                  and not visited[nr][nc]
              ):
                visited[nr][nc] = True
                queue.append((nr, nc))

          if island_sum % k == 0:
            count += 1

    return count