class Solution {
    public long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long totalCost = 0;
        
        // 1. Satisfy the overlapping requirement using the cheaper option between costBoth and (cost1 + cost2)
        int commonNeed = Math.min(need1, need2);
        totalCost += (long) commonNeed * Math.min(costBoth, (long) cost1 + cost2);
        
        // 2. Satisfy the remaining requirement for type 1 (if need1 > need2)
        if (need1 > need2) {
            int rem1 = need1 - need2;
            totalCost += (long) rem1 * Math.min(cost1, costBoth);
        }
        
        // 3. Satisfy the remaining requirement for type 2 (if need2 > need1)
        else if (need2 > need1) {
            int rem2 = need2 - need1;
            totalCost += (long) rem2 * Math.min(cost2, costBoth);
        }
        
        return totalCost;
    }
}