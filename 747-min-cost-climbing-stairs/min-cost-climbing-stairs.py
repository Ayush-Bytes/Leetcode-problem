class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        prev1 = 0
        prev2 = 0
        result = prev2

        for i in range(2,n+1):
            result = min(prev2 + cost[i-1], prev1 + cost[i-2])

            prev1 = prev2
            prev2 = result

        return result