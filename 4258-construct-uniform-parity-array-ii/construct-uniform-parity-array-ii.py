class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Step 1: Find the minimum odd number in the array
        min_odd = float('inf')
        for x in nums1:
            if x % 2 != 0:
                min_odd = min(min_odd, x)
        
        # If there are no odd numbers, all elements are already EVEN.
        if min_odd == float('inf'):
            return True
        
        # Step 2: If odd numbers exist, we check if we can make all elements ODD.
        # For every even number, there must exist an odd number smaller than it.
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False
                
        return True