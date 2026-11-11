class Solution {
    public int climbStairs(int n, int[] costs) {
        // dp[j] stores the minimum total cost to reach step j.
        // Since costs is 1-indexed of length n, our steps go from 0 to n.
        long[] dp = new long[n + 1];
        
        // Base case: starting at step 0 with cost 0
        dp[0] = 0;
        
        for (int j = 1; j <= n; j++) {
            long minCost = Long.MAX_VALUE;
            
            // We can jump from i to j where j - i can be 1, 2, or 3
            for (int k = 1; k <= 3; k++) {
                int i = j - k;
                if (i >= 0) {
                    // cost[j] in 1-indexed array corresponds to costs[j - 1] in 0-indexed Java array
                    long jumpCost = dp[i] + costs[j - 1] + (long)(j - i) * (j - i);
                    minCost = Math.min(minCost, jumpCost);
                }
            }
            dp[j] = minCost;
        }
        
        return (int) dp[n];
    }
}