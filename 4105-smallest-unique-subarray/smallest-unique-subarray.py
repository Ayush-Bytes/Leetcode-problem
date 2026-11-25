from collections import Counter
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        base = 100003
        mod = 10**9 + 7

        # Precompute powers of base mod m
        power = [1] * (n + 1)
        for i in range(1, n + 1):
            power[i] = (power[i - 1] * base) % mod

        def has_unique_of_len(length: int) -> bool:
            if length > n:
                return False

            # Initial window hash of size `length`
            h = 0
            for i in range(length):
                h = (h * base + nums[i]) % mod

            freq = Counter([h])
            high_pow = power[length - 1]

            # Slide window across nums
            for i in range(length, n):
                left_val = (nums[i - length] * high_pow) % mod
                h = (h - left_val + mod) % mod
                h = (h * base + nums[i]) % mod
                freq[h] += 1

            return any(count == 1 for count in freq.values())

        low, high = 1, n
        ans = n

        while low <= high:
            mid = (low + high) // 2
            if has_unique_of_len(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans