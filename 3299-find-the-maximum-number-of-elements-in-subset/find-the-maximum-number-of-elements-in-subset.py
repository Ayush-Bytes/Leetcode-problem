from collections import Counter

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        count = Counter(nums)
        ans = 0
        
        if count[1] > 0:
            ans = count[1] if count[1] % 2 != 0 else count[1] - 1
            

        for x in count:
            if x == 1: continue
            
            curr_len = 0

            while count[x] >= 2:
                curr_len += 2
                x = x * x  

                if count[x] >= 1:
                    ans = max(ans, curr_len + 1)
                else:

                    ans = max(ans, curr_len - 1) 
                    break
            else:
               
                if count[x] >= 1:
                    ans = max(ans, curr_len + 1)
                elif curr_len > 0:
                    ans = max(ans, curr_len - 1)
                
        return ans