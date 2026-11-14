import java.util.List;

class Solution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        int minSum = Integer.MAX_VALUE;
        int n = nums.size();
        
        // Iterate over all possible starting points of the subarray
        for (int i = 0; i < n; i++) {
            int currentSum = 0;
            // Iterate over all possible lengths from l to r
            for (int j = i; j < n; j++) {
                currentSum += nums.get(j);
                int length = j - i + 1;
                
                if (length >= l && length <= r) {
                    if (currentSum > 0) {
                        minSum = Math.min(minSum, currentSum);
                    }
                }
                
                // If length exceeds r, we can stop extending this subarray
                if (length > r) {
                    break;
                }
            }
        }
        
        return minSum == Integer.MAX_VALUE ? -1 : minSum;
    }
}