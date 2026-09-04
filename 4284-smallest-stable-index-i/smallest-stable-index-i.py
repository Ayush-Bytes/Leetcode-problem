class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Build suffix min array
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
            
        pref_max = float('-inf')
        
        # Traverse from left to right and find the first stable index
        for i in range(n):
            pref_max = max(pref_max, nums[i])
            if pref_max - suffix_min[i] <= k:
                return i
                
        return -1