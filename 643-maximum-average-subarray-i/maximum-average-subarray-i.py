class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        window_sum=0
        for i in range(k):
            window_sum += nums[i]
        ans=window_sum
        for i in range(k,n):
            window_sum+=nums[i]-nums[i-k]
            ans = max(ans,window_sum)
        return ans/k
