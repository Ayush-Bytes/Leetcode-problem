class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        half_len = n // 2
        
        # Sort the first half to get the smallest left side
        left_half = "".join(sorted(s[:half_len]))
        
        # If length is odd, keep the middle character
        mid = s[half_len] if n % 2 != 0 else ""
        
        # Right half is the reverse of the left half
        return left_half + mid + left_half[::-1]