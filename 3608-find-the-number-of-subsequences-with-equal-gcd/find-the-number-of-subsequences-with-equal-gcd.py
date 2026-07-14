import math

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        max_val = max(nums)

        dp = {}
        dp[(0, 0)] = 1
        
        for num in nums:
            next_dp = dp.copy()
            for (g1, g2), count in dp.items():
                ng1 = math.gcd(g1, num)
                next_dp[(ng1, g2)] = (next_dp.get((ng1, g2), 0) + count) % MOD
                
                ng2 = math.gcd(g2, num)
                next_dp[(g1, ng2)] = (next_dp.get((g1, ng2), 0) + count) % MOD
                
            dp = next_dp
            
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 > 0:
                ans = (ans + count) % MOD
                
        return ans