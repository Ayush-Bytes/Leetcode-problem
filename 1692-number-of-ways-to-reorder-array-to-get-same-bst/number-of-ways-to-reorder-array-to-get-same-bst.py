import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def helper(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # math.comb(n, k) calculates combinations nCk
            ways_left = helper(left)
            ways_right = helper(right)
            
            combined_ways = math.comb(len(left) + len(right), len(left))
            
            return (combined_ways * ways_left * ways_right) % MOD

        # Subtract 1 because the problem asks for *reorderings* (excluding the original array itself)
        return (helper(nums) - 1 + MOD) % MOD