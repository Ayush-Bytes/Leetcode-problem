class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(ch) for ch in str(n))
        
        n = len(nums)
        # Pair each number with its digit sum, value, and original index
        arr = [(digit_sum(nums[i]), nums[i], i) for i in range(n)]
        
        # Sort based on digit sum, then by value
        arr.sort(key=lambda x: (x[0], x[1]))
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue
            
            # Count the size of the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = arr[curr][2]
                cycle_size += 1
                
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps