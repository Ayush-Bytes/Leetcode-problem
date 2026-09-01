from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_r = start_c = -1
        litter_coords = []
        
        # Grid parse karke Start aur Litter locations nikalna
        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]
                if ch == 'S':
                    start_r, start_c = r, c
                elif ch == 'L':
                    litter_coords.append((r, c))
        
        num_litters = len(litter_coords)
        full_mask = (1 << num_litters) - 1
        
        # Map litter coordinates to bit index
        litter_map = {pos: i for i, pos in enumerate(litter_coords)}
        
        # BFS Queue: (r, c, mask, e, steps)
        queue = deque([(start_r, start_c, 0, energy, 0)])
        
        # best_energy[r][c][mask] -> maximum energy remaining at (r, c, mask)
        best_energy = {}
        best_energy[(start_r, start_c, 0)] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, e, steps = queue.popleft()
            
            # Agar sabhi litter collect ho gaye
            if mask == full_mask:
                return steps
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries and obstacles
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    ne = e - 1
                    if ne < 0:
                        continue  # Out of energy
                    
                    cell = classroom[nr][nc]
                    nmask = mask
                    
                    # Reset energy if standing on 'R'
                    if cell == 'R':
                        ne = energy
                    # Collect litter if standing on 'L'
                    elif cell == 'L':
                        if (nr, nc) in litter_map:
                            nmask |= (1 << litter_map[(nr, nc)])
                    
                    # State pruning: Only visit if we have strictly more energy than before
                    state = (nr, nc, nmask)
                    if ne > best_energy.get(state, -1):
                        best_energy[state] = ne
                        queue.append((nr, nc, nmask, ne, steps + 1))
                        
        return -1