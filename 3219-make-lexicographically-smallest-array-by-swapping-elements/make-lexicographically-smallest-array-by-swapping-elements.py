class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # Pairs of (value, original_index) sorted by value
        sorted_pairs = sorted([(val, i) for i, val in enumerate(nums)])
        
        ans = [0] * n
        
        # Process in connected components/groups
        i = 0
        while i < n:
            j = i + 1
            while j < n and sorted_pairs[j][0] - sorted_pairs[j - 1][0] <= limit:
                j += 1
            
            indices = sorted([sorted_pairs[k][1] for k in range(i, j)])
            
            # Place the sorted values into these sorted indices
            for k in range(i, j):
                val = sorted_pairs[k][0]
                target_idx = indices[k - i]
                ans[target_idx] = val
            
            i = j
            
        return ans