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
                # We found a ')'
                # Check if the next character is also ')'
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    # Only one ')' found, need to insert another one
                    res += 1
                    i += 1
                
                # Try to match with an available opening parenthesis
                if left > 0:
                    left -= 1
                else:
                    # No opening parenthesis available, need to insert '('
                    res += 1
                    
        # Any remaining unmatched opening parenthesis needs two ')' each
        res += left * 2
        return res