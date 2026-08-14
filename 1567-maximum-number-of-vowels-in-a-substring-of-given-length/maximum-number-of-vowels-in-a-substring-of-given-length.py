class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        n=len(s)
        count_of_vowels=0
        for ch in range(k):
            if s[ch] in vowels:
                count_of_vowels+=1
        ans = count_of_vowels
        for ch in range(k,n):
            if s[ch] in vowels:
                count_of_vowels +=1
            if s[ch - k] in vowels:
                count_of_vowels -= 1
            ans = max(ans,count_of_vowels)
        return ans

