class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        left = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                left += 1
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    res += 1
                    i += 1
                
                if left > 0:
                    left -= 1
                else:
                    res += 1
                    
        res += left * 2
        return res