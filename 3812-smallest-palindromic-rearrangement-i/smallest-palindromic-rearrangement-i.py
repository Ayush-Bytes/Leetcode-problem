class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        half_len = n // 2
        
        left_half = "".join(sorted(s[:half_len]))
        
        mid = s[half_len] if n % 2 != 0 else ""
        
        return left_half + mid + left_half[::-1]