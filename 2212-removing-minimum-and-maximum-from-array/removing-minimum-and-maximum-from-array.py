class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        # Find indices of min and max elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        # Ensure i is the smaller index and j is the larger index
        i, j = min(min_idx, max_idx), max(min_idx, max_idx)
        
        # Scenario 1: Remove both from the front
        option1 = j + 1
        
        # Scenario 2: Remove both from the back
        option2 = n - i
        
        # Scenario 3: Remove one from front and one from back
        option3 = (i + 1) + (n - j)
        
        return min(option1, option2, option3)