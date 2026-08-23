class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum_left = sum(int(c) for c in num[:half] if c != '?')
        sum_right = sum(int(c) for c in num[half:] if c != '?')
        
        q_left = num[:half].count('?')
        q_right = num[half:].count('?')
        
        # Balance equation: (sum_left - sum_right) * 2 == (q_right - q_left) * 9
        return (sum_left - sum_right) * 2 != (q_right - q_left) * 9