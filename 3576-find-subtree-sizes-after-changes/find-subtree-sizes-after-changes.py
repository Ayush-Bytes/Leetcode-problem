from collections import defaultdict
from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = defaultdict(list)
        for node in range(1, n):
            adj[parent[node]].append(node)

        new_parent = parent[:]
        last_seen = [-1] * 26

        def assign_parents(u: int) -> None:
            idx = ord(s[u]) - ord("a")
            prev_ancestor = last_seen[idx]

            if prev_ancestor != -1 and u != 0:
                new_parent[u] = prev_ancestor

            last_seen[idx] = u
            for v in adj[u]:
                assign_parents(v)
            last_seen[idx] = prev_ancestor

        assign_parents(0)

        new_adj = defaultdict(list)
        for node in range(1, n):
            new_adj[new_parent[node]].append(node)

        ans = [0] * n

        def calc_subtree_size(u: int) -> int:
            total = 1
            for v in new_adj[u]:
                total += calc_subtree_size(v)
            ans[u] = total
            return total

        calc_subtree_size(0)
        return ans