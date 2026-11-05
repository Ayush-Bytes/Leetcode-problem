import java.util.*;

class Solution {
    static class SlidingWindowMedianCost {
        int x;
        TreeMap<Long, Integer> left = new TreeMap<>();
        TreeMap<Long, Integer> right = new TreeMap<>();
        int leftSize = 0, rightSize = 0;
        long leftSum = 0, rightSum = 0;

        public SlidingWindowMedianCost(int x) {
            this.x = x;
        }

        private void balance() {
            int targetLeft = (x + 1) / 2;
            
            while (leftSize < targetLeft && !right.isEmpty()) {
                Map.Entry<Long, Integer> entry = right.firstEntry();
                long val = entry.getKey();
                int count = entry.getValue();
                
                if (count == 1) right.remove(val);
                else right.put(val, count - 1);
                
                rightSize--;
                rightSum -= val;
                
                left.put(val, left.getOrDefault(val, 0) + 1);
                leftSize++;
                leftSum += val;
            }
            
            while (leftSize > targetLeft && !left.isEmpty()) {
                Map.Entry<Long, Integer> entry = left.lastEntry();
                long val = entry.getKey();
                int count = entry.getValue();
                
                if (count == 1) left.remove(val);
                else left.put(val, count - 1);
                
                leftSize--;
                leftSum -= val;
                
                right.put(val, right.getOrDefault(val, 0) + 1);
                rightSize++;
                rightSum += val;
            }
        }

        public void add(long val) {
            if (left.isEmpty() || val <= left.lastKey()) {
                left.put(val, left.getOrDefault(val, 0) + 1);
                leftSize++;
                leftSum += val;
            } else {
                right.put(val, right.getOrDefault(val, 0) + 1);
                rightSize++;
                rightSum += val;
            }
            balance();
        }

        public void remove(long val) {
            if (left.containsKey(val)) {
                int count = left.get(val);
                if (count == 1) left.remove(val);
                else left.put(val, count - 1);
                leftSize--;
                leftSum -= val;
            } else if (right.containsKey(val)) {
                int count = right.get(val);
                if (count == 1) right.remove(val);
                else right.put(val, count - 1);
                rightSize--;
                rightSum -= val;
            }
            balance();
        }

        public long getCost() {
            if (left.isEmpty()) return 0;
            long median = left.lastKey();
            long leftCost = median * leftSize - leftSum;
            long rightCost = rightSum - median * rightSize;
            return leftCost + rightCost;
        }
    }

    public long minOperations(int[] nums, int x, int k) {
        int n = nums.length;
        long[] cost = new long[n - x + 1];
        
        SlidingWindowMedianCost sw = new SlidingWindowMedianCost(x);
        for (int i = 0; i < x; i++) {
            sw.add(nums[i]);
        }
        cost[0] = sw.getCost();
        
        for (int i = x; i < n; i++) {
            sw.remove(nums[i - x]);
            sw.add(nums[i]);
            cost[i - x + 1] = sw.getCost();
        }

        // DP table: dp[i][j] = min cost using up to index i with j windows
        long[][] dp = new long[n + 1][k + 1];
        for (long[] row : dp) {
            Arrays.fill(row, Long.MAX_VALUE / 2);
        }
        
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 0;
        }

        for (int j = 1; j <= k; j++) {
            long minPrev = Long.MAX_VALUE / 2;
            for (int i = 1; i <= n; i++) {
                if (i >= x) {
                    minPrev = Math.min(minPrev, dp[i - x][j - 1] + cost[i - x]);
                }
                dp[i][j] = Math.min(dp[i - 1][j], minPrev);
            }
        }

        return dp[n][k];
    }
}