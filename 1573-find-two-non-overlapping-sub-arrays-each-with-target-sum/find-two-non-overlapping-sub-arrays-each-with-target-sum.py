class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # min_len_left[i] stores the minimum length of a valid subarray ending at or before index i
        min_len_left = [float('inf')] * n
        
        prefix_sum = 0
        sum_to_index = {0: -1}
        min_len = float('inf')
        
        for i in range(n):
            prefix_sum += arr[i]
            need = prefix_sum - target
            if need in sum_to_index:
                end_idx = i
                start_idx = sum_to_index[need]
                curr_len = end_idx - start_idx
                min_len = min(min_len, curr_len)
            
            min_len_left[i] = min_len
            sum_to_index[prefix_sum] = i
            
        ans = float('inf')
        prefix_sum = 0
        sum_to_index = {0: n}
        min_len_right = float('inf')
        
        # Traverse from right to left to find the second non-overlapping subarray
        for i in range(n - 1, -1, -1):
            prefix_sum += arr[i]
            need = prefix_sum - target
            if need in sum_to_index:
                start_idx = i
                end_idx = sum_to_index[need]
                curr_len = end_idx - start_idx
                min_len_right = min(min_len_right, curr_len)
            
            sum_to_index[prefix_sum] = i
            
            # If there is a valid subarray to the left that doesn't overlap
            if i > 0 and min_len_left[i - 1] != float('inf') and min_len_right != float('inf'):
                ans = min(ans, min_len_left[i - 1] + min_len_right)
                
        return ans if ans != float('inf') else -1