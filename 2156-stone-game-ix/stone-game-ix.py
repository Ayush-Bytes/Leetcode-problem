class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt0 = sum(1 for x in stones if x % 3 == 0)
        cnt1 = sum(1 for x in stones if x % 3 == 1)
        cnt2 = sum(1 for x in stones if x % 3 == 2)
        
        if cnt0 % 2 == 0:
            return cnt1 >= 1 and cnt2 >= 1
        else:
            return abs(cnt1 - cnt2) > 2