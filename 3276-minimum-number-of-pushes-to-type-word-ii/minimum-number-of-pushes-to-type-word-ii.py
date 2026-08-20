from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Step 1: Count frequency of each character
        freq = Counter(word)
        
        # Step 2: Sort frequencies in descending order
        sorted_freqs = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        
        # Step 3: Calculate minimum pushes based on position
        for i, count in enumerate(sorted_freqs):
            # First 8 characters take 1 push, next 8 take 2 pushes, etc.
            pushes = (i // 8) + 1
            total_pushes += count * pushes
            
        return total_pushes