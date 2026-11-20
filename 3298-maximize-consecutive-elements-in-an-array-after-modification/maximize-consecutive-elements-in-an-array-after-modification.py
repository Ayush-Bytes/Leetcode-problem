class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        dp: dict[int, int] = {}
        ans = 0

        for x in nums:
            # Option 1: increment x -> x + 1, extending a sequence ending at x
            dp[x + 1] = max(dp.get(x + 1, 0), dp.get(x, 0) + 1)
            # Option 2: keep x as x, extending a sequence ending at x - 1
            dp[x] = max(dp.get(x, 0), dp.get(x - 1, 0) + 1)

            ans = max(ans, dp[x], dp[x + 1])

        return ans