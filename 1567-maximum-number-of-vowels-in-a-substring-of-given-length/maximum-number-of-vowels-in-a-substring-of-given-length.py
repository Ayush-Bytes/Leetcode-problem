class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        
        # Count vowels in the first window of size k
        current_vowels = sum(1 for i in range(k) if s[i] in vowels)
        max_vowels = current_vowels
        
        # Slide the window across the rest of the string
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels += 1
            if s[i - k] in vowels:
                current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)
            
        return max_vowels