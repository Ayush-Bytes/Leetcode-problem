class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Suffix Minimum precompute karte hain
        suffMin = [0] * n
        suffMin[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffMin[i] = min(nums[i], suffMin[i + 1])
        
        # Prefix Maximum ko dynamic tarike se track karte hue check karte hain
        curr_max = float('-inf')
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            # Instability score check karte hain
            if curr_max - suffMin[i] <= k:
                return i
                
        return -1