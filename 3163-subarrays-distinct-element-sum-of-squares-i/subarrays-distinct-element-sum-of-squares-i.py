class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        for i in range(n):
            distinct_set = set()
            for j in range(i, n):
                distinct_set.add(nums[j])
                total_sum += len(distinct_set) ** 2
                
        return total_sum