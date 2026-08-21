import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        # Helper function: Count numbers <= x that are multiples of at least one coin
        def count_valid(x: int) -> int:
            total_count = 0
            # Iterate through all non-empty subsets using bitmasking
            for mask in range(1, 1 << n):
                lcm_val = 1
                set_bits = 0
                for i in range(n):
                    if (mask >> i) & 1:
                        set_bits += 1
                        lcm_val = math.lcm(lcm_val, coins[i])
                        if lcm_val > x:  # Optimization to avoid huge numbers
                            break
                
                if lcm_val <= x:
                    if set_bits % 2 == 1:
                        total_count += x // lcm_val
                    else:
                        total_count -= x // lcm_val
                        
            return total_count

        # Binary search bounds
        low = 1
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_valid(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans