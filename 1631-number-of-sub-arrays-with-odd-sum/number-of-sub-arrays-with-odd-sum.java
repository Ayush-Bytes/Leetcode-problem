class Solution {
    public int numOfSubarrays(int[] arr) {
        long oddCount = 0;
        long evenCount = 1; // Base case for prefix sum 0 (even)
        long currentSum = 0;
        long totalSubarrays = 0;
        long MOD = 1_000_000_007;

        for (int num : arr) {
            currentSum += num;
            
            if (currentSum % 2 == 1) {
                totalSubarrays = (totalSubarrays + evenCount) % MOD;
                oddCount++;
            } else {
                totalSubarrays = (totalSubarrays + oddCount) % MOD;
                evenCount++;
            }
        }

        return (int) totalSubarrays;
    }
}