import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        res = []
        if not nums1 or not nums2 or k <= 0:
            return res
        
        # Min-heap stores tuples of: (sum, index_in_nums1, index_in_nums2)
        min_heap = []
        
        # Push initial pairs (nums1[i], nums2[0]) up to min(k, len(nums1))
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        # Pop the smallest sum pair and push the next pair from nums2
        while min_heap and len(res) < k:
            val, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])
            
            # If there's a next element in nums2 for the current nums1[i], push it
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                
        return res