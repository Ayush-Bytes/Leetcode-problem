class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_left = (m + n + 1) // 2
        
        while low <= high:

            i = (low + high) // 2
            
            j = total_left - i
            

            nums1_left_max = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right_min = nums1[i] if i < m else float('inf')
            
            nums2_left_max = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right_min = nums2[j] if j < n else float('inf')

            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:

                if (m + n) % 2 == 1:
                    return float(max(nums1_left_max, nums2_left_max))
 
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0

            elif nums1_left_max > nums2_right_min:
                high = i - 1
            else:
                low = i + 1
                
        return 0.0