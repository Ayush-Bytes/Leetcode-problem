import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list: u -> list of (v, weight)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Min-heap stores: (total_weight, current_node, consecutive_count)
        # Start at node 0, initial weight 0, count 1 for labels[0]
        pq = [(0, 0, 1)]
        
        # dist[u][count] keeps track of the min weight to reach node u with a given streak count
        dist = {}
        
        while pq:
            w, u, count = heapq.heappop(pq)
            
            if u == n - 1:
                return w
                
            if (u, count) in dist and dist[(u, count)] < w:
                continue
            dist[(u, count)] = w
            
            for v, weight in adj[u]:
                # Determine next count based on label match
                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1
                    
                # If streak exceeds k, this path is invalid
                if next_count > k:
                    continue
                    
                next_w = w + weight
                
                if (v, next_count) not in dist or next_w < dist[(v, next_count)]:
                    dist[(v, next_count)] = next_w
                    heapq.heappush(pq, (next_w, v, next_count))
                    
        return -1