class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        
        # Iterate through bracket boundaries: 10^3, 10^6, 10^9, 10^12, 10^15
        # Each bracket adds 1 more comma to numbers within it
        lower = 1000
        commas = 1
        
        while lower <= n:
            upper = min(n, lower * 1000 - 1)
            total_commas += (upper - lower + 1) * commas
            lower *= 1000
            commas += 1
            
        return total_commas
        