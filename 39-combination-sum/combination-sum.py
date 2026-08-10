class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(start_idx, current_combination, current_sum):
            # Base case: if current sum equals target, we found a valid combination
            if current_sum == target:
                res.append(list(current_combination))
                return
            
            # Base case: if sum exceeds target, stop exploring this path
            if current_sum > target:
                return
            
            # Explore candidates starting from start_idx to avoid duplicates
            for i in range(start_idx, len(candidates)):
                # Choose the candidate
                current_combination.append(candidates[i])
                
                # Recurse with the same index 'i' because we can reuse elements
                backtrack(i, current_combination, current_sum + candidates[i])
                
                # Backtrack: remove the last candidate added
                current_combination.pop()
        
        backtrack(0, [], 0)
        return res