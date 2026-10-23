class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1
        for i, val in enumerate(nums):
            # If the element is not in its correct position
            if val != i:
                if k == -1:
                    k = val
                else:
                    k &= val
                    
        # If all elements were already in place
        return k if k != -1 else 0