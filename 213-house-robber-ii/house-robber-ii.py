class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base Cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def robSimple(houses: List[int]) -> int:
            prev2, prev1 = 0, 0
            for money in houses:
                curr = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = curr
            return prev1
        
        return max(robSimple(nums[:-1]), robSimple(nums[1:]))