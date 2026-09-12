from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Append original index to each interval
        indexed_intervals = []
        for idx, (l, r, w) in enumerate(intervals):
            indexed_intervals.append((l, r, w, idx))
        
        # Sort by right endpoint
        indexed_intervals.sort(key=lambda x: x[1])
        
        rights = [interval[1] for interval in indexed_intervals]
        
        # memoization for DP: dp(i, count) -> returns (max_weight, list_of_indices)
        memo = {}
        
        def solve(i, count):
            if count == 0 or i < 0:
                return 0, []
            
            if (i, count) in memo:
                return memo[(i, count)]
            
            # Option 1: Skip the current interval
            res1_weight, res1_indices = solve(i - 1, count)
            
            # Option 2: Take the current interval
            l, r, w, orig_idx = indexed_intervals[i]
            
            # Find the latest interval that ends before current interval's start 'l'
            # Using binary search on right endpoints
            # We want the largest index j such that indexed_intervals[j][1] < l
            # bisect_right on rights gives the insertion point, so we subtract 1
            j = bisect_right(rights, l - 1) - 1
            
            prev_weight, prev_indices = solve(j, count - 1)
            take_weight = w + prev_weight
            take_indices = prev_indices + [orig_idx]
            
            # Compare options to get maximum weight and lexicographically smallest indices
            if take_weight > res1_weight:
                best = (take_weight, sorted(take_indices))
            elif take_weight < res1_weight:
                best = (res1_weight, sorted(res1_indices))
            else:
                # Weights are equal; choose lexicographically smaller index array
                best = (take_weight, sorted(take_indices) if sorted(take_indices) < sorted(res1_indices) else sorted(res1_indices))
                
            memo[(i, count)] = best
            return best

        _, best_indices = solve(n - 1, 4)
        return best_indices