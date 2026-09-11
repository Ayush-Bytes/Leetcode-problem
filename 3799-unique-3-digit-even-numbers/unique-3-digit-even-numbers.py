from collections import Counter

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = Counter(digits)
        ans = set()
        
        # Try all 3-digit even numbers from 100 to 998 with step 2
        for num in range(100, 1000, 2):
            s = str(num)
            digit_count = Counter(int(d) for d in s)
            
            # Check if we have enough of each digit in our input array
            possible = True
            for d, freq in digit_count.items():
                if count[d] < freq:
                    possible = False
                    break
            
            if possible:
                ans.add(num)
                
        return len(ans)