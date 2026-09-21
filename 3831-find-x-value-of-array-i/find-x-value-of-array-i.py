class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [0] * k
        
        # dp[r] keeps track of the number of valid non-empty subarrays 
        # ending at the previous index that yield a product modulo k equal to r.
        dp = [0] * k
        
        for num in nums:
            val = num % k
            new_dp = [0] * k
            # A single-element subarray containing just the current number
            new_dp[val] += 1
            
            # Extend all valid subarrays ending at the previous index
            for r in range(k):
                if dp[r] > 0:
                    new_dp[(r * val) % k] += dp[r]
            
            dp = new_dp
            
            # Accumulate the counts for each remainder from the current index's DP state
            for r in range(k):
                result[r] += dp[r]
                
        return result