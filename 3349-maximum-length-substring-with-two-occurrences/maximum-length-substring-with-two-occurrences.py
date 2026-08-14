class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        from collections import defaultdict
        
        count = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            
            # If any character count exceeds 2, shrink the window from the left
            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1
                
            # Update the maximum valid substring length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len