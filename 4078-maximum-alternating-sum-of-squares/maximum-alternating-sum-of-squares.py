class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Step 1: Take absolute values and sort them
        arr = sorted(abs(x) for x in nums)
        n = len(arr)
        
        # Step 2: The first half gets subtracted, the second half gets added
        mid = n // 2
        
        # Elements from 0 to mid-1 are subtracted (odd positions in alternating sum)
        total_sum = sum(x * x for x in arr[mid:]) - sum(x * x for x in arr[:mid])
        
        return total_sum