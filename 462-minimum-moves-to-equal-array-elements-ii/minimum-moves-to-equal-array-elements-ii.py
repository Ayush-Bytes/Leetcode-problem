class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # Sort the array to find the median
        nums.sort()
        
        # The median element is at the middle index
        median = nums[len(nums) // 2]
        
        # Calculate total absolute differences from the median
        return sum(abs(num - median) for num in nums)