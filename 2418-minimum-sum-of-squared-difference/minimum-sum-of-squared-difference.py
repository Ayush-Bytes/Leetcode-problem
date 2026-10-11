from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        total_k = k1 + k2
        
        # Step 1: Find absolute differences and count their frequencies
        diff_counts = Counter(abs(n1 - n2) for n1, n2 in zip(nums1, nums2))
        max_diff = max(diff_counts.keys()) if diff_counts else 0
        
        # Step 2: Greedily reduce the largest differences
        current_max = max_diff
        while total_k > 0 and current_max > 0:
            count = diff_counts[current_max]
            if count <= total_k:
                # We can reduce all elements at 'current_max' down to 'current_max - 1'
                total_k -= count
                diff_counts[current_max] = 0
                diff_counts[current_max - 1] += count
                current_max -= 1
            else:
                # We can only reduce a portion of the elements at 'current_max'
                diff_counts[current_max] -= total_k
                diff_counts[current_max - 1] += total_k
                total_k = 0
                
        # Step 3: Calculate the final sum of squared differences
        result = 0
        for diff, count in diff_counts.items():
            if diff > 0:
                result += (diff ** 2) * count
                
        return result