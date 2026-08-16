from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings
        strs = [str(num) for num in nums]
        
        # Custom comparator: compare x + y vs y + x
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Sort using custom comparator
        strs.sort(key=cmp_to_key(compare))
        
        # Handle edge case where the largest number is "0" (e.g., nums = [0, 0])
        result = "".join(strs)
        return "0" if result[0] == "0" else result