class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [0] * k
        
        dp = [0] * k
        
        for num in nums:
            val = num % k
            new_dp = [0] * k
            new_dp[val] += 1
            
            for r in range(k):
                if dp[r] > 0:
                    new_dp[(r * val) % k] += dp[r]
            
            dp = new_dp
            
            # Accumulate the counts for each remainder from the current index's DP state
            for r in range(k):
                result[r] += dp[r]
                
        return result