class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_val = max(nums)
        points = [0] * (max_val + 1)
        
        for num in nums:
            points[num] += num
            
        prev2 = 0
        prev1 = 0
        
        for i in range(max_val + 1):
            curr = max(prev1, prev2 + points[i])
            prev2 = prev1
            prev1 = curr
            
        return prev1