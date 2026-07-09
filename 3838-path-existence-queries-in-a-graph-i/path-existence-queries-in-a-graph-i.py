class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
       
        component_id = [0] * n
        current_id = 0
        
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                current_id += 1
            component_id[i] = current_id

        ans = []
        for u, v in queries:
            ans.append(component_id[u] == component_id[v])
            
        return ans