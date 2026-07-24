class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        
        # Step 1: Compute all unique pair XORs
        pair_xors = set()
        n = len(unique_nums)
        for i in range(n):
            for j in range(i, n):
                pair_xors.add(unique_nums[i] ^ unique_nums[j])
                
        # Step 2: Combine pair XORs with single elements to get triplet XORs
        triplet_xors = set()
        for p in pair_xors:
            for x in unique_nums:
                triplet_xors.add(p ^ x)
                
        return len(triplet_xors)